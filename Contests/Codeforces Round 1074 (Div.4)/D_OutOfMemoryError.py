import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        h = int(data[idx + 2])
        idx += 3

        original = list(map(int, data[idx:idx + n]))
        idx += n

        cur_val = [0] * n
        cur_ver = [0] * n
        ver = 1

        for _ in range(m):
            b = int(data[idx]) - 1
            c = int(data[idx + 1])
            idx += 2

            base = cur_val[b] if cur_ver[b] == ver else original[b]
            newv = base + c

            if newv > h:
                ver += 1
            else:
                cur_ver[b] = ver
                cur_val[b] = newv

        res = []
        for i in range(n):
            res.append(str(cur_val[i] if cur_ver[i] == ver else original[i]))
        out_lines.append(' '.join(res))

    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    main()


