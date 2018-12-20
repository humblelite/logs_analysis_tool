import psycopg2


def get_articles():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute(
        'select path, count(*) as num '
        'from log '
        'group by path '
        'order by num desc '
        'limit 3 offset 1')
    db.commit()
    return c.fetchall()
    db.close()


def get_authors():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute(
        'select name, count(*) as num'
        ' from (articles join log on log.path like concat("/article/", articles.slug))as slugger'
        ' join authors on slugger.author = authors.id'
        ' group by authors.name '
        'order by num desc')
    db.commit()
    return c.fetchall()
    db.close()


def get_percent():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute(
        'select requestdates, percent || "% errors" as percenterror'
        ' from(select coalesce(alljoin.alldate, errorjoin.errordate) as requestdates, '
        'round(cast(errorjoin.errorcount / alljoin.allcount * 100 as numeric), 1)  as percent '
        'from (select to_char(time, "monthDD,YYYY") as alldate, count(*)::float as allcount from log '
        'group by alldate)alljoin'
        ' full join(select to_char(time, "monthDD,YYYY") as errordate, count(*)::float as errorcount from log'
        ' where status = "404 NOT FOUND" '
        'group by errordate)errorjoin on alljoin.alldate = errorjoin.errordate) as percentage'
        ' where percent > 1')
    db.commit()
    return c.fetchall()
    db.close()
