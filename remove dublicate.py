dic={"rno":11,"name":"sai","per":21,"age":21}
if (dic["rno"]==dic["name"] or dic["per"]==dic["age"]):
    p=dic.popitem()
    print(p)  
    print(dic)

dic={"rno":10,"per":21,"age":10}
if(dic["rno"]==dic["per"] or dic["per"]==dic["age"] or dic["rno"]==dic["age"]):
         p=dic.popitem()
         print(p)  
         print(dic)