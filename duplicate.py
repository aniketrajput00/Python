
n=[22,11,44]
flag=0
for i in range (0,len(n)):
      if n[i] not in n[i+1:]:
        i+1
      else:
        flag=1


if flag==1:
    print("DUPLICATES") 
else:
    print("ALL UNIQUES")    

        