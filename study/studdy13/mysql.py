#pip install PyMySQL
import pymysql
db = pymysql.connect("localhost","root","123456","mysql",port=3306)
cursor = db.cursor()
cursor.execute("select * from user")
# cursor.execute("use study")
# cursor.execute("""
#     CREATE TABLE people2(
#     id INT,
#     name VARCHAR(300)
# )
# """)
print(cursor.description)

while True:
    data = cursor.fetchone();
    if not data:
        break
    print(data)
db.close()
print(pymysql.apilevel)
print(pymysql.threadsafety)
print(pymysql.paramstyle)