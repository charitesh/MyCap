print("Fibonacci Series")
a=0
b=1
n=int(input("Enter the numbmer of terms:"))
print(b)
for i in range(1, n):
    c=a+b
    print(c)
    a=b
    b=c
