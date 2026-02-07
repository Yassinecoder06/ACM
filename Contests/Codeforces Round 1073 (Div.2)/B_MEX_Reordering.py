#MEX minimum excluded value

def MEX(a: list):
    s = set(a)
    mex = 0
    while mex in s:
        mex += 1
    return mex


def check_valid_ordering(arr):
    n = len(arr)
    for i in range(n - 1):
        prefix_mex = MEX(arr[:i + 1])
        suffix_mex = MEX(arr[i + 1:])
        if prefix_mex == suffix_mex:
            return False
    return True


def can_reorder(a):
    n = len(a)
    
    if len(set(a)) == 1:
        return False
    
    orderings = [
        a,                          
        sorted(a),                  
        sorted(a, reverse=True),   
    ]
    
    for ordering in orderings:
        if check_valid_ordering(ordering):
            return True
    
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if can_reorder(a):
        print("YES")
    else:
        print("NO")