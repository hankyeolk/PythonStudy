# 병합 정렬

example_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
example_list2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
example_list3 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

# ver1
def merge_sort(a:list):
  n = len(a)

  if n <= 1:
    return a  # 리스트의 크기가 가장 작은 1일때. (종결 조건)

  mid = n // 2 # 리스트를 반으로 나눈다.
  g1 = merge_sort(a[:mid])  # 재귀 호출로 첫 번째 그룹 (0 ~ mid - 1)
  # print(g1)
  g2 = merge_sort(a[mid:])  # 재귀 호출로 첫 번째 그룹 (mid ~ n - 1)
  # print(g2)

  result = []
  while g1 and g2:
    if g1[0] < g2[0]:
      result.append(g1.pop(0))
    else:
      result.append(g2.pop(0))

  while g1:
    result.append(g1.pop(0))
  while g2:
    result.append(g2.pop(0))
  return result

print(merge_sort(example_list))

# ver2
def merge_sort2(a:list):
  n = len(a)

  if n <= 1:
    return

  mid = n // 2
  g1 = a[:mid]
  g2 = a[mid:]
  merge_sort2(g1)  # 재귀함수로 g1, g2 정렬
  merge_sort2(g2)

  i1 = 0
  i2 = 0
  ia = 0

  while i1 < len(g1) and i2 < len(g2):
    if g1[i1] > g2[i2]:  # 오름차순 하고 싶으면 < 이렇게 하면 된다.
      a[ia] = g1[i1]
      i1 += 1
      ia += 1
    else:
      a[ia] = g2[i2]
      i2 += 1
      ia += 1

  while i1 < len(g1): # 남아있는 부분을 정렬해주는 것
    a[ia] = g1[i1]
    i1 += 1
    ia += 1
  while i2 < len(g2):
    a[ia] = g2[i2]
    i2 += 1
    ia += 1

merge_sort2(example_list2)
print(example_list2)
