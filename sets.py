#Stores multiple values in single variable
#Unordered
myset = {"car", "bike", "boat","trsin"}
# print(myset)
#Unchangable
#dublicates are not allowed
# print("bike"in myset)

myset1 = {1,2,3,4,}
myset2 = {4,5,6}
# myset3 = myset1.union(myset2)
myset3 = myset1.intersection(myset2)
myset4 = myset1.symmetric_difference(myset2)
# myset.add("cycle")
print(myset4)