import bisect

n = int(input())

r = list(map(int, input().split()))
s = list(map(int, input().split()))
raduis_score = list(zip(r, s))

cx, cy = map(int, input().split())

m = int(input())

raduis_score.sort(key=lambda x: x[0])
r.sort()
rsquared = list(map(lambda x: x**2, r))

score_total = 0
for _ in range(m):
    x,y = map(int, input().split())
    r2 = (x-cx)**2 + (y-cy)**2
    if r2 <= rsquared[-1]:
        idx = bisect.bisect_left(rsquared, r2)
        score_total += raduis_score[idx][1]

print(score_total)