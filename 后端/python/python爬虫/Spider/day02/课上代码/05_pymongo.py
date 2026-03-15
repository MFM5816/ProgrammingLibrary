'''testdb - mytab - {'name':'Lucy'}'''
import pymongo

# 连接对象
conn = pymongo.MongoClient('localhost',27017)
# 库对象
db = conn['testdb']
# 集合对象
myset = db['mytab']

myset.insert_one({'name':'Lucy'})











