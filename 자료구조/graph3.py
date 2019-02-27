# 탐색 알고리즘
# BFS(Breadth First Search)
num_tree = {
  1: [2, 3],
  2: [1, 4, 5],
  3: [1],
  4: [2],
  5: [2]
}

def bfs(object, start):
  queue = []
  done = set()

  queue.append((start, 0))
  done.add(start)

  while queue:
    (x, y) = queue.pop(0)
    print((x, y))

    for p in object[x]: # num_tree[1]에 관련된 값들만 호출된다.
      if p not in done:
        queue.append((p, y + 1))
        done.add(p)

bfs(num_tree, 1)