fruits = [  'apple'  ,  'banana'  ,  'cherry'  ]
#pops_fruits=fruits.pop(1)
#print(fruits)
#fruits.append('Avdesh') 
#fruits.insert(1,'peas')# we can use insert when we have to add or update any type of data in list
#fruits.remove('Avdesh')# with the help of this function we can remove any specific date from the list which we have already created
last_fruit=fruits.pop()# we can use this function for pop a last data from the list
#print(fruits)
#print(last_fruit)
#print(pops_fruits)
#print(fruits)
fruits.append(['Tea','Papaya'])
print(fruits)
copy_fruits=fruits.copy()
copy_fruits[2][0]=55
copy_fruits[2][1]=100
copy_fruits[1]=200
print(copy_fruits[0])
print(copy_fruits)