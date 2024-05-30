num=int(input("Enter number:"))
per=0
for i in range(1,num):
  if num%i==0:
   per=per+i
if per==num:
  print("number is perfect")
else:
  print("number is not perfect")
   