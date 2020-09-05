import re

f = input ("Enter file name (indluding the .txt): ")
g = open(f, "r")

lines = g.readlines()
i = 0
a = ""
b = ""
c = ""
for txt in lines:
    if i%4 == 1:
        pattern = '^(  Name: )(.*)'
        match = re.search(pattern, txt)
        a = match.group(2)
    if i%4 == 2:
        pattern = '^(  JNDI name: )(.*)'
        match = re.search(pattern, txt)
        b = match.group(2)
    if i%4 == 3:
        pattern = '^(  Base Queue Name: )(.*)'
        match = re.search(pattern, txt)
        c = match.group(2)
        print(a + " " + b + " " + c)
    i += 1
