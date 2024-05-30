n=int(input("Enter number:"))
s=0
d=0
for i in range(1,n):
    d=int(n)%10
    s=s+i**i
    n=n//10
    
if n==s:
    print("number is armstrong")
else:
    print("number is not armstrong")