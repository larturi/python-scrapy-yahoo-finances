import os
import json
import scrapy
    
class SpiderYahoo(scrapy.Spider):
    name = 'yahoo'
    start_urls = ['https://finance.yahoo.com/quote/TECO2.BA']
    custom_settings = {
        'FEEDS': {
            'yahoo.json': {
                'format': 'json',
                'overwrite': True,
                'encoding': 'utf-8',
                'indent': 4
            }
        }
    }

    def start_requests(self):
        urls = [
            'https://finance.yahoo.com/quote/TECO2.BA',
            'https://finance.yahoo.com/quote/TEO',
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
            
    def parse(self, response):
    
        keys = [
            'previous_close',
            'open',
            'bid',
            'ask',
            'days_range',
            'week_range_52',
            'avg_volume',
            'market_cap',
            'beta_5Y_monthly',
            'pe_ratio_ttm',
            'eps_ttm',
            'forward_dividend_and_yield',
            'ex_dividend_Date',
            'target_est_1y',
        ]
        
        values = response.xpath(
            '//div[@id="quote-summary"]//tbody/tr/td/text()'
        ).getall()
        
        data = {}
        for i in range(len(keys)):
            data[keys[i]] = values[i]
            
        # Add Volume attribute to object data response
        volume = response.xpath('//*[@id="quote-summary"]//fin-streamer/text()').get()
        data['volume'] = volume
        
        return {
            'link': response.url,
            'data': data,
        }

  