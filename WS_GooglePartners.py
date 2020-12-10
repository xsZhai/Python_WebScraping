
# originalUrl: 'https://cloud.withgoogle.com/partners/?sort-type=DISTANCE&address-location=GB'

import requests, json
import pandas as pd

s = requests.Session()

headers = {
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://cloud.withgoogle.com/partners',
    'Origin': 'https://cloud.withgoogle.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8;',
}

params = (
    ('key', 'AIzaSyAt_7JVd31O9f7TbBNgL_qNNYwjvzANz8A'),
)

npt = ''

# page
def get_corp(cid):
    response = s.get('https://cloudpartner.googleapis.com/v1/directory/profiles/ACkb94bwDdkNHZ6oKSQZKXlksfpPSxPOYClT3D7ysr_DWAUtsFza_x5SyQtGyhcZHbbBJdkPcfLP', headers=headers, params=params)
    response = s.get('https://cloudpartner.googleapis.com/v1/directory/profiles/%s' % cid, headers=headers, params=params)
    id=response.json()['id']
    name=response.json()['displayName']
    result={}
    address=response.json()['offices'][0]['address']
    if 'email' in response.json()['offices'][0]:
        email=response.json()['offices'][0]['email']
    else:
        email=''
    if 'phoneNumber' in response.json()['offices'][0]:
        phone=response.json()['offices'][0]['phoneNumber']
    else:
        phone=''
    if 'website' in response.json()['offices'][0]:
        web=response.json()['offices'][0]['website']
    else:
        web=''
    result['id']=id
    result['name']=name
    result['address']=address
    result['email']=email
    result['phone']=phone
    result['web']=web

    return result

gotnum = 0
totalnum = 5420
# out = open('googlepartnerid.csv','a')
# out.truncate(0)
# out.write('[\n')
first=0

while gotnum < totalnum:
    data = '{"query":"","language":"en","engagementTypes":[],"expertises":[],"industries":[],"initiatives":[],"partnerTypes":[],"regions":[],"specializations":[],"addressLocation":"Brazil","sortOptions":{"sortDimension":"DISTANCE","sortOrder":"SORT_ORDER_UNSPECIFIED"},"pageToken":"%s"}' % npt

    response = s.post('https://cloudpartner.googleapis.com/v1/directory/profiles:search', headers=headers, params=params, data=data)

    result = response.json()
    npt = result['nextPageToken']
    numin = len(result['matchingProfiles'])
    gotnum += numin
    print(gotnum)
    for line in result['matchingProfiles']:
        try:
            cid =line['id']
            corp = get_corp(cid)
            df=pd.DataFrame([corp])
            df.to_csv('googlepartnerid1209.csv',mode='a',index=0,header=(first==0))
            first+=1
        except Exception as e:
            print(e)
        # out.write(cid+',\n')

# out.write(']')
# out.close()

print('done')
