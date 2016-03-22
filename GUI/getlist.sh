#!/usr/bin/env bash
#wget https://en.wikipedia.org/wiki/List_of_physicists
mv List_of_physicists List_of_physicists.html
grep "—" List_of_physicists.html > listamedia.html
pandoc  listamedia.html -t plain -o listaplain.txt
#TO get the wikipedia page
listawiki=$(grep -o -P '(?<=href=").*(?=tit)' listamedia.html | cut -d '/' -f3 | tr -d '"')
#Create lista with views:
#from  https://gist.github.com/dannguyen/f415b1797f686f995f8e
for i in $listawiki
do 
#Data for October 2015
    RESPONSE=$(curl -s https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/$i/daily/2015100100/2015103100)
    VALS=$(jq '.items[] | .views' <<< $RESPONSE | tr '\n' ',')
    MAXVAL=$(jq '.items[] | .views' <<< $RESPONSE | sort -rn | head -n1) 
    echo $i $MAXVAL >> listavistas.txt
    echo aaa
done

#TO do do it with 
curl -X GET --header 'Accept: application/json' 'https://en.wikipedia.org/api/rest_v1/page/summary/Benjamin_Lee_(physicist)'

#This gives you the extact and also title



