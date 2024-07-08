def square_list(n):
    a=[]
    for i in range(1,n+1):
        a.append(i*i)
    print(a)

n=int(input("Enter number:"))
square_list(n)