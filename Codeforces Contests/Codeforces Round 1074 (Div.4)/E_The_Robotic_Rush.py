import sys
import bisect


def main() -> None:
	data = sys.stdin.buffer.read().split()
	t = int(data[0])
	idx = 1
	out_lines = []
	inf = 10**30

	for _ in range(t):
		n = int(data[idx])
		m = int(data[idx + 1])
		k = int(data[idx + 2])
		idx += 3

		a = list(map(int, data[idx:idx + n]))
		idx += n

		b = list(map(int, data[idx:idx + m]))
		idx += m
		b.sort()

		gdCode = data[idx].decode()
		idx += 1

		right_reach = [0] * k
		left_reach = [0] * k
		s = 0
		mn = 0
		mx = 0
		for i, ch in enumerate(gdCode):
			if ch == 'R':
				s += 1
			else:
				s -= 1
			if s > mx:
				mx = s
			if s < mn:
				mn = s
			right_reach[i] = mx
			left_reach[i] = -mn

		death_at = [0] * (k + 2)

		for pos in a:
			j = bisect.bisect_left(b, pos)
			dl = pos - b[j - 1] if j > 0 else inf
			dr = b[j] - pos if j < m else inf

			if dl != inf:
				p = bisect.bisect_left(left_reach, dl)
				tL = p + 1 if p < k else k + 1
			else:
				tL = k + 1

			if dr != inf:
				p = bisect.bisect_left(right_reach, dr)
				tR = p + 1 if p < k else k + 1
			else:
				tR = k + 1

			dt = tL if tL < tR else tR
			if dt <= k:
				death_at[dt] += 1

		alive = n
		ans = []
		for i in range(1, k + 1):
			alive -= death_at[i]
			ans.append(str(alive))
		out_lines.append(' '.join(ans))

	sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
	main()
