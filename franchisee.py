import requests
import pandas as pd
first=0

startnum=0
finishnum=390928
num_each_call=10000

while startnum<finishnum:

    headers = {
        'authority': 'www.franchimp.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.franchimp.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.franchimp.com/index.php?page=franchisees',
        'accept-language': 'en-CA,en;q=0.9,zh-CA;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'cookie': '__cfduid=ddf17c8f5f0c1677ecafc436d5945710e1608100335; _gid=GA1.2.65368760.1608563523; PHPSESSID=b092025340065fd35b4662903100c167; _ga_263BLJW05N=GS1.1.1608563523.2.1.1608565259.0; _ga=GA1.2.1750073772.1608100361; _gat_gtag_UA_131746798_1=1',
    }

    data = {
    'draw': '1',
    'columns[0][data]': 'franchiseeID',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'franchisor',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'true',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'franchiseeName',
    'columns[2][name]': '',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'true',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'business-name',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'true',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'email',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'phone',
    'columns[5][name]': '',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'false',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'address',
    'columns[6][name]': '',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'true',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': 'franchimpID',
    'columns[7][name]': '',
    'columns[7][searchable]': 'true',
    'columns[7][orderable]': 'true',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'order[0][column]': '1',
    'order[0][dir]': 'asc',
    'start': '%s'%startnum,
    'length': '%s'%num_each_call,
    'search[value]': '',
    'search[regex]': 'false'
    } 

    response = requests.post('https://www.franchimp.com/secondresponse.php', headers=headers, data=data)

    items=response.json()['data']

    for item in items:
        result={}
        result['business-name']=item['business-name']
        result['franchiseeName']=item['franchiseeName']
        result['franchisor']=item['franchisor']
        result['address']=item['address']
        result['state']=item['state']
        result['website']=item['website']
        df=pd.DataFrame([result])
        df.to_csv('franchisee1221.csv',mode='a',index=0,header=(first==0))
        first+=1
    startnum=startnum+num_each_call
    print(startnum)

print('------------done-----------')
