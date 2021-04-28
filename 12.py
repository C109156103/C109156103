# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:19:45 2020

@author: dk394
"""

dict1={}
n = eval(input("輸入筆數n:"))
for i in range (n):
    key,value = map(str,input().split())
    dict1[key] = value
print(dict1)
word = str(input("輸入欲查詢單字:"))
if word not in dict1 :
    print("字典未有此單字")    
else:
    print(dict1[word])