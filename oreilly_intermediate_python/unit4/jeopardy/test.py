#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:22:08 2016

@author: ilyarudyak
"""

import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()
sql_request = 'SELECT name FROM category LIMIT 10'
cursor.execute(sql_request)
results = cursor.fetchall()
connection.close()

[print(category[0]) for category in results]