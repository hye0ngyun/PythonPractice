import pymysql as my
con = my.connect(host='127.0.0.1', user='root', password='1234', db='bdb')
c = con.cursor()

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu char(10), price int)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')
c.execute('select * from score')

# c.execute('drop table if exists ex_data')
# c.execute('create table ex_data(int"id", string"name")')
# c.execute('insert into ex_data values(1, "Kim")')
# c.execute('delete from ex_data where int = 1')

c.execute('select * from lunch')
res = c.fetchall()

for i in res:
    print(i[0], i[1])
print(res)
con.commit()
c.close()
con.close()