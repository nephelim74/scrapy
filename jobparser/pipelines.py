# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from customs import parse_salary_re

class JobparserPipeline:

    def __init__(self):
        client = MongoClient(host ='localhost', port=27017)
        self.mongo_base = client.vacancies241126_3
    def process_item(self, item, spider):
        print()
        # item.get('salary')
        # item['min_salary'] = item.get('salary')[1]
        # item['max_salary'] = item.get('salary')[3]
        print()
        item['salary'] = parse_salary_re(item.get('salary'))
        print()
        match = re.search(r'/vacancy/(\d+)', item.get('_id'))
        if match:
            item['_id'] = int(match.group(1))
        print()
        collections = self.mongo_base[spider.name]
        collections.insert_one(item)

        return item
