
dic={
    1:'Avdesh',
    2:'Ankit',
    3:'Amit',
    4:'Ajeet',
}
dic1={4:'Pradeep',
      5:'Sumit',
      6:'Subham'
      }
dic2 = {  "John"  : {  "Age"  :  27  ,  "Hometown"  :  "Boston"  },  "Rebecca"  :  {  "Age"  :  31  ,  "Hometown"  :  "Chicago"  }} # nested dictionary
print(dic[3])
print(dic)
print(dic.get(1))
print(dic.values())
print(dic.keys())
#dic.update(dic1)# this function is used to update() any kind of the data in dictionary
#dic.clear()# this funciton is used for empty to the dictionary
#dic.pop(3)# this function is used for pop one data from dictionary
#dic.popitem()# this function is used for opo last value from the dictionary 
del dic[2]
print(dic)
for key in dic.keys():
    print(dic[key])
print(dic2)