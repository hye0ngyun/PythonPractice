import sqlite3 as s
con = s.connect('c:\\db\\mydb')
c = con.cursor()

c.execute('drop table if exists Man')
c.execute('create table Man(name text, age integer)')
c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 30)')
c.execute('insert into Man values("이강인", 21)')

c.execute('select * from movie order by audience desc')
# c.fetchall(): c.execute()함수에서 select한 값을 리스트 내 튜플로 가져옴
res = c.fetchall()
for i in res:
    print(i[0], i[1], i[2], i[3])

con.commit()
c.close()
con.close()
