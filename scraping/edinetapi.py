import requests
import json
import sys
import zipfile
import glob
from bs4 import BeautifulSoup
import os
import pandas
# ref : https://non-dimension.com/get-xbrldata/
# res.headers見たほうがいいか

def get_info(year,month):
    endpoint='https://disclosure.edinet-fsa.go.jp/api/v1/documents.json'
    wfilepath='EDINET/metadata/'+year+'-'+month+'/'
    if os.path.exists(wfilepath) is False:
        os.mkdir(wfilepath)
    for i in range(1,32):
        day = str(i).rjust(2,'0')
        params = {
          "date" : '{}-{}-{}'.format(year,month,day),
          "type" : 2
        }
        res=requests.get(endpoint,params=params, verify=False)
        # res.encoding = res.apparent_encoding
        if res.json()['metadata']['status'] != '200':
            print('err')
            print(res.json()['metadata']['status'])
            continue

        jdata = json.loads(res.text)
        cnt=str(jdata['metadata']['resultset']['count'])
        print('件数:'+cnt)

        f=open(wfilepath+params['date']+'_cnt'+cnt+'.csv','w',encoding='utf-8')
        f.write( \
        'docID' +','+ \
        'secCode' +','+ \
        'JCN' +','+ \
        'filerName' +','+ \
        'fundCode' +','+ \
        'docDescription' +','+ \
        'docTypeCode' +','+ \
        'periodStart' +','+ \
        'periodEnd' +','+ \
        'submitDateTime' +','+ \
        'xbrlFlag' + '\n' )

        results=jdata['results']
        for result in results:
            f.write( \
            str(result['docID']) +','+ \
            str(result['secCode']) +','+ \
            str(result['JCN']) +','+ \
            str(result['filerName']) +','+ \
            str(result['fundCode']) +','+ \
            str(result['docDescription']) +','+ \
            str(result['docTypeCode']) +','+ \
            str(result['periodStart']) +','+ \
            str(result['periodEnd']) +','+ \
            str(result['submitDateTime']) +','+ \
            str(result['xbrlFlag']) + '\n' )
        f.close()


def save_detail_info(documents):
    endpoint1='https://disclosure.edinet-fsa.go.jp/api/v1/documents/'
    for document in documents:
        filename = 'EDINET/zip/' + document + '.zip'
        if os.path.exists(filename) is False:
            endpoint=endpoint1+document
            params={
                'type':1 #書類本文＋監査報告書＋XBRLファイル
            }
            res=requests.get(endpoint,params=params,verify=False)
            res.encoding = res.apparent_encoding

            if res.status_code == 200:
                with open(filename,'wb') as f:
                    for c in res.iter_content(chunk_size=1024):
                        f.write(c)
            else:
                print(res.status_code)
        else:
            print(filename+'は存在しています')

