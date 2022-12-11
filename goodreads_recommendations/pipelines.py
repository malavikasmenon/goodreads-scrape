# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class GoodreadsRecommendationsPipeline:
    def __init__(self):
        self.csv_file = 'book_recos.csv'
        self.field_names = ['title', 'author', 'category']

    def process_item(self, item, spider):
        with open(self.csv_file, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=self.field_names)
            writer.writerow(item)