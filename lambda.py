# list1 = [3,4,10,9,18,66,13,15]

# evenNum = list(filter(lambda i : i%2==0,list1))
# print(evenNum)

# square = list(map(lambda i : i**2,list1))
# print(square)

# list2 = [10,20,30,40,50]

# triple = list(map(lambda i : i*3 , list2))
# print(triple)

# list3 = ["a","B","C","D","e","f"]
# reverse = list(map(lambda i : i.swapcase(),list3))
# print(reverse)

# #decorators
# def div(a,b):
#     print(a/b)

# def good_div(func):

#     def inner_div(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)

#     return inner_div


from functools import reduce

list1 = [1,2,3,4,5,6,7]
sum = reduce(lambda i,j: i+j, list1)
print(sum) 