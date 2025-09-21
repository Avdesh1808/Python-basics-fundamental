# * (Asterisk): Matches the preceding character zero or more times. a*b would match "b", "ab", "aab", and so on
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='y*z'
match=re.findall(pattern,d)
print(match)