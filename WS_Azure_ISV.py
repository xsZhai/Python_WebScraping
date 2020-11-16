
#scraping invividual software developers from Azure marketplace website

import requests
from lxml import html
import re
import kumihotools

def toDomain(link):
    import re
    return (re.sub(r'^(https?://)?(www\d?\.)?','', link).split('/')+[''])[0].strip()

for num in range(121,239):
    print(num)
    azureWebs=open('azure_ISV_webs.csv',mode='a')
    res=requests.get("https://azuremarketplace.microsoft.com/en-ca/marketplace/apps?filters=partners&page="+str(num))

    Xlinks="//a[@class='tileLink']/@href"

    Links=html.fromstring(res.content).xpath(Xlinks)
    for link in Links:
        try:
            res2=requests.get("https://azuremarketplace.microsoft.com"+link)
            Xurl="//div[@class='link']/a[@class='c-hyperlink linkContent'][1]/@href"
            url=html.fromstring(res2.content).xpath(Xurl)
        except Exception as e:
            print(e)
            continue
        if url:
            original_url=toDomain(url[0])
            print(original_url)
            azureWebs.write(original_url+'\n')
azureWebs.close()

print('---------done---------')
