import sys

class Slotted:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = Slotted(1,2)
print(obj)
print(sys.getsizeof(obj))
# print(sys.getsizeof(obj.__dict__))