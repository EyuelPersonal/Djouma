import requests
import datetime
import base64
import constants
import DBuse
from bs4 import BeautifulSoup

import json

constants.__init__()

class images():

 def __init__(self):
  self.url_image = constants.URL_IMAGES
  self.user = constants.WPNAME
  self.password = constants.WPPASS
  self.date = datetime.datetime.now()

 def upload_image(self, image, news_id):
  credentials = self.user + ':' + self.password
  token = base64.b64encode(credentials.encode())
  header = {'Authorization': 'Basic '+token.decode('utf-8')}
  media = {'file':image}

  responce = requests.post(self.url_image, headers = header,  files = media)
  print(responce.content.decode('utf-8'))

  id = json.loads(responce.content.decode('utf-8'))['id']
  link = json.loads(responce.content.decode('utf-8'))['link']

  DBuse.add_image(news_id, link, id)

 def download_image(self, news_id):
  page_link = DBuse.get_image(news_id)
  links  = None
  for i in page_link.keys():
   links = page_link[i]

  html = requests.get(links).content
  soup = BeautifulSoup(html)
  images = soup.findAll('p',{'class':'attachment'})[0]
  soup_2 = BeautifulSoup(str(images))

  image_link = None
  for a in soup_2.findAll('a',href = True):
   image_link = a['href']


  print(image_link)
  image_file = requests.get(image_link).content


  return image_file