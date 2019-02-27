# set practice
# s = set()
# s.add(1)
# s.add(2)
# print(len(s))
# s.discard(2)
# s.clear()
# print(2 in s)

# find 동명이인
name = ["tom", "jerry", "mike", "tom"]
name2 = ["tom", "jerry", "mike", "tom", "mike"]
def find_same(a):
  n = len(a)
  result = set()
  for i in range(0, n - 1): # 마지막 자료는 앞에 것들과 다 비교했기 때문에 제외해도 된다.
    for j in range(i + 1, n):
      if a[i] == a[j]:
        result.add(a[i]) # 값이 같으면 set에 넣어라
  return result

print(find_same(name))
print(find_same(name2))

# 가능한 짝 조합 출력하기
name3 = ["tom", "jerry", "mike"]
def matching(a):
  n = len(a)
  for i in range(0, n - 1):
    for j in range(i + 1, n):
      print(a[i] ," - " , a[j])

matching(name3)
