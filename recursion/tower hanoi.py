def hanoi(n, start, end, support):
  if n == 1:
    print(start, "-->", end)
    return

  hanoi(n - 1, start, support, end)
  print(start, "-->", end)
  hanoi(n - 1, support, end, start)


print("n = 1")
print(hanoi(1, 1, 3, 2))
print()
print("n = 2")
print(hanoi(2, 1, 3, 2))
print()
print("n = 3")
print(hanoi(3, 1, 3, 2))