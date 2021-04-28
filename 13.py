nu=int(input(""))

summer=0
nsummer=0

if nu<=120:
    summer+=nu*2.10
    nsummer+=nu*2.10

if 121<= nu <=330:
    nu=nu-120
    summer+=nu*3.02+252
    nsummer+=nu*2.68+252

if 331<= nu <=500:
    nu=nu-330
    summer+=nu*4.39+886.2
    nsummer+=nu*3.61+814.8

if 501<= nu <=700:
    nu=nu-500
    summer+=nu*4.97+1632.5
    nsummer+=nu*4.01+1428.5

if nu>700:
    nu=nu-700
    summer+=nu*5.63+2626.5
    nsummer+=nu*4.5+2230.5
    
print("Summer months:"+str(summer))
print("Non-Summer months:"+str(nsummer))
