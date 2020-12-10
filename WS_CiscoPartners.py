# originalUrl: 'https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/openBasicSearch.do'
import requests, json
import pandas as pd

s =requests.Session()

headers = {
    'sec-fetch-mode': 'cors',
    'origin': 'https://locatr.cloudapps.cisco.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,fr;q=0.6',
    'adrum': 'isAjax:true',
    'refer': 'https://www.cisco.com/c/en/us/partners/partner-with-cisco/become-an-integrator.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/openBasicSearch.do',
    'authority': 'locatr.cloudapps.cisco.com',
    'sec-fetch-site': 'same-origin',
}


# out = open('/home/zdai/Tesla/corpFiles/ciso.json','a')
# out.truncate(0)
# out.write('[\n')
first=0

for i in range(1):

    data = '{"SEARCH_PARAM":{"SEARCH_CRITERIA":[{"CATEGORY_ID":"1","CATEGORY_DISPLAY_NAME":"Country","LANGUAGE_CD":"EN","PARENT_CATEGORY_DESC":"LOCATION","KEYWORD_ID":"^136560940^","PARENT_CATEGORY_ID":"1","CATEGORY_TYPE":"SEARCH","KEYWORD_DISPLAY_NAME":"PERU","$$hashKey":"object:784"}],"START_INDEX":%i,"END_INDEX":%i,"ADVANCED_FILTERS":[],"SORT_FILTER":[],"SORT_TYPE":"BADGE_RANK ASC"},"LANGUAGE_CD":"EN"}' % (i*1000,(i+1)*1000)

    response = s.post('https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/service/searchService/getSearchResults/', headers=headers, data=data)

    result = response.json()
    if result:
        corps = result['docs']
        for corp in corps:
            result={}
            if 'SITE_NAME' in corp:
                result['name']=corp['SITE_NAME']
            else:
                result['name']=''
            if 'LOC_COORDINATES' in corp:
                result['ll']=corp['LOC_COORDINATES']
            else:
                result['ll']=''
            if 'WEB_ADDR' in corp:
                result['web']=corp['WEB_ADDR']
            else:
                result['web']=''
            if 'SITE_ADDR_1' in corp:
                result['addressLine']=corp['SITE_ADDR_1']
            else:
                result['addressLine']=''
            if 'SITE_CITY' in corp:
                result['city']=corp['SITE_CITY']
            else:
                result['city']=''
            if 'SITE_STATE' in corp:
                result['state']=corp['SITE_STATE']
            else:
                result['state']=''
            if 'SITE_ZIP' in corp:
                result['zip']=corp['SITE_ZIP']
            else:
                result['zip']=''
            if 'SITE_COUNTRY' in corp:
                result['country']=corp['SITE_COUNTRY']
            else:
                result['country']=''
            if 'SITE_PHONE' in corp:
                result['phone']=corp['SITE_PHONE']
            else:
                result['phone']=''
            df=pd.DataFrame([result])
            df.to_csv('ciscoPartnersColombia.csv',mode='a',index=0,header=(first==0))
            first+=1
# out.write(']')
# out.close()
