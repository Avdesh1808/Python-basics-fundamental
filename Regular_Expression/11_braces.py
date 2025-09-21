# {m,n} (Braces): Matches the preceding character at least m and at most n times. a{2,4} would match "aa", "aaa", and "aaaa".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='y{1,4}'
match=re.findall(pattern,d)
print(match)