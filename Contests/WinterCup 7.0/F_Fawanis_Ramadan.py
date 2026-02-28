n = int(input())
s = input()

def count(l,n):
    nb = 0
    for i in range(n-1):
        if l[i] == "1" and l[i+1]=="0":
            nb +=1
    return nb
l = list(s)
if count(l,n) == count(l[::-1],n):
    print("0")
if count(l,n) > count(l[::-1],n):
    print("1")
    print(s.find("1"))
if count(l,n) < count(l[::-1],n):
    print("1")
    print(s.find("0"))
