"""
33.input: "google" print count of each character
"""
s=raw_input("enter a string:")
s1=set(s)
for i in s1:
  print i,s.count(i)
