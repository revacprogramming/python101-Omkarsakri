# Tuples
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
x=handle.read()
l=[]
d={}
for line in handle:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From"):
        y=line.split()
        a=y[5]
	can=a.split(':')
    candle=can[0]
    l.append(candle)
    l.sort()
for word in l:
    d[word]=d.get(word,0)+1

for a,b in d.items():
    print(a,b)
