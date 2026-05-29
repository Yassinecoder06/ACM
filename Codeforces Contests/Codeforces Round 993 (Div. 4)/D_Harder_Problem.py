import sys
import heapq


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    outputs = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        counts = [0] * (n + 1)
        heap = [(0, v) for v in range(1, n + 1)]
        heapq.heapify(heap)

        res = [0] * n
        prev = None

        for i, ai in enumerate(a):
            if i == 0 or ai != prev:
                chosen = ai
            else:
                while heap and counts[heap[0][1]] != heap[0][0]:
                    heapq.heappop(heap)
                if heap and heap[0][0] < counts[ai]:
                    chosen = heap[0][1]
                else:
                    chosen = ai

            counts[chosen] += 1
            heapq.heappush(heap, (counts[chosen], chosen))
            res[i] = chosen
            prev = ai

        outputs.append(" ".join(map(str, res)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()