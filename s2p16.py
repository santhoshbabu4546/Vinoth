s,h=map(int,input().split())
for i in range (s+1,h):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i, end=' ')
