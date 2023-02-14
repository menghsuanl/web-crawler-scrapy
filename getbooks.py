import scrapy
from scrapy import Request 

class GetbooksSpider(scrapy.Spider):
    name = "getbooks"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        """
        Parse the information on the catalog page and then call parse_page function to parse info inside the detail pages of 
        every books
        """
        books = response.xpath('//div/ol[@class="row"]/li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]')
        
        for book in books:
            title = book.xpath('article[@class="product_pod"]/h3/a/text()').extract_first()
            price = book.xpath('article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()[1:]
            star = book.xpath('article[@class="product_pod"]/p/@class').extract_first()[12:]
            rel_url = book.xpath('article[@class="product_pod"]/h3/a/@href').extract_first()
            abs_url = response.urljoin(rel_url)
            # click into the inner page of the book: abs_url
            yield Request(abs_url, callback=self.parse_page, dont_filter=True,
                    #store in meta, make it globally available across functions
                meta={'Title': title, 'Price': price, 'Star': star, 'URL': abs_url})
        # go to the next page
        rel_next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        abs_next_url = response.urljoin(rel_next_url)
        yield Request(abs_next_url, callback = self.parse)
        
    def parse_page(self, response):
        """
        Parse the stock and desc in the bool detail page
        :return: dict, six attribute of each book
        """
        title = response.meta.get('Title')
        price = response.meta.get('Price')
        star = response.meta.get('Star')
        abs_url = response.meta.get('URL')
        stock = response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()').extract()[1].strip()
        desc = response.xpath('//article[@class="product_page"]/p/text()').extract_first()
        
        yield {'Title': title,'Price': price, 'Star': star, 'URL': abs_url, 'Stock': stock, 'Description':desc}
        
