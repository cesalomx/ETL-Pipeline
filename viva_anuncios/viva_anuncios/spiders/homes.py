import scrapy
from scrapy_selenium import SeleniumRequest

#my_class
class HomesSpider(scrapy.Spider):
    name = 'homes'
    #functions to clean data
    def remove_characters(self, value):
        return value.strip(' m²')

    def remove_coma(self, value):
        return value.strip(',')    
    
    def remove_plus(self,value):
        return value.strip('+')
    
    #Starting my request and doing the pagination using Selenium
    def start_requests(self):
        urls=[f'https://www.vivanuncios.com.mx/s-venta-inmuebles/queretaro/page-{i}/v1c1097l1021p50'.format(i) for i in range(1,51)]
        for url in urls:
            yield SeleniumRequest(
                url=url,
                wait_time=5,
                callback=self.parse
                )
    #scraping
    def parse(self, response):
        homes = response.xpath("//div[@id='tileRedesign']/div")
        for home in homes:
            yield {
                'price': home.xpath("normalize-space(.//span[@class='ad-price']/text())").get(),
                'location': home.xpath(".//div[@class='tile-location one-liner']/b/text()").get(),
                'description': home.xpath(".//div[@class='tile-desc one-liner']/a/text()").get(),
                'bathrooms': self.remove_plus(home.xpath("normalize-space(//div[@class='chiplets-inline-block re-bathroom']/text())").get()),
                'bedrooms': self.remove_plus(home.xpath("normalize-space(.//div[@class='chiplets-inline-block re-bedroom']/text())").get()),
                'm2': self.remove_characters(home.xpath("normalize-space(.//div[@class='chiplets-inline-block surface-area']/text())").get()),
                'link': home.xpath("//div[@class='tile-desc one-liner']/a/@href").get()
            }
            
        # next_page = response.xpath("//a[@class='icon-pagination-right']/@href").get()
        # if next_page:
        #     absolute_url = f"https://www.vivanuncios.com.mx/s-venta-inmuebles/queretaro/v1c1097l1021p1{next_page}"
        #     yield SeleniumRequest(
        #         url=absolute_url,
        #         wait_time=3,
        #         callback=self.parse,
        #         dont_filter = True
        #     )