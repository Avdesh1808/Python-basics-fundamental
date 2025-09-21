# + (Plus Sign): Matches the preceding character one or more times. a+b would match "ab", "aab", but not "b".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='x+y'
match=re.search(pattern,d)
print(match)