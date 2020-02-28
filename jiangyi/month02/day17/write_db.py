import  pymysql

#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database= 'student',
                   charset='utf8')

#创建游标(操作数据 执行sql语句，获取结果)
cur=db.cursor()

#执行各种数据操作
try:
    # sql="insert into cls values (6,'Joy',13,'m',84);"
    # cur.execute(sql)
    sql="update cls set score=%s where name=%s;"
    cur.execute(sql,[85,'Joy'])
    db.commit()
except:
    db.rollback()


#关闭游标和数据库
cur.close()
db.close()