import sys
from math import comb


def count_winnable(n, k):
    d = n.bit_length() - 1
    total = 0

    for length in range(1, d + 1):
        max_extra_ones = k - length
        if max_extra_ones < 0:
            continue
        bits_after_leading_one = length - 1
        if max_extra_ones >= bits_after_leading_one:
            total += 1 << bits_after_leading_one
        else:
            total += sum(comb(bits_after_leading_one, ones) for ones in range(max_extra_ones + 1))

    if d + 1 <= k:
        total += 1

    return total


data = sys.stdin.buffer.read().split()
t = int(data[0])
answers = []

for i in range(1, 2 * t + 1, 2):
    n = int(data[i])
    k = int(data[i + 1])
    answers.append(str(n - count_winnable(n, k)))

print('\n'.join(answers))
