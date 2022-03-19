from pinotdb import connect
conn = connect(host='localhost', port=8099, path='/query/sql', scheme='http')
curs = conn.cursor()

curs.execute("select * from wikievents limit 10")

for row in curs:
    print(row)
