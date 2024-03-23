class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x + self.y > other.x + other.y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError
        
pt_1 = Point(1, 2)
pt_2 = Point(3, 4)
pt_3 = Point(5, 6)

sum_of_pts = pt_1 + pt_2

print(sum_of_pts > pt_3)