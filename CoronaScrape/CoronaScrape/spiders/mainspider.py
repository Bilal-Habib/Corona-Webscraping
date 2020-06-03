import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://news.google.com/covid19/map?hl=en-GB&gl=GB&ceid=GB%3Aen&mid=%2Fm%2F07ssc'
    ]

    def parse(self, response):
        # for col in response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[1]/table/thead//tr'):
        #     yield  {
        #         'head_1' : col.xpath('th[1]//text()').extract_first(),
        #         'head_2' : col.xpath('th[2]//text()').extract_first(),
        #         'head_3' : col.xpath('th[3]//text()').extract_first(),
        #         'head_4' : col.xpath('th[4]//text()').extract_first(),
        #         'head_5' : col.xpath('th[5]//text()').extract_first(),
        #     }

        for row in response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[1]/table/tbody//tr'):
            yield {
                'Location' : row.xpath('th//text()').extract_first(),
                'Confirmed' : row.xpath('td[1]//text()').extract_first(),
                'Cases per 1 million people' : row.xpath('td[2]//text()').extract_first(),
                'Recovered' : row.xpath('td[3]//text()').extract_first(),
                'Deaths' : row.xpath('td[4]//text()').extract_first(),
            }
