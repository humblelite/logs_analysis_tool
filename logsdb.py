import psycopg2



def get_articles ():
    db = psycopg2.connect(dbname = 'news')
    c = db.cursor()
    c.execute('select path, count(*) as num from log group by path order by num desc limit 3 offset 1')
    db.commit()
    return c.fetchall()
    db.close()

