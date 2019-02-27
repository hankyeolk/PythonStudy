#find friends

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

  qu.append(start)
  done.add(start)

  while qu:
    p = qu.pop(0)

    print(p) # 이 부분에만 print를 줘야 이름이 한 명씩 나온다.

    for x in g[p]:
      if x not in done: # g['summer']의 value 값들을 queue, set에 저장
        qu.append(x)
        done.add(x)


print_all_friends(fr_info, 'summer')