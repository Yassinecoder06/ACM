n = int(input())
s = n*(n+1)/2
for i in range(n):
    x = int(input())
    s -= x
print(int(s))
