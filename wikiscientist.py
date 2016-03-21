#!/usr/bin/python3

import wikipedia
import re
startlist=[]
names=[ [line.split(sep='—')[0], re.findall('\d+', line)  ] for line in  open(r'listaplain.txt')]
random.randint(0,len(names))




