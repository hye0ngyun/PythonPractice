import sqlite3 as s
con = s.connect('c:\\db\\adb')
c = con.cursor()

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu, price)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')
c.execute('select * from score')
c.execute('delete from score where name = "김정호"')
c.execute('delete from score where name = "임꺽정"')

c.execute('drop table if exists ex_data')
c.execute('create table ex_data(int"id", string"name")')
c.execute('insert into ex_data values(1, "Kim")')
c.execute('delete from ex_data where int = 1')

c.execute('select * from lunch')
res = c.fetchall()

for i in res:
    print(i[0][1])
print(res)
con.commit()
c.close()
con.close()