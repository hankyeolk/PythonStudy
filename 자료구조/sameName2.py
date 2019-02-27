# dictionary
dict1 = dict()
dict1["justin"] = 13
dict1['john'] = 10
dict1['mike'] = 9
dict1['summer'] = 4
print(dict1)

# 동명이인 dictionary로 처리하기
'''
key 값을 이름으로 정하고
해당하는 value에 이름이 찾아진 횟수를 입력해서 조사하면 된다.
'''
name = ['justin', 'tom', 'john', 'tom', 'summer']

def sameName(a):
  name_dict = {}
  for n in a: #리스트에서 값을 직접적으로 for 반복문 요소로 쓰려면 range로 안해줘도 된다.
    print(n)
    if n in name_dict:
      name_dict[n] += 1
    else:
      name_dict[n] = 1

  result = set()
  print()
  for n in name_dict:
    print(n)
    if name_dict[n] >= 2:
      result.add(n)

  return result


print(sameName(name))

# 학생 번호와 학생 이름
s_num = [39, 14, 67, 105]
s_name = ["justin", "john", "mike", "summer"]

def student(a, b, x):
  student_dict = {}
  for i in range(len(a)):
    student_dict[a[i]] = b[i]
  if x in student_dict:
    return student_dict[x]
  else:
    return '?'

print(student(s_num, s_name, 300))
