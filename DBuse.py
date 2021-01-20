import datetime
from DBhandler import *

def add_news(news_id, user_id, username,news):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO djouma.news_db(news_id,user_id,user_name,news_date,news) VALUES(%s,%s,%s,%s,%s)",(news_id,user_id,username, now ,news))
    mydb.commit()

def delete_news(user_id):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    today =  datetime.datetime.now().date()
    cursor.execute("DELETE FROM djouma.news_db WHERE user_id = {} and news_date = curdate()".format(user_id))
    mydb.commit()

def get_news():
    news = {}
    today = datetime.datetime.now().date
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute(" select distinct user_name, news from news_db where news_date > curdate()-1".format(today))
    results = cursor.fetchall()
    for r in results:
        news[str(r[0])] = str(r[1])
    return news