def solve(n: int):
    if n % 2 == 0:  
        k = n // 2
        print(k)
        print("2 " * k)        
    else:         
        k = (n - 3) // 2 + 1
        print(k)
        print("2 " * (k - 1) + "3")

n = int(input())
solve(n)
