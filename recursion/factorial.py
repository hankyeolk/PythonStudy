# factorial
# def fact(a):
#   f = 1
#   for i in range(1, a + 1):
#     f = f * i
#   return f
# print(fact(5))

# 재귀함수로 factorial 계산 (중요!)
def fact(a):
  if a <= 1:
    return 1
  return a * fact(a - 1)

print(fact(10))
# 재귀로 n개 숫자 합 구하기
def sumf(a):
  if a <= 1:
    return 1
  return a + sumf(a - 1)
print(sumf(10))

# 재귀로 n개의 숫자 중 최댓값 구하기
example_list = [17, 92, 18, 33, 58, 7, 33, 42]
# def find_max(a):
#   n = len(a)
#
#   for i in range(1, n):
#     max_v = a[0]
#     if max_v < a[i]:
#       max_v = a[i]
#       return max_v
#
#   return
def find_max(a, n):
  if n == 1:
    return a[0]  # 리스트 크기가 1일 때가 가장 기본적인 환경

  max_n_1 = find_max(a, n - 1)
  if max_n_1 > a[n - 1]:
    return max_n_1
  else:
    return a[n - 1]

print(find_max(example_list, len(example_list)))