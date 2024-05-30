num=int(input("enter number:"))
temp=num
rev=0
while(num>0):
    d=num%10
    rev=rev*10+d
    num=num//10
if(temp==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")    