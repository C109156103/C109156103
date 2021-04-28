# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:47:49 2020

@author: dk394
"""

d1={}
for i in range(3):
    s1=input("請輸入姓名")
    s2=input("請輸入電子郵件")
    d1[s1]=s2
s3=input("請輸入要查詢的電子郵件姓名")
print(d1[s3])