rows=int(input("Enter number of rows: "))

#Create an empty list
list=[]

#Create the sub lists
for i in range (rows) :
    list.append([])
    list[i].append(1)

    #Calculate the value using the 2 numbers above it (sum)
    for j in range (1,i) :
        list[i].append(list[i-1][j-1]+list[i-1][j])
    if rows != 0 :
        list[i].append(1)

#Print the final Pascal Triangle
for i in range(rows):
    print("   "*(rows-i),end=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(list[i][j]),end=" ")
    print("\n")