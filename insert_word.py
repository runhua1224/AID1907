import pymysql
import re

f = open("dict.txt")  # 打开文件

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()

# 执行sql语句
sql = "insert into words (word,mean) values (%s,%s)"

for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except:
        db.rollback()
f.close()
# 关闭数据库
cur.close()
db.close()
