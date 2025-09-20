#| (Pipe): Acts as an OR operator. cat|dog would match either "cat" or "dog".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
match=re.findall(r"[x|y]",d)
print(match)