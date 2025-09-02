def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("Thanks for using this Function")
    return mfx
@greet
def hello():
    print("Hello world")
@greet
def add(a,b):
    print(a+b)
add(6,3)
hello()