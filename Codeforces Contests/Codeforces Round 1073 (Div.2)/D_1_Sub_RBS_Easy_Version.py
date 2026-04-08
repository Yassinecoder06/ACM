import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(200005)
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    t = int(next(iterator))
    results = []
    
    for _ in range(t):
        try:
            n = int(next(iterator))
            s = next(iterator)
        except StopIteration:
            break
            
        tot_open = n // 2  # Since s is RBS, number of '(' is exactly n/2
        curr_open = 0
        found = False
        
        # We need to find a ')' followed by '(' such that there is at least one more '(' after that.
        # i.e., s[i] == ')', s[i+1] == '(' and count('(') in s[i+2:] >= 1
        
        for i in range(n - 1):
            if s[i] == '(':
                curr_open += 1
            else:
                # s[i] == ')'
                if s[i+1] == '(':
                    # The number of open brackets in s[i:] is (tot_open - curr_open)
                    # s[i] is ')', so it doesn't consume an open bracket from the count
                    # s[i+1] is '(', which consumes one
                    # So open brackets available after i+1 is (tot_open - curr_open) - 1
                    
                    if (tot_open - curr_open) - 1 >= 1:
                        found = True
                        break
        
        if found:
            results.append(str(n - 2))
        else:
            results.append("-1")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()

          