s = "string"
i = 123
f = 3.14
b = True
c= 12.34
t1 =( s, i ,f , b ,c)
print("identifier :", t1 ,"type:" , type(t1) ,"id" , id(t1),"length:" , len(t1))
t2 = tuple([s, i ,f , b ,c])
print("identifier :", t2 ,"type:" , type(t2) ,"id" , id(t2),"length:" , len(t2))
t3 = tuple((s, i ,f , b ,c))
print("identifier :", t3,"type:" , type(t3) ,"id" , id(t3),"length:" , len(t3))
t4 = tuple(t3)
print("identifier :", t4 ,"type:" , type(t4) ,"id" , id(t4),"length:" , len(t4))
