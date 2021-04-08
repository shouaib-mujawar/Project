l=[2,7,5]
n=len(l)
for i in range(0,n):
	for j in range(i,n):
		for k in range(i,j+1):
			print(l[k],end=" ")
		print("\n",end="")