# '[]' used for define a charachter set in regular expression
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
match=re.findall(r"[A]",b)
print(match)
print(type(match))
