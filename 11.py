# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:04:46 2020

@author: dk394
"""

m,d = map(int,input("輸入月及日為:").split("/"))

date = m * 100 +d 

if date >= 121 and date <=219:
    print("星座為:Aquarius")
elif date >= 220 and date <= 320:
    print("星座為:Pisces")
elif date >= 421 and date <= 521:
    print("星座為:Aries")
elif date >= 522 and date <= 621:
    print("星座為:Taurus")   
elif date >= 622 and date <= 722:
     print("星座為:Cancer")   
elif date >= 723 and date <= 821:
    print("星座為:Leo")
elif date >= 822 and date <= 923:
    print("星座為:Virgo")
elif date >= 924 and date <= 1023:
    print("星座為:Libra")
elif date >= 1024 and date <= 1122:
    print("星座為:Scorpio")
elif date >= 1123 and date <= 1222:
    print("星座為:Sagittarius")
elif date >= 1223 and date <= 120:
    print("星座為:Capricornus")