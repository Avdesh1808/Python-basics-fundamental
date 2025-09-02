# import module_name
# import my_math
# print(f"using import: {my_math.add(2,3)}")
# print(f"using import: {my_math.pi}")

# from module_name import item
from my_math import sub
from my_math import add
print(f"using import : {sub(6,3)}")
print(f"using import : {add(6,3)}")  # there is no need to prefix in code when item import from modules

# 4. import module_name as alias 
import my_math as mm
print(f"using import : {mm.sub(6,3)}")# we can access any module by alias name means short names  which we can define by own
print(f"using import : {mm.add(6,3)}") 