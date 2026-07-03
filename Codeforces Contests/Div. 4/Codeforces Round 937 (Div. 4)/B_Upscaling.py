t = int(input())

for _ in range(t):
    n = int(input())
    

    lign1 = ("##" + "..") * (n // 2) + ("##" if n % 2 else "")
    
    lign1 = "".join("##" if j % 2 == 0 else ".." for j in range(n))
    lign2 = "".join(".." if j % 2 == 0 else "##" for j in range(n))

    for i in range(n):
        row = lign1 if i % 2 == 0 else lign2
        print(row)
        print(row)