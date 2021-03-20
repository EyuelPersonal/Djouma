import requests
import datetime
import base64
import constants
import DBuse
from io import BytesIO

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

  id = responce.content.decode('utf-8')['id']
  link = responce.content.decode('utf-8')['link']

  DBuse.add_image(news_id, link, id)

 def download_image(self, news_id):
  image_link = DBuse.get_image(news_id)
  image = BytesIO(requests.get(image_link))
  return image