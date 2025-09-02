fruits = [  'apple'  ,  'banana'  ,  'cherry', 1 , 2 , 3 , 1 , 1 ]
print(fruits)
fruits.append('guava') # add data in end of the list we can also add list using appen() function
fruits.extend(['pomigranate','mango'])# add more than one data in listprint(fruits)
fruits.reverse()
print(fruits)
print(fruits.count(1))
print(fruits.index('cherry'))
m = fruits.copy()
print(m)
fruits.insert(2,'Avdesh')# to update data in list on indexing 
print(fruits)
l = [990,160,660]
fruits.extend(l)
print(fruits)
print(fruits+m)
