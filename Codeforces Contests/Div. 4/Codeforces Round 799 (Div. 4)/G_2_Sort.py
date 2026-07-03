for _ in range(int(input())):
  n,k=map(int,input().split())
  d=[*map(int,input().split())]
  s=t=0
  for i in range(n-1):
    if d[i]<d[i+1]*2:t+=1
    else:t=0
    if t>=k:s+=1
  print(s)