def uppercase_lowercase(s):
    uc=0
    lc=0
    for ch in s:
        if ch>='A' and ch<='Z':
            uc=uc+1
        else:
            lc=lc+1

        if ch==" ":
          lc=lc-1
          
    print("Uppercase=",uc)
    print("Lowercase=",lc)        

s=input("Enter String:")
uppercase_lowercase(s)