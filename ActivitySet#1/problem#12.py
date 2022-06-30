import re
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
naam = open(name)
g=list()
omkar={}
for line in naam:
  m=re.search("From ")
    m=line.split()
    if len(m)>0
      a=m[1]
      g.append(a)
for word in g:
    omkar[word]=omkar.get(word,0)+1
biggest=None
for word,s in omkar.items():
    if biggest is None or s>biggest:
        biggest=s
        bigword=word
print(bigword,biggest)
