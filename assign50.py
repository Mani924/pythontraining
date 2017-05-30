"""
50.input n=3 
    output: 	111
		101
		111
"""
n= input("Enter number:")
for i in range(n):
        for j in range(n):
                if j==0 or j==n-1 or i==0 or i==n-1:
                        print 1,
                else:
                        print 0,
        print "\n"
