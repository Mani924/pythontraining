"""
48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
"""
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
n = []
out = []
for i in l:
	if l.index(i) == 0:
		n.extend([i])
	if l.index(i) != 0:
		j = l[l.index(i)-1]
		if (j+1) == i:
			n.extend([i])
		else:
			out.append(n)
			n = []
			n.extend([i])
			if l.index(i) == (len(l)-1):
				out.append(n)

print out
