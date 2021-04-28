# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:48:03 2020

@author: dk394
"""

s1=set("紅豆生南國，春來發幾枝?願君多采擷，此物最相思。")
s2=set("春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。")
if "，"or"。"or"?"in s1:
    s1.remove("，")
    s1.remove("。")
    s1.remove("?")
if "，"or"。"in s2:
    s2.remove("，")
    s2.remove("。")
print(s1&s2)