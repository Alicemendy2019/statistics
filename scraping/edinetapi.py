import requests
import json
import sys

# ref : https://non-dimension.com/get-xbrldata/
# res.headers見たほうがいいか

def get_info(year,month):
    endpoint='https://disclosure.edinet-fsa.go.jp/api/v1/documents.json'
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
        f=open('EDINET/'+params['date']+'_cnt'+cnt+'.csv','w')
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
        filename = 'EDINET/' + document + '.zip'
        if res.status_code == 200:
            with open(filename,'wb') as f:
                for c in res.iter_content(chunk_size=1024):
                    f.write(c)
        else:
            print(res.status_code)
def show_ditail_info(docID):
    import zipfile
    import glob
    from bs4 import BeautifulSoup
    import os
    filepath1='EDINET/' + docID
    print(filepath1)
    data = zipfile.ZipFile(filepath1+ '.zip')
    data.extractall(filepath1)
    filepath2=filepath1 + '/XBRL/PublicDoc/'
    # filepath2='test' + '/XBRL/PublicDoc/'
    files=glob.glob(filepath2+'*.htm')
    files = sorted(files)
    targetfile=files[1]
    print(targetfile)
    with open(targetfile,encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    tagP=soup.find_all('p')
    for p in tagP:
        print(p.text)

if __name__ == '__main__':
    while True:
        indata=input('数値で入力してください\n1:月ごとの開示請求情報取得\n2:詳細データ保存\n3:詳細データ表示\n9:終了\n---> ')
        if indata == '1':
            ym=input('年月を入力してください')
            year=ym[:4]
            month=ym[4:].replace('-','').rjust(2,'0')
            if len(year) == 4 and len(month) ==2:
                get_info(year,month)
            else:
                print(year)
                print(month)
        elif indata == '2':
            documents = ['S100IBHG','S100I62D']
            save_detail_info(documents)
        elif indata == '3':
            docID='S100IBHG'
            show_ditail_info(docID)
        elif indata == '9':
            sys.exit()
        else:
            print('不正な入力です')
            sys.exit()
