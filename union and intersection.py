def st (s1,s2):
     s=s1.split(" ")
     ss=s2.split(" ")
     #print(s)
     #print(ss)
     print("union=",set(s)^set(ss))
     print("Intersection=",set(s)&set(ss))

s1=input("Enter string 1:")
s2=input("Enter string 2:")

st(s1,s2)

