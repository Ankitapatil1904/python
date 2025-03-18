" Multiple List Objects with the same set of elements "
print("\t -- Multiple List Objects with the same set of elements --\n")
l1 = ['Python', 123, 3.14, 12+34j, True, -240, 0, 11.22]
print("Identifier l1 :", l1, "Type :", type(l1), "ID :", id(l1))
l2 = ['Python', 123, 3.14, 12+34j, True, -240, 0, 11.22]
print("Identifier l2 :", l2, "Type :", type(l2), "ID :", id(l2))
l3 = l2
print("Identifier l3 :", l3, "Type :", type(l3), "ID :", id(l3))
l3[2] = 12.34
print("\nAfter making changes into the identifier l3 :")
print("Identifier l1 :", l1, "Type :", type(l1), "ID :", id(l1))
print("Identifier l2 :", l2, "Type :", type(l2), "ID :", id(l2))
print("Identifier l3 :", l3, "Type :", type(l3), "ID :", id(l3))
print("\nThank you.")
