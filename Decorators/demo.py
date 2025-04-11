def before (func):
    def wrap():
        print("printing before something...")
        func()
    return wrap

def after(func):
    def wrap(*a):
        func(*a)
        print("print before something....")
    return wrap

def add(func):
    def sum (*a):
        func(*a)
        sum = 0
        for i in a:
            sum+=i
        print("sum is : ",sum)
    return sum

@before
def test():
    print("testing something....")

@add
def home(a,b):
    print("Total...")

home(10,20)