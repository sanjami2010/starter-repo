class Square:
    def __init__(self,side=1):
        self.__side=side
    def getSide(self):
         return self.__side
    def getArea(self):
        return self.__side* self.__side
    def getPerimeter(self):
        return self.__side*4
    
    
square1 = Square()
square2=Square(5.3)
#print(square1.getSide())
print(square2.getSide())
#print(square1.getArea())
#print(square1.getPerimeter())
print(square2.getArea())
print(square2.getPerimeter())

         