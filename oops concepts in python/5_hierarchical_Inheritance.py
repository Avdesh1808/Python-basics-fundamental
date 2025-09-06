# This is the example of hierarchical inheritance
class A:
    def A_fun(self,name):
        self.a_name=name
        print(f"Class A :- {self.a_name}")
class B(A):
    def B_fun(self,name):
        self.b_name=name
        print(f"class B :- {self.b_name}")
class C(A):
    def C_fun(self,name):
        self.c_name=name
        print(f"class C :- {self.c_name}")
class B1(B):
    def B1_fun(self,name):
        self.b1_name=name
        print(f"class B1 :- {self.b1_name}")
class B2(B):
    def B2_fun(self,name):
        self.b2_name=name
        print(f"class B2 :- {self.b2_name}")
class C1(C):
    def C1_fun(self,name):
        self.c1_name=name
        print(f"class C1 :- {self.c1_name}")
class C2(C):
    def C2_fun(self,name):
        self.c2_name=name
        print(f"class C2 :- {self.c2_name}")
print("This is the Example of hierarchical inheritance")
a=C2()
a.C2_fun("C2")
a=C1()
a.C1_fun("C1")
a=B2()
a.B2_fun("B2")
a=B1()
a.B1_fun("B1")
a=C()
a.C_fun("C")
a=B()
a.B_fun("B")
a.A_fun("A")
 