#empty_set=set()
#number_set={1,2,3,4,5,6,}
#duplicate_set={1,1,1,2,2,3,5,4,6,8,96,45}
#print(f"no duplication in set{duplicate_set}")
#print(number_set)
#number_set.add(90)# use add() function to update data in sets
#number_set.add(100)
#print(number_set)
#number_set.remove(5)
#number_set.remove(6)
#print(number_set)
names1 = {  "Glory"  ,  "Tony"  ,  "Joel"  ,  "Dennis"  } 
names2 = {  "Morgan"  ,  "Joel"  ,  "Tony"  ,  "Emmanuel"  ,  "Diego"  }
names_union = names1.union(names2) #  names1 | names2 
print(names_union)
names_interasection=names1.intersection(names2)#  names1 & names2 
print(names_interasection)
names_difference=names1.difference(names2)# names1-names2
print(names_difference)
name_symetric_difference=names1.symmetric_difference(names2) # names1 ^ names2
print(name_symetric_difference)
print(set())
print(list())
print(tuple())
print(dict())