# coding=utf-8

import time
import json

from bson import ObjectId
import pymysql
from pymongo import MongoClient
from kafka.producer import KafkaProducer
from wsp.utils.parse import text_from_http_body


class StoreMiddleware:

    match_url = "ieeexplore.ieee.org:80/xpl"
    mongo_addr = "mongodb://wsp:wsp123456@192.168.120.90:27017"
    mongo_db = "ScholarInfoBase"
    mongo_collection = "ieee"
    mysql_host = "192.168.120.90"
    mysql_user = "root"
    mysql_pwd = "123456"
    kafka_addr = "192.168.120.90:9092"
    kafka_topic = "ieee"
    not_found_feature = "<h1>Page Not Found</h1>"

    def __init__(self):
        self._mongo_client = MongoClient(self.mongo_addr)
        self._coll = self._mongo_client[self.mongo_db][self.mongo_collection]
        self._conn = pymysql.connect(host=self.mysql_host,
                                     user=self.mysql_user,
                                     password=self.mysql_pwd,
                                     db="ScholarInfoBase")
        self._cur = self._conn.cursor()
        self._producer = KafkaProducer(bootstrap_servers=[self.kafka_addr, ])

    async def handle_input(self, response):
        # print("%s Response url: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), response.url))
        if response.url.find(self.match_url) >= 0:
            self._store(response)

    def _store(self, response):
        url = response.request.url
        obj_id = ObjectId()
        sql = "insert into `IEEEMetaSource` (ID, detailPageId, detailPageUrl, crawlTime) values (%s, %s, %s, %s)"
        page_id = "%s" % obj_id
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            eq = url.rindex("=")
            id = url[eq + 1:]
        except Exception:
            pass
        else:
            html = text_from_http_body(response)
            if html.find(self.not_found_feature) >= 0:
                return
            self._cur.execute(sql, (id, page_id, url, t))
            self._coll.insert_one({"_id": obj_id, "url": url, "body": response.body})
            data_dict = {"id": id, "crawl_time": t, "html": html}
            self._producer.send(self.kafka_topic, json.dumps(data_dict).encode("utf-8"))
