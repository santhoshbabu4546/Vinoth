s,h=input().split()
s=int(a)
h=int(b)
for i in range(s+1,h):
	count=0
	for x in range(1,i+1):
		if(i%x==0):
			count+=1
	if(count==2):
		print(i,end=' ')
