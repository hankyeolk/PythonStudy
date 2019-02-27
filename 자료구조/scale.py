# 무게가 다른 저울을 판별하는 알고리즘

def weigh(a, b, c, d): # a, b = right / c, d = left (b - a = d - c)
  '''
    a ~ b 가 가볍다면 -1을 호출
    c ~ d 가 가볍다면 1을 호출
    양쪽의 무게가 같다면 0을 호출
  '''
  fake = 29  # 가벼운 동전이 29번이라고 가정
  if a <= fake and fake <= b:
    return -1
  if c <= fake and fake <= d:
    return 1
  return 0

def find_fake(left, right):
  for i in range(left + 1, right + 1):

    result = weigh(left, right, i, i)
    if result == -1:
      return left
    elif result == 1:
      return i
  return -1

n = 100
print(find_fake(0, n - 1))