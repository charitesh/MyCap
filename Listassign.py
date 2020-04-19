#assigning elements to different lists

#creating 2 different lists
listassign1 = []
listassign2 = []

#assigning elements to list 1
n=int(input("Enter number of elements for list 1: "))
print("Enter elements for list 1")
for i in range(0, n):
    val1=input("Enter elements: ")
    listassign1.append(val1)
    
#output elements of list 1
    
print("Elements in list 1: ")
for i in range (0, n):
    print(" ", end=(listassign1[i]))

    
#assigning elements to list 2
m=int(input("Enter number of elements for list 2: "))
print("Enter elements for list 2")
for j in range(0, m):
    val2=input("Enter element: ")
    listassign2.append(val2)
    
#output elements of list 2
    
print("Elements in list 2: ")
for j in range(0, m):
    print(" ", end=(listassign2[j]))
