#!/usr/bin/env python3

import re
from PIL import Image
import requests
from io import BytesIO

names= [ [re.findall('(?<=href=").*(?=tit)' , str(line))  , re.findall('(?<=—).*(?=<)', str(line))] for line in  open(r'listamedia.html') if ( re.search('(?<=href=").*(?=tit)' , str(line))    and re.search('\d',str(line))) ]

names2=[ [ re.sub(' ','', re.sub('"','',i[0][0].split(sep='/')[2])) ,re.findall('\d+',i[1][0])   ] for i in names ]


# Get url from rest API
url="https://en.wikipedia.org/api/rest_v1/page/summary/"+str(names2[5][0])  
dataj = requests.get(url)
dataj = dataj.json()

# Image 
urlimage=dataj.get('thumbnail').get('source')
responseimage = requests.get(urlimage)
img = Image.open(BytesIO(responseimage.content))
img.show()

#Extract
extract = re.sub('\d', '--' , dataj.get('extract'))

#Title
tit = dataj.get('title')

#Get views

