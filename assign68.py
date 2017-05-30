"""
68. Take Source and destination file paths from command line arguments and copy the sourcontent into destination.
    Make Sure that your program checking the below conditions.
     1.if the source file not there. Should ask the user to enter new source file or want to quit a program
     2.if the destination file already there in the specified path. Should warn the user want to proceed
     or want to enter new destination file name or want to quit
"""
import os  
source=(raw_input('Enter a source path'))
def fileop(source):
    if os.path.exists(source):
        des=raw_input('Enter a des path')
        if os.path.exists(des):
            print "File already existS"
            x=raw_input("do you want to proceed or enter new destination file name or want to quit(proceed,new,quit):")
            if x.lower()=='proceed':
                f=open(source)
                f1=open(des, 'a')
                for line in f.readlines():
                    f1.write(line)
                f1.close()
                f.close()
                print "Content copied to des file:"
            elif x.lower()=='new':
                des=raw_input('Enter a new des path')
                f=open(source)
                f1 = open(des, 'a')
                for line in f.readlines():
                    f1.write(line)
                    f1.close()
                    f.close()
                print "Content copied to des file:"
            else:
                print "User quit from process"
        else:
           f=open(source)
           f1=open(des, 'a')
           for line in f.readlines():
               f1.write(line)
           f1.close()
           f.close()
           print "Content copied to des file:"
           
    else:
        print "file doesnot exit:"
        x=raw_input('do you want enter a new file or quit the program(Yes/quit)')
        if x.lower()=='yes':
            source=raw_input('Enter a new source path')
            fileop(source)
        else:
            print "user want to quit the process"
fileop(source)
