# palindrome(회문)

# ver using queue, stack
def palindrome(a):
  qu = []
  st = []

  for x in a: # string 값을 idx = 0 ~ len(a)까지 순차적으로 가져오는 것

    if x.isalpha():  # x라는 string값이 알파벳으로만 구성되어있는지 여부를 알아보는 method(true/false)
                     # 공백, 특수문자 걸러냄
      qu.append(x.lower()) # lowercase(소문자)로 바꾸어 복사
      st.append(x.lower())

    while qu:
      if qu.pop(0) != st.pop():
        return False

  return True

print(palindrome("Wow"))

# ver not use queue, stack
def palindrome2(a):

  i = 0
  j = len(a) - 1
  while i < j:
    if a[i].isalpha() == False:  # i번째 글자가 알파벳이 아니면 뒤로 한칸 이동
      i += 1
    elif a[j].isalpha() == False:
      j -= 1
    elif a[i].lower() != a[j].lower():
      return False

    else:
      i += 1
      j -= 1

  return True
print(palindrome2("madaM, I ' m AdaM"))

