li=["tiger","rabbit","dagon","snake","hoser","sheep","monkey","rooster","pig",
    "rat","ox"]
nu=int(input(""))
if nu-2010>0:
    print(li[(nu-2010)%12])
else:
    
    print(li[-(abs(nu-2010)%12)])
