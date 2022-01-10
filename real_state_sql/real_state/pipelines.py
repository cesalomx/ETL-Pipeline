# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
    
class SQLlitePipeline(object):
       
    def open_spider(self, spider):
        self.connection = sqlite3.connect('homes.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                        CREATE TABLE QRO_HOMES(
                            price TEXT,
                            location TEXT,
                            description TEXT,
                            bathrooms TEXT,
                            bedrooms TEXT,
                            meters TEXT,
                            link TEXT
                        )
                        ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
        
    def close_spider(self,spider):
        self.connection.close()
        
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO QRO_HOMES (price,location,description,bathrooms,bedrooms,meters,link) VALUES(?,?,?,?,?,?,?)
                       ''',(
            item.get('price'),
            item.get('location'),
            item.get('description'),
            item.get('bathrooms'),
            item.get('bedrooms'),
            item.get('meters'),
            item.get('link'),
        ))
        self.connection.commit()
        return item   
