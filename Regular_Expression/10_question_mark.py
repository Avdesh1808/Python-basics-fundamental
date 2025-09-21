# ? (Question Mark): Matches the preceding character zero or one time. It makes the preceding part optional. colou?r would match both "color" and "colour".
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='xy?z'
match=re.findall(pattern,d)
print(match)