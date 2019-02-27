#순차 탐색 (Sequential Search)
example_list = [17, 92, 18, 33, 58, 5, 33, 42]

def seqS(a, x):
  for i in range(len(a)):
    if a[i] == x:
      return i
  return -1  #else를 쓰면 끝까지 가지 않고 종료해버림

print(seqS(example_list, 900))

def seqS2(a, x):
  k = []
  for i in range(len(a)):
    if a[i] == x:
      k.append(i)
  return k

print(seqS2(example_list, 900))

s_num = [39, 14, 67, 105]
s_name = ["justin", "john", "mike", "summer"]

def seqS3(a, b, x):
  for i in range(len(a)):
    if a[i] == x:
      return b[i]
  return "?"
print(seqS3(s_num, s_name, 67))