# '\' used to drop special character
import re # re is a module  it is a inbuild module in python
# This is the example of text where we ll use to find pattern in the string.
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
match=re.search(r"\.",b)#search function is used for search pattern in string. we use backword slash ' \ ' to find '.' in string pattern
print(match)