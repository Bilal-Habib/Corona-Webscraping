import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://news.google.com/covid19/map?hl=en-GB&gl=GB&ceid=GB%3Aen&mid=%2Fm%2F07ssc'
    ]

    def parse(self, response):
        # self.cases_amount = response.xpath(
        #     '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/text()').extract()
        # self.deaths_amount = response.xpath(
        #     '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/text()').extract()
        self.names = []
        for column in range(3, 7):
            for row in range(3, 13):
                self.names[column][row] = response.xpath(
                    '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div[1]/table/tbody/tr[%d]/td[%d]/text()' % (row, column)).extract()

    