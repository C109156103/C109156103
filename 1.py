x=int(input("X 軸座標: "))
y=int(input("Y 軸座標: "))

r=x**2+y**2

if x==0 and y==0:
    print("該點位於原點",end="")
if x==0 and y>0:
    print("該點位上半平面Y軸上",end="")
if x==0 and y<0:
    print("該點位下半平面Y軸上",end="")
if x>0 and y==0:
    print("該點位右半平面X軸上",end="")
if x<0 and y==0:
    print("該點位左半平面X軸上",end="") 

if x >0 and y>0:
    print("該點位於第一象限",end="")
if x <0 and y>0:
    print("該點位於第二象限",end="")
if x <0 and y<0:
    print("該點位於第三象限",end="")
if x >0 and y<0:
    print("該點位於第四象限",end="")

if r!=0:
    print("，離原點距離為根號"+str(r))
