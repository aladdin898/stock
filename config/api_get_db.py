#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: WanWei
# Description: 获取的数据库连接

import sys
import MySQLdb

# 获取数据库连接
def get_cursor():    
    db = MySQLdb.connect("ip", "user", "passwd", "database")
    cursor = db.cursor()
    return db, cursor

# 查询数据
def get_db(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# 批量插入
def insert_many(cursor, db, query, records):
    cursor.executemany(query, records)
    db.commit()

if __name__ == "__main__":  
    db, cursor = get_cursor()
    result = get_db(cursor, 'select * from src_price_day')
    print result