def show_ditail_info(docID):
    filepath1='EDINET/zip/' + docID
    filepathS='EDINET/extractData/' + docID
    if os.path.exists(filepathS) is False:
            # os.mkdir(filepathS)
        print(filepath1)
        data = zipfile.ZipFile(filepath1+ '.zip')
        data.extractall(filepathS)
    else:
        print('data存在しています'+filepathS)
    filepath2=filepathS + '/XBRL/PublicDoc/'
    # filepath2='test' + '/XBRL/PublicDoc/'
    files=glob.glob(filepath2+'*.htm')
    files = sorted(files)
    targetfile=files[1]
    print(targetfile)
    with open(targetfile,encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    tagP2=soup.select('p.smt_tblC,p.smt_tblL,p.smt_tblR')
    for p in tagP2:
        print(p.text)

def select_sec_data(year,month):
    savepath='EDINET/seccode/secdata.csv'
    orgdatapath='EDINET/metadata/'+year+'-'+month+'/'
    files=glob.glob(orgdatapath+'*.csv')
    if len(files) == 0:
        print('dataがありません')
        return
    with open(savepath,'a') as f:
        for file in files:
            fr = pandas.read_csv(file,header=0)
            for row in fr.itertuples():
                if row.secCode != 'None':
                    f.write(",".join(map(str,row[1:]))+'\n')

def get_ym():
    ym=input('年月を入力してください')
    year=ym[:4]
    month=ym[4:].replace('-','').rjust(2,'0')
    if len(year) == 4 and len(month) ==2:
        return year,month
    else:
        print('不正な入力値です')
        print(year)
        print(month)
        return 'err',''

def get_file():
    abs_file=input('ファイルをフルパスで入力してください')
    root, ext = os.path.splitext(abs_file)
    if ext == '.xbrl':
        return abs_file
    else:
        print(os.path.isfile(abs_file))
        print(ext)
        print('xbrlを入力してください')

def parse_xbrl_data(file):
    # XBRLから利益等情報を取得する（仮）
    # todo : 他の定義情報もkeys()で確認し取得
    from xbrl import XBRLParser
    # import codecs
    from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
    import csv
    # XBRLファイルを開いて定義情報を取得
    # f=r"C:\Users\amepa\Documents\仕事\beyoufree\Python\statistics\scraping\EDINET\extractData\S100IKPS\XBRL\PublicDoc\jpcrp040300-q1r-001_E26815-000_2020-03-31_01_2020-05-14.xbrl"
    f=file
    print(f)
    with open(f,encoding='utf8') as of:
        pa=XBRLParser.parse(of)
        context_ref_piriod = {}
        # for n in pa.find_all('xbrli:context',{'id':['Prior1YTDDuration','CurrentYTDDuration','Prior1YearDuration']}):
        for n in pa.find_all('xbrli:context'):
            id=n.get_attribute_list('id')
            child=n.findChildren(['xbrli:instant', 'xbrli:period'])
            # if child.name ==
            piriod=child[0].get_text().strip('\n').replace('\n',' ～ ')
            context_ref_piriod[id[0]] = piriod

    # 取得したい情報をDBから取得したCSVをもとに抽出
    p=EdinetXbrlParser()
    # f=r"C:\Users\amepa\Documents\仕事\beyoufree\Python\statistics\scraping\EDINET\extractData\S100IKPS\XBRL\PublicDoc\jpcrp040300-q1r-001_E26815-000_2020-03-31_01_2020-05-14.xbrl"
    d=p.parse_file(f)
    rf = r"EDINET\template\wnt_data.csv"
    with open(rf) as f:
        ff = csv.reader(f)
        for row in ff:
            d2=d.get_data_list(row[2])
            # print(d2)
            if len(d2) == 0:
                print(row[1] + ': None' )
            else:
                for rd in d2:
                    if rd.get_context_ref() in context_ref_piriod.keys():
                        print(row[1] + ':' + str(rd.value) + ':' + context_ref_piriod[rd.get_context_ref()])
                    elif rd is None:
                        print(row[1] + ':' + 'None')
                    else :
                        print(row[1] + ':' + str(rd.value) + ':' + rd.get_context_ref())

if __name__ == '__main__':
    while True:
        indata=input('数値で入力してください\n1:月ごとの開示請求情報取得\n2:詳細データ保存\n\
3:詳細データ表示\n4:証券コード有データ取得保存\n\
5:XRBLファイル情報取得\n9:終了\n---> ')
        if indata == '1':
            year,month = get_ym()
            if year == 'err':
                pass
            else:
                get_info(year,month)
        elif indata == '2':
            documents = ['S100IKPS']
            save_detail_info(documents)
        elif indata == '3':
            docID='S100IKPS'
            show_ditail_info(docID)
        elif indata == '4':
            year,month = get_ym()
            if year == 'err':
                pass
            else:
                select_sec_data(year,month)
        elif indata == '5':
            # file=get_file()
            file=r"C:\Users\yohei\AppData\Local\Git\statistics\scraping\EDINET\extractData\S100I9DG\XBRL\PublicDoc\jpcrp030000-asr-001_E26815-000_2019-12-31_01_2020-03-23.xbrl"
            if file is None:
                pass
            # elif :
                file=r"C:\Users\amepa\Documents\仕事\beyoufree\Python\statistics\scraping\EDINET\extractData\S100IKPS\XBRL\PublicDoc\jpcrp040300-q1r-001_E26815-000_2020-03-31_01_2020-05-14.xbrl"
            else:
                parse_xbrl_data(file)
        elif indata == '9':
            sys.exit()
        else:
            print('不正な入力です')
            sys.exit()

"""
四半期のXBRLは１１ファイル
# https://www.fsa.go.jp/search/20160314/1b_1.pdf#search='%E3%82%BF%E3%82%AF%E3%82%BD%E3%83%8E%E3%83%9F+%E5%AE%9A%E7%BE%A9+%E6%A7%98%E5%BC%8F'

"""
