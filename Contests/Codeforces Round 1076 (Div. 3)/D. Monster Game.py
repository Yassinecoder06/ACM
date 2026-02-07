import sys
import bisect

data = sys.stdin.read().split()
it = iter(data)
try:
	t = int(next(it))
except StopIteration:
	t = 0

out_lines = []
for _ in range(t):
	n = int(next(it))
	a = [int(next(it)) for _ in range(n)]
	b = [int(next(it)) for _ in range(n)]

	a.sort()
	# prefix sums of b for levels
	pref = [0] * n
	pref[0] = b[0]
	for i in range(1, n):
		pref[i] = pref[i-1] + b[i]

	best = 0
	# iterate unique strengths
	i = 0
	while i < n:
		x = a[i]
		# number of swords with strength >= x
		cnt = n - bisect.bisect_left(a, x)
		# number of levels we can finish with cnt swords
		k = bisect.bisect_right(pref, cnt)
		score = x * k
		if score > best:
			best = score
		# skip duplicates
		j = i + 1
		while j < n and a[j] == x:
			j += 1
		i = j

	out_lines.append(str(best))

sys.stdout.write("\n".join(out_lines))
