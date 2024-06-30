List=input("Enter String:")
print("Alternate characters forword direction:",end=" ")
for i in range(0,len(List),2):
    print(List[i],end=" ")

print("\n Alternate characters backword direction:",end=" ")
for i in range(len(List)-1,0,-2):
    print(List[i],end=" ")   