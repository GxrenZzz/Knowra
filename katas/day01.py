s = "the cat sat on the mat"

# 1 
words = s.split()
for i in words:
  print(f"{i} : {len(i)}")

# 2 
words = s.split()
words = "".join(words)
count = {}
for char in words:
  count[char]  = count.get(char,0) + 1

print(count)


# 3 
words = s.split()
count ={}
for i in words:
  count[i] = count.get(i,0) + 1

for k,v in sorted(count.items(), key=lambda items : (-items[1],items[0])):
  print(k,v)

