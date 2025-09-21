# () (Parentheses): Used for grouping and capturing. They group parts of a regex together so a quantifier like * or + can apply to the entire group. For example, (ab)+ would match "ab", "abab", "ababab", etc. They also capture the matched substring, which can be retrieved later.
import re
a='charlie and the cocolate factory'
b='Avdeshchuahan.singh.@gmail.com'
c='hello'
d='xyz,xyyz,xyz,xyyz,xxy,xyzz,zyx,yxz'
pattern='(singh)+'
match=re.findall(pattern,b)
if match:
    print("Text founded in b ", match)
else:
    print("no text found in b")

