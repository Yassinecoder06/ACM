import sys


MOD = 676767677
data = list(map(int, sys.stdin.buffer.read().split()))
tests = data[0]
index = 1

answers = []
for _ in range(tests):
    n = data[index]
    index += 1
    a = data[index:index + n]
    index += n

    total = 0
    last_non_one = -1
    for position, value in enumerate(a):
        if value > 1:
            total += value
            last_non_one = position

    if last_non_one == -1:
        answers.append("1")
    else:
        has_trailing_one = any(value == 1 for value in a[last_non_one + 1:])
        answers.append(str((total + (1 if has_trailing_one else 0)) % MOD))

sys.stdout.write("\n".join(answers))
        
