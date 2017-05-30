"""
51. input: google
	output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension
"""
s="google"
c = {i:s.count(i) for i in s}
print c
