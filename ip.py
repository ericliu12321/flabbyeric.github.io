import re

f = input ("Enter file name (indluding the .txt): ")
g = open(f, "r")
h = open("result.txt", "w")

lines = g.readlines()
for txt in lines:
    pattern = '(172\.16\.)(.*)'
    match = re.search(pattern, txt)

    if not(match):
        g.write(txt)
