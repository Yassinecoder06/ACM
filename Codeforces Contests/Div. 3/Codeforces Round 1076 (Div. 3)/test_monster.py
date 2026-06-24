import random
from subprocess import Popen, PIPE, STDOUT

# Import the fast solution by reading the file and defining a function
import importlib.util, sys
spec = importlib.util.spec_from_file_location('monster_fast', 'D. Monster Game.py')
monster_fast = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monster_fast)

# Fast solver function: wrap logic from file into a callable
def fast_solve(a, b):
    n = len(a)
    A = sorted(a)
    pref = [0]*n
    pref[0] = b[0]
    for i in range(1,n):
        pref[i] = pref[i-1] + b[i]
    import bisect
    best = 0
    i = 0
    while i < n:
        x = A[i]
        cnt = n - bisect.bisect_left(A, x)
        k = bisect.bisect_right(pref, cnt)
        score = x * k
        if score > best:
            best = score
        j = i+1
        while j < n and A[j]==x:
            j+=1
        i=j
    return best

# Brute solver: try all x from 0..max(a) and compute cnt accordingly
def brute_solve(a,b):
    n = len(a)
    best = 0
    for x in range(0, max(a)+1):
        cnt = sum(1 for val in a if val >= x)
        # compute how many levels
        cur = 0
        k = 0
        for bi in b:
            if cur + bi <= cnt:
                cur += bi
                k += 1
            else:
                break
        if x * k > best:
            best = x * k
    return best

random.seed(1)
for _ in range(20000):
    n = random.randint(1,7)
    a = [random.randint(1,10) for _ in range(n)]
    b = [random.randint(1,n) for _ in range(n)]
    f = fast_solve(a,b)
    g = brute_solve(a,b)
    if f != g:
        print('Found mismatch')
        print('n=',n)
        print('a=',a)
        print('b=',b)
        print('fast=',f)
        print('brute=',g)
        break
else:
    print('No mismatches found')
