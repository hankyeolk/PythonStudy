#tuple_bitcode
myTuple = ('k', 'l', 'i', 'a')
# sorted(myTuple)
# print(myTuple)
print(type(myTuple))
print(myTuple + ('oh', 'i'))

a = (10, 20, 30, 20, 40, 30)
print(10 in a)
b = tuple(i for i in range(10) if i % 2 == 0)
print(b)