import scrapy


class GetquotesSpider(scrapy.Spider):
    name = "getquotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        #authors = response.xpath('//small[@class="autjor"]/text()').extract()
        
        quotes = response.xpath('//div[@class="quote"]')
        
        for quote in quotes:
            author = quote.xpath('span/small[@class="author"]/text()').extract_first()
            text = quote.xpath('span[@class="text"]/text()').extract_first()[1:-1]
            tag = quote.xpath('div[@class="tags"]/meta/@content').extract_first()
            
            # option2
            # tag = ",".join(i for i in quote.xpath('div[@class="text"]/a/text()').extract())
            rel_url = quote.xpath('span/a/@href').extract_first()
            abs_url = response.urljoin(rel_url)
            
            
            yield {'Author':author, 'Text':text, 'Tag':tag, 'URL':abs_url}