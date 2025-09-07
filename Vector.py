import math
class vector2D:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return  f" ({self.x} , {self.y}) "
        
    
    def __add__ (self,other):
        return vector2D(self.x + other.x ,self.y +other.y)
    
    
    def __sub__ (self,other):
        return vector2D (self.x - other.x ,self.y -other.y)
    
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    
    def direction (self):
        return math.degrees(math.atan2(self.y,self.x ))
    
    
    def __mul__ (self,value):
        return (self.x*value , self.y*value)
    
    
    def __dot__ (self,other):
        return (self.x * other.x + self.y * other.y)
    
    
        
 
 
    
    