def power(x,y):
    a=1
    for i in range(1,y+1):
        a=x*a
        print("power of x of y:",a)
x=int(input("Enter X:"))
y=int(input("Enter y:"))

power(x,y)