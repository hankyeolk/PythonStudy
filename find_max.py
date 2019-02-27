# the largest number finding
example_list = [17, 92, 18, 33, 58, 7, 33, 42]

def find_max(a):
  n = len(a)
  max_v = a[0]
  for i in range(1, n):
    if a[i] > max_v:
      max_v = a[i]
  return max_v

print(find_max(example_list))

# find the largest number's index

def find_idx(a):
  n = len(a)
  max_idx = 0
  for i in range(1, n):
    if a[i] > a[max_idx]:
      max_idx = i
  return max_idx

print(find_idx(example_list))

#find minimum number index
def find_min_idx(a):
  n = len(a)
  min_idx = 0
  for i in range(1, n):
    if a[i] < a[min_idx]:
      min_idx = i
  return min_idx

print(find_min_idx(example_list))
print(min(example_list))