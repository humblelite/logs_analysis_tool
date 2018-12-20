#!/usr/bin/env python3
import psycopg2


# gets the top three articles from the log table removes /articles/ path
# and appends "-views" to the end of the number count.
def get_articles():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute('select substring(path,10) as popular, num || \'-views\' '
              'from(select path, count(*) as num from log group by path) as newquery '
              'order by num desc '
              'limit 3 offset 1')
    db.commit()
    rows = c.fetchall()
    print('\n')
    print('Most popular 3 articles of all times.')
    for row in rows:
        print(row)
    print('\n')
    db.close()


# gets the most popular article authors and appends "-views" to end of number count.
def get_authors():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute('select name, num || \'-views\''
              ' from (select name, count(*) as num '
              'from (articles join log on log.path like concat(\'/article/\', articles.slug))as slugger '
              'join authors on slugger.author = authors.id '
              'group by authors.name '
              'order by num desc) as newquery')
    db.commit()
    rows = c.fetchall()
    print('\n')
    print('Most popular article authors of all times.')
    for row in rows:
        print(row)
    print('\n')
    db.close()


# gets the dates where the request errors percentage where greater then 1
# by  dividing 404 not found request by 202 ok request and multipliying by 100 for each day
# and appends "%error" to end of percentage
def get_percent():
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute(
        'select requestdates, percent || \'% errors\' as percenterror'
        ' from(select coalesce(alljoin.alldate, errorjoin.errordate) as requestdates, '
        'round(cast(errorjoin.errorcount / alljoin.allcount * 100 as numeric), 1)  as percent '
        'from (select to_char(time, \'monthDD,YYYY\') as alldate, count(*)::float as allcount from log '
        'group by alldate)alljoin'
        ' full join(select to_char(time, \'monthDD,YYYY\') as errordate, count(*)::float as errorcount from log'
        ' where status = \'404 NOT FOUND\' '
        'group by errordate)errorjoin on alljoin.alldate = errorjoin.errordate) as percentage'
        ' where percent > 1')
    db.commit()
    rows = c.fetchall()
    print('\n')
    print("Days where more than 1 percent of request lead to errors.")
    for row in rows:
        print(row)
    print('\n')
    db.close()


if __name__ == '__main__':
    get_articles(), get_authors(), get_percent()
