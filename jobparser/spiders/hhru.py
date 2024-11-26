import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?text=python&area=1&hhtmFrom=main&hhtmFromLabel=vacancy_search_line"]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        print()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//span[@data-qa="serp-item__title-text"]/ancestor::a/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath('//div[@class="bloko-columns-row"]//h1//text()').get()
        salary = response.xpath('//div[@data-qa="vacancy-salary"]//text()').getall()
        _id = response.xpath('//link[@rel="canonical"]').get()
        url = response.url
        print()
        yield JobparserItem(name=name, salary=salary, url=url, _id=_id)
        # print()
