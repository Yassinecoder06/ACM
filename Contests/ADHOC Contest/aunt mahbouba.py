test = int(input())
l = []
for i in range(test):
    n = int(input())
    s = 0
    some_list = list(map(int, input().split()))
    for el in some_list:
        s += el
    l.append(-s)

for i in range(test):
    print(l[i])