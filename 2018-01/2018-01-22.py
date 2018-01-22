'''
远程操作mongodb

http://api.mongodb.com/python/current/installation.html   安装mogodb 网址
http://api.mongodb.com/python/current/tutorial.html       mogodb教程网址

'''

from pymongo import MongoClient

client = MongoClient('mongodb://118.31.19.120:27017/')     # 连接数据库
print(client.database_names())   # 打印出数据库为：['node_club_dev', 'local']

db = client.get_database('node_club_dev')

'''
打印出 node_club_dev数据库中的表，
表为：['messages', 'replies', 'system.indexes', 'topiccollects', 'topics', 'users']
'''
collections = db.collection_names()
print(collections)

# users表
users = db.get_collection('users')


# http://118.31.19.120:3000/signin 登录testuser ,更新active项
users.find_one_and_update({"loginname":"testuser"},{'$set':{"active":True}})
