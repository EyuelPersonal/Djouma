import requests
import datetime
import base64
import constants
import DBuse
import random

constants.__init__()

url = constants.URL
user = constants.WPNAME
password = constants.WPPASS
date = datetime.datetime.now()

news = DBuse.get_news()

def post(url, user, password, date, title, post):
 credentials = user + ':' + password
 token = base64.b64encode(credentials.encode())
 header = {'Authorization': 'Basic ' + token.decode('utf-8')}
 post = {
  'title'    : '{}'.format(title),
  'status'   : 'publish',
  'content'  : '{}'.format(post),
  'categories': 5,
  'featured_media': [78,11,38][random.randint(0,2)],
  'date_gtm'   : str(date)

 }
 responce = requests.post(url , headers=header, json=post)
 print(responce)

def poster(url, user, password, date, news):
 for key in news.keys():
  print(str(key)+":"+news[key])
  post(url, user, password, date, key, news[key])


if __name__ == '__main__':
 poster(url, user, password, date, news)



