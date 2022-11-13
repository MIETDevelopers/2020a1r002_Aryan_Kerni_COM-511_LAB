'''Example 1: Define a class that can add and subtract two numbers.
Following the syntax above, we shall decide on the name to give our class. Then in the class
body, we shall define two methods namely i.e. add and subtract. Each of these methods will
implement the operation for addition and subtraction respectively.'''
class add_sub:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# define 'add' method
    def add(self):
        return self.x + self.y
# define 'subtract' method
    def subtract(self):
        return self.x - self.y
if __name__ == '__main__':
    x = 10
    y = 6
# create an instance
    opp = add_sub(x,y)
# call add method
    print(f'{x} + {y} = {opp.add()}')
#print(opp.add())
# call subtract method
    print(f'{x} - {y} = {opp.subtract()}')
    

'''Example 2: Define class and instance attributes'''
class Cylinder:
# class attribute
    pi = 3.14
    def __init__(self, radius, height):
    # instance variables
        self.radius = radius
        self.height = height
if __name__ == '__main__':
        c1 = Cylinder(4, 20)
        c2 = Cylinder(10, 50)
        print(f'Pi for c1:{c1.pi} and c2:{c2.pi}')
        print(f'Radius for c1:{c1.radius} and c2:{c2.radius}')
        print(f'Height for c1:{c1.height} and c2:{c2.height}')
        print(f'Pi for both c1 and c2 is: {Cylinder.pi}')