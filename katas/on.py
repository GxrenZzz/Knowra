words = list("abcdefghij")
step =3
size=4
chunck_words_list = []
for i in range(0,len(words),step):
  chunck = words[i:i + size]
  chunck_words_list.append(chunck)
  i = i + step

print(words[9:13])