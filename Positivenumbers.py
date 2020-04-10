list1 =[]
n=int(input("Enter number of elements: "))
for i in range(0, n):
    val=int(input("Enter the number: "))
    list1.append(val)
    
print("Positive numbers in the range are: ")

for i in range(0, n):
    if (list1[i]>0):
        print(list1[i],end=' ')
