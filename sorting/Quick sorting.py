# 퀵 정렬

# ver1 (빈 리스트를 만드는 방법)
def quick_sort(a):
  n = len(a)
  if n <= 1:
    return a

  pivot = a[n - 1] # list의 마지막 값을 기준으로 설정
  g1 = []
  g2 = []
  for i in range(0, n - 1): # 마지막 값이 pivot에 기준으로 잡혀있다.
    if a[i] < pivot:
      g1.append(a[i])
    else:
      g2.append(a[i])

  return quick_sort(g1) + [pivot] + quick_sort(g2)

example_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(example_list))

# ver2
def quick_sort_sub(a, start, end):  # 정렬 대상이 start 부터 end 까지 라는 말

  if end - start <= 0:
    return     # 리스트 크기가 1이 되면 종료

  pivot = a[end]  # 기준을 잘 새우는 것이 중요하다.

  i = start
  for j in range(start, end): # end - 1 까지
    if a[j] <= pivot:
      a[i], a[j] = a[j], a[i]
      i += 1
  print(i)
  a[i], a[end] = a[end], a[i]

  quick_sort_sub(a, start, i - 1) # 기적처럼 pivot 값만 빠진 그룹이 2개로 나뉜다.
  quick_sort_sub(a, i + 1, end)   # 다시 재귀함수 호출을 통해서 정렬

def quick_sort2(a):
  quick_sort_sub(a, 0, len(a) - 1)

example_list2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5, 11]

quick_sort2(example_list2)
print(example_list2)

example_list3 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5, 11]

