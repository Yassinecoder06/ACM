import sys
import bisect

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
a = list(map(int, data[2:2 + n]))
b = list(map(int, data[2 + n:2 + n + m]))

a.sort()

result = []
for bj in b:
    count = bisect.bisect_right(a, bj)
    result.append(count)

print(' '.join(map(str, result)))