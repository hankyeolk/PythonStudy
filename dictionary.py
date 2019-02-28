list1 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(list1))
list2 = ['12', '34', '56']
print(dict(list2))
# dict(list1).get()
print(dict(list1).pop('a'))
print(dict(list1).keys())

diction = {'a':'b', 'b':'c'}
var = list(diction.keys())[0]
result = diction.get('a')
print('%s는 %s이다' % (var, result))