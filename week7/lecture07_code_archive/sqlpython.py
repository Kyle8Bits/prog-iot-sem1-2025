import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='abc@123$',
    database='People'
)

cursor = conn.cursor()
print(cursor)

cursor.execute('DROP TABLE IF EXISTS user')
sql = """CREATE TABLE IF NOT EXISTS user (
           id INT(11) NOT NULL AUTO_INCREMENT,
           name VARCHAR(255) NOT NULL,
           age INT(11) NOT NULL,
           PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cursor.execute(sql)
cursor.close()
conn.close()
print('succeed')
