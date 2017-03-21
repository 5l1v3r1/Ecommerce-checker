# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import re

class EcommerceSpider(scrapy.Spider):
    name = "ecommerce"
    filename = 'result.txt'
    template = "{0:50}  {1:5}"

    def start_requests(self):
        with open(self.filename, 'w') as f:
            f.write(self.template.format('Website', 'Ecommerce\n'))
        urls = []
        with open('websites.txt', 'r') as input_file:
            for line in input_file:
                urls.append(line[:-1])
        for url in urls:
            yield scrapy.Request(url='http://' + url, callback=self.parse)
            

    def parse(self, response):
        theHTML = response.body
        def findWholeWord(w):
            return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
        with open(self.filename, 'a+') as f:
            find = findWholeWord('cart')(theHTML)
            if find != None:
                f.write(self.template.format(response.url, 'true\n'))
            else: f.write(self.template.format(response.url, 'false\n'))



    
