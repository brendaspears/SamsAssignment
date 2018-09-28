initialVelocity = 0
speedLimit = 60
timeSpent = int(input("Time Spent on the Road = "))
acceleration = int(input("Acceleration = "))
distance = int(input("Distance =  "))
u = initialVelocity
a = acceleration
t = timeSpent
v = u + ( a * t )
for i in range ( timeSpent + 1 ):
    s = (1/2) * a * ((i)**2)
    noOfStar = s // 5
    print ("Duration : ",i," Distance : ",end="")
    for j in range ( int(noOfStar)):
        print("*",end="")
    print ("\n")
if v > 60:
    print ("The person went over the speed limit. ( Max speed was " , v , " m/s )")
else:
    print ("The person did not go over the speed limit. ( Max speed was ", v , " m/s )" )
s = (1/2) * a * (t**2)
if s <= distance :
    print ("The person reached the destination. ( Reached ", s ," m/s)" )
else:
    print ("The person did not reach the destination. ( Reached ",s," m/s )")