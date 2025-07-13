word = input()
word_vow = 0

for i in range(len(word)):
  if word[i] == 'a':
    word_vow += 1
  elif word[i] == 'e':
    word_vow += 2
  elif word[i] == 'i':
    word_vow += 3
  elif word[i] == 'o':
    word_vow += 4
  elif word[i] == 'u':
    word_vow += 5
print(word_vow)