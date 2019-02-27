# finding exit
# a 를 시작점으로 p에 도달하는 가장 짧은 경로를 구하는 함수

def maze(graph, start, end):
  qu = []
  done = set()    # 집합의 역할을 qu 다음에 저장하게 해서 중복을 막게 하는 것

  qu.append(start)
  done.add(start)

  while qu:
    x = qu.pop(0)  # 문자열로 만들어 주는 것
    v = x.split("->")[-1] # qu에 저장된 노드의 마지이 처리해야 할 노드

    if v == end:
      return x                # 지금까지의 전체 이동 경로 알려주는 것
    for y in graph[v]:        # 아직 처리가 안 된 노드들을 중
      if y not in done:       # 큐에 저장된 적이 없는 노드를
        qu.append(x +"->"+ y) # 새 이동경로 형태로 큐에 저장
        done.add(y)           # 중복 방지를 위해 집합에도 저장


maze_g = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}
print(maze(maze_g, 'a', 'o'))
