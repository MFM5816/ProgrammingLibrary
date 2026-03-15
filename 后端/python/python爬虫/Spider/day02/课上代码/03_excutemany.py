import pymysql

db = pymysql.connect(
    'localhost','root','123456','maoyandb',
    charset='utf8'
)
cursor = db.cursor()
ins = 'insert into filmtab values(%s,%s,%s)'
r_list = [
    ('大话西游之大圣娶亲','周星驰','1994'),
    ('大话西游之月光宝盒','周星驰','1995')
]
cursor.executemany(ins,r_list)
db.commit()



























