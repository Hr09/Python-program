fname=input("Enter file name")
try:
    fhand=open(fname)
except:
    print("File name not found",fname)
    quit()
lst=list()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if line == "": continue

    words = line.split()
    if words[0] !="From": continue
    secwords=words[5].split(':')
    counts[secwords[0]]=counts.get(secwords[0],0)+1

for k,v in counts.items():
    lst.append((k,v))
lst.sort()


for k,v in lst:
    print(k,v)
