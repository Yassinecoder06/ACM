from collections import Counter

n = int(input())
s = list(input())

c = Counter(s)
out = list(c["n"]*"1"+c["z"]*"0")
 
print(" ".join(out))