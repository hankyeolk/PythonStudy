# mySet = {'a', 1.2, (1,2,4)} #list can not join in 'set'
# print(type(mySet))
#
# a = {1,2,3,4,5,6,7}
# b = {2,4,5,6,1,7,9}
# print(a.intersection(b)) #교집합
# print(a.union(b)) # union(합집합)
# print(a.difference(b)) #a 차집합

newmySet = {1}
newmySet.add('a')
print(newmySet)
newmySet.update([1,2], [3,4])
print(newmySet)
print(newmySet.pop())
