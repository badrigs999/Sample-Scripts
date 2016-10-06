

x, y, z, n = int(input()), int(input()), int(input()), int(input())

for a in range(0,x+1):
	for b in range(0,y+1):
		for c in range(0,z+1):
			if a+b+c != n:
				print ([a,b,c])
			else:
				pass

#              or
#how to use single line using for loop.......
# print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])