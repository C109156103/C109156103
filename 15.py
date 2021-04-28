target=int(input("輸入階層值M : "))
n=1
stap=1
while(True):
    if target<n*stap:
        break
    else:
        stap=n*stap
        n+=1
print(n)
