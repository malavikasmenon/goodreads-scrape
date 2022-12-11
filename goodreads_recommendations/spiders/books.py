import scrapy
from scrapy.loader import ItemLoader

from ..items import GoodreadsRecommendationsItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/choiceawards/best-fiction-books-2022']

    def parse(self, response):
        category = response.css('div.gcaMastheader::text').get()
        books = response.css('div.answerWrapper')
        for book in books:
            l = ItemLoader(item=GoodreadsRecommendationsItem(), selector=book)
            book_name = book.css('img::attr(alt)').get().split('by')
            l.add_value('title', book_name[0])
            l.add_value('author', book_name[1])
            l.add_value('category', category)
            yield l.load_item()
