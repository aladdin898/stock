#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: sakura9 (wanwei6660@gmail.com)
# Description: fetch historical data from yahoo's interface. (http://www.predream.org/show-58-320-1.html)

import sys
import urllib2
import datetime
sys.path.append("../config")
from api_get_db import *

today = datetime.date.today() #获得今天的日期
stock_id="300093"

################################ 获取数据 ########################################
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
listurl = "http://ichart.yahoo.com/table.csv?s=300093.sz&a=11&b=01&c=2014&d=%s&e=%s&f=%s&g=d"%('01', 28, 2015)
print listurl
req = urllib2.Request(url=listurl, headers=headers)
fd = urllib2.urlopen(req)
serverlist = fd.readlines()

################################ 插入数据库 ######################################
db, cursor = get_cursor()
records = []
for line in serverlist:
    if "Date" in line:
        continue
    if int(line.strip().split(',')[5]) == 0:
        continue
    records.append([stock_id] + [a.replace('-', '') for a in line.strip().split(',')])
print records
query = "insert IGNORE into src_price_day values(%s, %s, %s, %s, %s, %s, %s, %s)"
insert_many(cursor, db, query, records)            
print "%s Rows loaded to %s"%(str(len(records)), "src_price_day")
