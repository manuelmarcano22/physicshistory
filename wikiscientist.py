#!/usr/bin/python3

import re
import subprocess
import random
import numpy as np
from PIL import Image
import requests
from io import BytesIO

startnames=[]
score=0.

names= [ [re.findall('(?<=href=").*(?=tit)' , str(line))  , re.findall('(?<=—).*(?=<)', str(line))] for line in  open(r'listamedia.html') if ( re.search('(?<=href=").*(?=tit)' , str(line))    and re.search('\d',str(line))) ]
names2=[ [ re.sub(' ','', re.sub('"','',i[0][0].split(sep='/')[2])) ,re.findall('\d+',i[1][0])   ] for i in names ]

numberoftries=5

limitedy = False
centuary=len(names2)

years = input('Define the years separated by space or write all.  \n')

year1=years.split(sep=' ')[0]
if year1.isdigit():
    limitedy = True
    year2 = years.split(sep=' ')[1]
    cent=[i[1][0]   for i in names2]
    cent= np.array(cent, dtype=int)
    centmask = np.where(np.logical_and(cent > int(year1), cent <  int(year2)))


cont=True
while cont:
    if limitedy == False:
        num=random.randint(0,centuary)
    else:
        num=np.random.choice(centmask[0])
    # Get url from rest API
    url="https://en.wikipedia.org/api/rest_v1/page/summary/"+str(names2[num][0])  
    dataj = requests.get(url)
    dataj = dataj.json()
    #Title
    tit = dataj.get('title')
    startnames.append([tit,names2[num][1][0] ])
    for i in range(1,numberoftries):
        if limitedy == False:
            num=random.randint(0,centuary)
        else:
            num=np.random.choice(centmask[0])
        # Get url from rest API
        url="https://en.wikipedia.org/api/rest_v1/page/summary/"+str(names2[num][0])  
        dataj = requests.get(url)
        dataj = dataj.json()
        #Title
        tit = dataj.get('title')
        startnames.append([tit,names2[num][1][0]]  )
        print(str(startnames[i-1][0])+' was born on '+ str(startnames[i-1][1]))
        agedif = float(startnames[i][1]) - float(startnames[i-1][1])  
        print('Was '+str(startnames[i][0])+" born before, after or the same year as "+str(startnames[i-1][0])+'?')
        conti=False
        while conti==False:
            inputkey = input('Press h for a hint, hi for an image,  a for after, b for before and s for same year:\n')
            if str(inputkey).startswith('h'):
                #Extract
                extract = re.sub('\d', '--' , dataj.get('extract'))
                print(extract)
                if len(str(inputkey)) >= 2:
                    # Image 
                    try:
                        urlimage=dataj.get('thumbnail').get('source')
                        responseimage = requests.get(urlimage)
                        img = Image.open(BytesIO(responseimage.content))
                        img.show()
                    except:
                        print('\n Oops! No photos available\n')
            elif str(inputkey) == 'b':
                conti=True
                if np.sign(agedif) == -1:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+' was born on '+str(startnames[i][1])+'\n')

            elif str(inputkey) == 'a':
                conti=True
                if np.sign(agedif) == 1:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+' was born on '+str(startnames[i][1])+'\n')

            elif str(inputkey) == 's':
                conti=True
                if np.sign(agedif) == 0:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+' was born on '+str(startnames[i][1])+'\n')
            else:
                print('Please insert a valid character.')
    cont=False
    print('total score is '+str(int(np.sum(score)))+' out of '+ str(int(len(startnames)-1)) +' tries')


