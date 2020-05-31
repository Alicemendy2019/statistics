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
        endpoint=endpoint1+document
        params={
            'type':1
        }
        res=requests.get(endpoint,params=params,verify=False)
        res.encoding = res.apparent_encoding
        filename = 'EDINET/zip/' + document + '.zip'
        if res.status_code == 200:
            with open(filename,'wb') as f:
                for c in res.iter_content(chunk_size=1024):
                    f.write(c)
        else:
            print(res.status_code)
def show_ditail_info(docID):

    filepath1='EDINET/zip/' + docID
    filepathS='EDINET/extractData/' + docID
    print(filepath1)
    data = zipfile.ZipFile(filepath1+ '.zip')
    data.extractall(filepathS)
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

if __name__ == '__main__':
    while True:
        indata=input('数値で入力してください\n1:月ごとの開示請求情報取得\n2:詳細データ保存\n\
3:詳細データ表示\n4:証券コード有データ取得保存\n9:終了\n---> ')
        if indata == '1':
            year,month = get_ym()
            if year == 'err':
                pass
            else:
                get_info(year,month)
        elif indata == '2':
            documents = ['S100I9DG']
            save_detail_info(documents)
        elif indata == '3':
            docID='S100I9DG'
            show_ditail_info(docID)
        elif indata == '4':
            year,month = get_ym()
            if year == 'err':
                pass
            else:
                select_sec_data(year,month)
        elif indata == '9':
            sys.exit()
        else:
            print('不正な入力です')
            sys.exit()
