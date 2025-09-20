#. (Dot): Matches any single character except a newline. It's a wildcard for a single position. For example, (c.t) would match "cat", "cot", and "cut". (Dot): Matches any single character except a newline. It's a wildcard for a single position. For example, c.t would match "cat", "cot", and "cut"
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
match=re.search(r"[x.z]",d)
print(match)