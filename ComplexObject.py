i1 = 24
print("Identifier i1 :", i1, "Type :", type(i1), "ID :", id(i1))
i2 = 42
print("Identifier i2 :", i2, "Type :", type(i2), "ID :", id(i2))
c1 = complex(i1, i2)
print("After c1 = complex(i1, i2) :", c1, "Type :", type(c1), "ID :", id(c1))
f1 = 3.3
print("Identifier f1 :", f1, "Type :", type(f1), "ID :", id(f1))
f2 = 2025.3
print("Identifier f2 :", f2, "Type :", type(f2), "ID :", id(f2))
c2 = complex(f1, f2)
print("After c2 = complex(f1, f2) :", c2, "Type :", type(c2), "ID :", id(c2))
c3 = complex(i1, f1)
print('After c3 = complex(i1, f1) :', c3, "Type :", type(c3), "ID :", id(c3))
c4 = complex(f2, i2)
print("After c4 = complex(f2, i2) :", c4, "Type :", type(c4), "ID :", id(c4))
s1 = "123"
print("Identifier s1 :", s1, "Type :", type(s1), "ID :", id(s1))
