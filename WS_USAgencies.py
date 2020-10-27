# got information of federal agencies from a certain website
import requests
from lxml import html
import pandas as pd

originalweb='https://www.usa.gov/federal-agencies/a'
originaltarget="//ul[@class='one_column_bullet']/li/a[@class='url']//@href"
name='//article/header[1]/h1/text()'
website="//article/section[@class='otln'][1]/p/a/@href"
address="//p[@class='spk street-address']//text()"
email="//*[text()='Email:']/ancestor::section//p//text()"
phone="//article/section[@class='otln'][3]/p[@class='spk tel']/span[@class='num']/text()"
tollfree="//section[@class='otlnrw'][3]/p[@class='spk tel']/span[@class='num']/text()"
branch="//*[text()='Government branch:']/ancestor::section//p//text()"
pagelist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w']

first=0
for num in pagelist:
    web=requests.get("https://www.usa.gov/federal-agencies/%s" % str(num))
    targetwebs=html.fromstring(web.content).xpath(originaltarget)
    for targetweb in targetwebs:
      testurl=requests.get("https://www.usa.gov"+targetweb).content
      testname=html.fromstring(testurl).xpath('//article/header[1]/h1/text()')
      testwebsite=html.fromstring(testurl).xpath("//article/section[@class='otln'][1]/p/a/@href")
      testaddress=html.fromstring(testurl).xpath("//p[@class='spk street-address']//text()")
      targetaddress=[]
      for a in testaddress:
        b=a.strip()
        targetaddress.append(b)
      testemail=html.fromstring(testurl).xpath("//*[text()='Email:']/ancestor::section//p//text()")
      testemail2=[]
      for a in testemail:
        b=a.strip()
        testemail2.append(b)
      testphone=html.fromstring(testurl).xpath("//article/section[@class='otln'][3]/p[@class='spk tel']/span[@class='num']/text()")
      testtollfree=html.fromstring(testurl).xpath("//section[@class='otlnrw'][3]/p[@class='spk tel']/span[@class='num']/text()")
      testbranch=html.fromstring(testurl).xpath("//*[text()='Government branch:']/ancestor::section//p//text()")
      line={}
      line['name']=';'.join(testname).replace('\n','')
      line['web']=';'.join(testwebsite).replace('\n','')
      line['address']=';'.join(targetaddress).replace('\n','')
      line['email']=';'.join(testemail2).replace('\n','')
      line['phone']=';'.join(testphone).replace('\n','')
      line['tollfree']=';'.join(testtollfree).replace('\n','')
      line['branch']=';'.join(testbranch).replace('\n','')
      result=pd.DataFrame([line])
      print(result)
      pd.DataFrame([line]).to_csv('usagent.csv',index=0,header=(first==0),mode='a')
      first+=1
