class employes:
    def __init__(self,name,id,city): # this is intiral constructor use for intialize and create objects in instance of class and it is also called permeterize constructor
        self.em_Name = name
        self.em_id = id
        self.em_cityname = city

    def em_info(self):
        print(f"{self.em_Name},{self.em_id},{self.em_cityname}")
    
a=employes("Avdesh",2316,"Noida")
b=employes("Amit",2626,"Nehru Place")
c=employes(2,3,2)
a.em_info()
b.em_info()
c.em_info()

# it is the example of default constructor when we use without perameter in __init__ function
def __init__(self):
    print("Hello world ")

