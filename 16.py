# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:44:33 2020

@author: dk394
"""

dict1={}
n = int(input("輸入筆數n:"))
while(n<=4):  
    for i in range (0,n):
        key = list()
        key1,value = map(str,input().split())
        key.append(key1)
        dict1[key1] = value
    print(dict1)
    #word = str(input("輸入欲查詢單字:"))
    for i in range (0,n):
        k = key[i]
        print(k,"牌得到",dict1[k],"面")
    break