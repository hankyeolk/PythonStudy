# 1 부터 n 까지의 합 fun1

def sumN(x):
  a = 0
  for i in range(1, x + 1):
    a = a + i
    # x값으로 들어갈 숫자가 1부터 이므로 a를 0으로 시작해주는 것이 맞다.
  return a

# print(sumN(10))
# print(sumN(55))

# 1 부터 n 까지의 합 fun2

def sumN2(x):
  return (x * (x + 1)) // 2  # //는 정수의 나눗셈
# print(sumN2(10))


# 1 부터 n 까지의 제곱합

def sumS(x):
  # a = 0
  # for i in range(1, x + 1):
  #   a = a + i * i # 추가되는 i 요소만 제곱으로 표시 해줘야 한다.
  # return a
  return x * (x + 1) * (2 * x + 1) // 6 # 공식

print(sumS(10))
