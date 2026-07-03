def summator(*v):
    x = 0
    y = 0
    for k, vy in v:
        x += k
        y += vy
    return x, y


v1 = (10, 20)
v2 = (10, 2)
v = v1 + v2
print(v)
print(type(v))
v = summator(v1, v2)
print(v)
#class Vector(object):
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        x = self.x +


    def __str__(self):
        return f'V({self.x}, {self.y})'


v1 = Vector(10, 20)
v2 = Vector(10 ,2)
print(v1, v1)
print(v1)
v = v1 + v2