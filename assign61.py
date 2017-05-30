"""
61. number of lines, words, characters
"""
num_lines = 0
num_words = 0
num_chars = 0
path=raw_input("enter a path of file:")
with open(path,'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
print "Number of lines in file",num_lines
print "Number of words in file",num_words
print "Num of charcters in a file",num_chars
f.close()
