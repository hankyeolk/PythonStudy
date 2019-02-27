# 친밀도 계산

fr_info = {
  'summer': ['john', 'justin', 'mike'],
  'john': ['summer', 'justin'],
  'justin': ['john', 'summer', 'mike', 'may'],
  'mike': ['summer', 'justin'],
  'may': ['justin', 'kim'],
  'kim': ['may'],
  'tom': ['jerry'],
  'jerry': ['tom']
}

def print_all_friends(g, start):
  qu = [] #앞으로 처리해야 할 사람을 queue에 저장
  done = set() #이미 queue에 추가한 사람을 집합에 기록해서 중복방지

  qu.append((start , 0)) # start = 사람 이름, 0 = 친밀도 계산 --> tuple 형태로 저장 // 자기자신에 대한 친밀도는 = 0
  done.add(start)

  while qu:
    (p, d) = qu.pop(0) # (p = name, d = 친밀도)

    print(p, d) # 이 부분에만 print를 줘야 이름이 한 명씩 나온다.

    for x in g[p]:
      if x not in done: # g['summer']의 value 값들을 queue, set에 저장
        qu.append((x, d + 1))
        done.add(x)


print_all_friends(fr_info, 'summer')