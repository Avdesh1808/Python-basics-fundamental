#$ (Dollar Sign): Matches the end of a string. world$ would only match strings that end with "world".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern="com$"# when we have to search last string in strings
match1=re.search(pattern,b)
if match1:
    print("match found in b  ", match1.group())
else:
    print("match not found in b")
