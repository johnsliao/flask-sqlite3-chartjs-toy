import sqlite3

conn = sqlite3.connect('flaskr.db')
c = conn.cursor()

c.execute('insert into entries (week, data1, data2) values (1, 5, 2)')
c.execute('insert into entries (week, data1, data2) values (2, 2, 4)')
c.execute('insert into entries (week, data1, data2) values (3, 9, 6)')
c.execute('insert into entries (week, data1, data2) values (4, 12, 8)')
c.execute('insert into entries (week, data1, data2) values (5, 20, 12)')
c.execute('insert into entries (week, data1, data2) values (6, 17, 18)')

conn.commit()
conn.close()