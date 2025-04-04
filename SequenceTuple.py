print("\t -- String to Tuple object conversion --\n")
s1 = "Python"
print("Identifier s1 :", s1, "Type :", type(s1), "ID :", id(s1), "Length :", len(s1))
t1 = tuple(s1)
print("Identifier t1 :", t1, "Type :", type(t1), "ID :", id(t1), "Length :", len(t1))
t2 = tuple([s1])            # t2 = (s1,)
print("Identifier t2 :", t2, "Type :", type(t2), "ID :", id(t2), "Length :", len(t2))


print("\n\t -- List to Tuple object conversion --\n")
l = [123, True, "List", 45.67, 98+7654j]
print("Identifier l :", l, "Type :", type(l), "ID :", id(l), "Length :", len(l))
t3 = tuple(l)
print("Identifier t3 :", t3, "Type :", type(t3), "ID :", id(t3), "Length :", len(t3))
t4 = tuple([l])             # t4 = (l,)
print("Identifier t4 :", t4, "Type :", type(t4), "ID :", id(t4), "Length :", len(t4))


print("\n\t -- One Tuple object into another conversion --\n")
t = (123, True, "List", 45.67, 98+7654j)
print("Identifier t :", t, "Type :", type(t), "ID :", id(t), "Length :", len(t))
t5 = tuple(t)
print("Identifier t5 :", t5, "Type :", type(t5), "ID :", id(t5), "Length :", len(t5))
t6 = tuple([t])             # t6 = (t,)
print("Identifier t6 :", t6, "Type :", type(t6), "ID :", id(t6), "Length :", len(t6))


print("\n\t -- Dictionary to Tuple object conversion --\n")
d = {"EmpID": 1002, "EmpName": "Shambhavi Nargide", "Post": "HR Manager", "CTC": 24.67}
print("Identifier d :", d, "Type :", type(d), "ID :", id(d), "Length :", len(d))
t7 = tuple(d)
print("Identifier t7 :", t7, "Type :", type(t7), "ID :", id(t7), "Length :", len(t7))
t8 = tuple([d])             # t8 = (d,)
print("Identifier t8 :", t8, "Type :", type(t8), "ID :", id(t8), "Length :", len(t8))


print("\n\t -- Set to Tuple object conversion --\n")
s = {2, 4, 6, 8, 10}
print("Identifier s :", s, "Type :", type(s), "ID :", id(s), "Length :", len(s))
t9 = tuple(s)
print("Identifier t9 :", t9, "Type :", type(t9), "ID :", id(t9), "Length :", len(t9))
t10 = tuple([s])            # t10 = (s,)
print("Identifier t10 :", t10, "Type :", type(t10), "ID :", id(t10), "Length :", len(t10))
