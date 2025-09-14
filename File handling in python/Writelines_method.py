# This is the code example of readlines in a file
# This methode used to write a sequence of string to a file.
f=open('File handling in python/T.txt','w')
lines= ['25 26 29\n','30 20 40 \n','50 60 20\n','60 50 70\n']#\n this key use for next line and write a data in a file as string form
f.writelines(lines)
f.close()