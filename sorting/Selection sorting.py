#선택 정렬
d = [2, 4, 5, 1, 3]

def find_min_idx(a):
  n = len(a)
  min_idx = 0
  for i in range(1, n):
    if a[i] < a[min_idx]:
      min_idx = i
  return min_idx

def sel_sort(a):
  result = []
  while a: #list a에 아직 자료가 남아있으면 밑에 실행부분을 실행해라
    min_idx = find_min_idx(a) #최솟값을 찾아라
    value = a.pop(min_idx) #pop(i)는 index = i인 값을 빼오는 것.
    result.append(value)  #비어 있는 리스트에 value에 저장된 값을 넣어라.
  return result

print(sel_sort(d))


def sel_sort2(a):
  min_idx = 0
  for i in range(0, len(a) - 1):
    min_idx = i

    for j in range(i + 1, len(a)):

      if a[j] < a[min_idx]:
        min_idx = j

    a[i], a[min_idx] = a[min_idx], a[i]  # 두 자료의 값의 위치를 바꾸는 방법! #for문 밖에서 바꿔주면 된다.
  print(a)

sel_sort2(d)

#O(n**2) 복잡도

def sel_sort_max(a:list):
  n = len(a)
  for i in range(0, n - 1):
    max_idx = i
    for j in range(i + 1, n):
      if a[j] > a[max_idx]:
        max_idx = j
    a[i], a[max_idx] = a[max_idx], a[i]
  print(a)

sel_sort_max(d)