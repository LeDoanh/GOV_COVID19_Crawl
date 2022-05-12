import scrapy
import json
from GOV_Covid19.items import COVID19_pandemic
from datetime import date

class GOV_Covid19(scrapy.Spider):
    name = 'GOV_Covid19'
    api = 'https://static.pipezero.com/covid/data.json'
    _id = 1
    
    custom_settings = {"FEEDS": {"Covid19.json": {"format": "json"}}}
    
    def start_requests(self):
        yield scrapy.Request(url = self.api, callback = self.parse)
        
    def parse(self, response):
        Data_covid = json.loads(response.body)
        situation_today = COVID19_pandemic()
        
        for data in Data_covid['locations']:
            situation_today['_id'] = self._id
            self._id += 1
            situation_today['name'] = data['name']
            situation_today['cases'] = data['cases']
            situation_today['casesToday'] = data['casesToday']
            situation_today['death'] = data['death']
            # situation_today['time'] = date.today().strftime('%d/%m/%Y')
            yield situation_today