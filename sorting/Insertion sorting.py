# 삽입 정렬

# ver.1
# def find_ins_idx(r:list, v): #리스트 r 에서 v가 들어가야 할 위치를 찾는 함수
#   for i in range(0, len(r)):
#     if v < r[i]:
#       return i # v값이 r[i] 값보다 작으면 v가 i번 인덱스에 들어가야 한다는 뜻
#
#   return len(r) # v값이 가장 크다면 맨 뒤에 서야한다는 뜻
#
# def ins_sort(a:list):
#   result = []
#   while a:
#     value = a.pop(0) # list a 에서 가장 앞의 값을 뽑는다.
#     ins_idx = find_ins_idx(result, value)
#     result.insert(ins_idx, value) #ins_idx에 있는 index값에 value에 들어온 값을 넣자.(insert method)
#   return result

example_list = [2, 4, 5, 1, 3]
# print(ins_sort(example_list))

# ver2.(오름차순)
def ins_sort2(a:list):
  n = len(a)
  for i in range(1, n):
    key = a[i]
    j = i - 1  # j가 i의 바로 왼쪽 위치

    while j >= 0 and a[j] > key: # key 값이 들어갈 자리를 찾는 반복문
      a[j + 1] = a[j] # 값을 한 칸 오른쪽으로 이동
      j -= 1
    a[j + 1] = key  # 찾은 위치에 key 값 저장

ins_sort2(example_list)
print(example_list)

# ver3 (내림차순)
example_list2 = [2, 4, 5, 1, 3]
def ins_sort3(a:list):
  n = len(a)
  for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] < key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  print(a)

ins_sort3(example_list2)