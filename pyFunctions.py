def add(x, y):
    print("x is {} and y is {}".format(x,y))
    return x + y

add(5, 3)

def create_adder(x):
    def adder(y):
        print(x + y)
        return x + y
    return adder
    
adder_of_10 = create_adder(10)
adder_of_10(3)

a = lambda x, y: x + y
print(a(2, 3))