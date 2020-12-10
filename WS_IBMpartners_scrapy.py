import scrapy
import json
import pandas as pd


class IbmpartnerSpider(scrapy.Spider):
    name = 'ibmPartner'
    allowed_domains = ['ibm.com']
    start_urls = ['https://www.ibm.com/partnerworld/bpdirectory/api/businessPartner/retrieveBusinessPartners?search=&startindex=11&numresults=1910&sort=relevance&geo=DE']

    def parse(self, response):
        
        pd.DataFrame(response.json()['businessPartners']).to_csv('ibmPartners_DE.csv',index=0)
