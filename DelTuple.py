t1 = (True , "true ", 123.456 , 123+456j,"123.456")
print("identifier t1 :" , t1 ,"type :", type(t1),"id:" , id(t1) , "length:" , len(t1))
t2 = ( 2, 4 , 'a',6 ,'e', 8 , 'i', 10)
print("identifier t2:" , t2 ,"type :", type(t2),"id:" , id(t2) , "length:" , len(t2))
del t1
print("identifier t1 :" , t1 ,"type :", type(t1),"id:" , id(t1) , "length:" , len(t1))
del t2
print("identifier t2:" , t2 ,"type :", type(t2),"id:" , id(t2) , "length:" , len(t2))
      
