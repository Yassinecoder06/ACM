for i in range(int(input())):
    n = int(input())
    print((len(sorted(list(input().split('*')))[-1])+1)//2)