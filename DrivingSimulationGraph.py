import matplotlib.pyplot as plt
initialVelocity = 0
speedLimit = 60
timeSpent = float(input("Time Spent on the Road = "))
acceleration = float(input("Acceleration = "))
distance = float(input("Distance =  "))
u = initialVelocity
a = acceleration
t = timeSpent
v = u + ( a * t )
x=[]
y=[]
for i in range ( int(timeSpent) ):
    s = (1/2) * a * ((i)**2)
    noOfStar = s // 5
    print ("Duration : ",i," Distance : ",end="")
    for j in range ( int(noOfStar)):
        print("*",end="")
    print ("\n")
    x.append(i)
    y.append(s)
plt.plot(x,y)
plt.show()