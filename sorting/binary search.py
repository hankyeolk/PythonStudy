# 이분 탐색
'''
 1. 중간 위치를 찾는다
 2. 찾는 값과 중간 위치 값을 비교한다
 3. 같다면 원하는 값 찾은 것
 4. 찾는 값이 중간 값보다 크다면 오른쪽을 대상으로 1번부터 반복
 5. 찾는 값이 중간 값보다 작다면 왼쪽을 대상으로 1번부터 반복
 * 이분 탐색은 미리 정렬된 리스트의 자료를 가지고만 할 수 있다.
'''
# ver1
def binary_search(a, x):
  start = 0
  end = len(a) - 1

  while start <= end:
    mid = (start + end) // 2
    if x == a[mid]:
      return mid
    elif x > a[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return -1 # 찾는 값이 없으면 -1의 값을 가진다.

example = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(binary_search(example, 64))

# ver2 (재귀함수 사용)
def binary_sub(a, x, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2

  if x == a[mid]:
    return mid
  elif x > a[mid]:
    return binary_sub(a, x, mid + 1, end)
  else:
    return binary_sub(a, x, start, mid - 1)

  return -1

def binary(a, x):
  return binary_sub(a, x, 0, len(a) - 1)

example2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
t = binary(example2, 64)
print(t)