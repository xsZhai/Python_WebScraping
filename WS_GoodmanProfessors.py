# this scrip gets all contact information of presessors in Goodman School of Business in Brock University

import requests
from lxml import html

originalweb="https://brocku.ca/goodman/faculty-research/faculty-directory/"
originaltarget='//div[@class="vc_row wpb_row vc_row-fluid"][3]//a/@href'
name="//h1[@class='entry-title']/text()"
title="//div[@class='wpb_wrapper']/h2/text()"
contact="//div[@class='wpb_wrapper']/p//text()"


web=requests.get(originalweb)
print(web.content)
targetwebs=html.fromstring(web.content).xpath(originaltarget)
print(targetwebs[0])
len(targetwebs)

professor=open("professor.text","a")

for link in targetwebs:


    targetwebsall=requests.get(link)
    targetwebshl=html.fromstring(targetwebsall.content)

    targetname=(targetwebshl.xpath(name)+[''])[0].replace('\n',' ')
    targettitle=(targetwebshl.xpath(title)+[''])[0].replace('\n',' ')
    targetcontact=' '.join(map(str,targetwebshl.xpath(contact))).replace('\n',' ')


    targetall= ' '.join([targetname,targettitle,targetcontact])+'\n'
    print(targetall)

    professor.write(targetall)

professor.close()
