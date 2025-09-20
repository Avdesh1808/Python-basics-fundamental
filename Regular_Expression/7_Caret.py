# ^ (Caret): Matches the beginning of a string. ^hello would only match strings that start with "hello".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='^charlie'
match=re.search(pattern,a)
print(match)