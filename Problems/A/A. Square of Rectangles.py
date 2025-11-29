import sys
import math
input = sys.stdin.readline

def can_make_square(rects):
    # rects = [(l1,b1), (l2,b2), (l3,b3)]
    area = sum(l*b for l,b in rects)
    S = int(math.isqrt(area))
    if S*S != area:
        return False

    # Case A: all three in one row
    if all(b == S for _,b in rects) and sum(l for l,_ in rects) == S:
        return True
    # Case B: all three in one column
    if all(l == S for l,_ in rects) and sum(b for _,b in rects) == S:
        return True

    # Try 2 on one strip, 1 on the other
    # i,j go together; k goes alone
    for i in range(3):
        for j in range(i+1, 3):
            k = 3 - i - j
            li, bi = rects[i]
            lj, bj = rects[j]
            lk, bk = rects[k]

            # horizontal split: top row has i&j, bottom row has k
            # top: same height bi=bj, widths sum to S
            # bottom: width lk=S, heights bi+bk=S
            if bi == bj and bi + bk == S and li + lj == S and lk == S:
                return True

            # vertical split: left column has i&j, right col has k
            # left: same width li=lj, heights sum to S
            # right: height bk=S, widths li+lk=S
            if li == lj and bi + bj == S and bk == S and li + lk == S:
                return True

    return False

def main():
    t = int(input())
    for _ in range(t):
        a = list(map(int, input().split()))
        # note input guarantees l3≤l2≤l1 and b3≤b2≤b1, but our code works for any order
        rects = [(a[0],a[1]), (a[2],a[3]), (a[4],a[5])]
        print("YES" if can_make_square(rects) else "NO")


main()

