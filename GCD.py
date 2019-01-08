#최대공약수 구하기
# def gcd(a, b):
#   i = min(a, b)
#   while True:
#     if a % i == 0 and b % i == 0:
#       return i
#     i -= 1
#
# print(gcd(4, 6))
# print(gcd(1, 5))

#유클리드 정리 - gcd(a, b) = gcd(b, a % b)
#           - gcd(n, 0) = n (종료 조건)

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

print(gcd(10, 8))

# fucking fibona
def fibona(n):
  # if n == 1 or n == 2: #이 방법되 괜찮지만
  #   return 1
  if n <= 1:
    return n
  return fibona(n - 1) + fibona(n - 2)
print(fibona(5))