# encoding=utf-8
import pymongo
#客户端对象
client = pymongo.MongoClient('localhost')
#连接名叫‘huo’数据库
db = client['huo']
#获取名为‘ta0’的表,并插入一条信息
db['ta0'].insert({"name":"huodongge"})
