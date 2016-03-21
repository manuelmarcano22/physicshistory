#!/usr/bin/python3

import re
import wikipedia
import random
import numpy as np
startnames=[]
score=0.
names=[ [line.split(sep='—')[0], re.findall('\d+', line)  ] for line in  open(r'listaplain.txt')]

numberoftries=3
maxfame=100
num=random.randint(0,maxfame)

cont=True
while cont:
    num=random.randint(0,maxfame)
    startnames.append(names[num])
#    print(str(startnames[0][0])+'was born on: '+ str(startnames[0][1][0]))
    for i in range(1,numberoftries): 
        num=random.randint(0,maxfame)
        startnames.append(names[num])
        print(str(startnames[i-1][0])+'was born on '+ str(startnames[i-1][1][0]))
        agedif = float(startnames[i][1][0]) - float(startnames[i-1][1][0])  
        print('Was '+str(startnames[i][0])+"born before, after or the same year as "+str(startnames[i-1][0])+'?')
        conti=False
        while conti==False:
            inputkey = input('Press h for a hint, a for after, b for before and s for same year:\n')
            if str(inputkey) == 'h':
                hint=wikipedia.summary(str(startnames[i][0])+'Physics', sentences=1)
                print(re.sub('\d', '---', hint))
            elif str(inputkey) == 'b':
                conti=True
                if np.sign(agedif) == -1:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+'was born on '+str(startnames[i][1][0])+'\n')

            elif str(inputkey) == 'a':
                conti=True
                if np.sign(agedif) == 1:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+'was born on '+str(startnames[i][1][0])+'\n')

            elif str(inputkey) == 's':
                conti=True
                if np.sign(agedif) == 0:
                    print('Great job!\n')
                    score+=1
                else:
                    print('Sorry. Wrong answer. '+\
                            str(startnames[i][0])+'was born on '+str(startnames[i][1][0])+'\n')
            else:
                print('Please insert a valid character.')
    cont=False
    print('total score is '+str(int(np.sum(score)))+' out of '+ str(int(len(startnames)-1)) +' tries')




