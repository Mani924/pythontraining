"""
59.copy 1 file content in to another file(Take the source and destination file path from the user)
"""
sourcepath=raw_input("Enter the path of source file:")
destpath=raw_input("Enter the destination path of file where to copy content:")
f= open(sourcepath)
f1 = open(destpath, 'a')
for line in f.readlines():
    f1.write(line)
f1.close()
f.close()

