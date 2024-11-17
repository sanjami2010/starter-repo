class Petroleum:
    def __init__(self,name,last_month_price,current_month_price,grade='Octane'):
                 self.__name=name
                 self.__last_month_price=last_month_price
                 self.__current_month_price=current_month_price
                 self.__grade=grade
    def getPetroleumProductName(self):
        return self.__name
    def getPetroleumProductGrade(self):
        return self.__grade
    def getPetroleumProductLastMonth_Price(self):
        return self.__last_month_price
    def setPetroleumProductLastMonthPrice(self,last_month_price):
          self.__last_month_price=last_month_price
    def getPetroleumProductCurrentMonthPrice(self):
          return self.__current_month_price
    def setPetroleumProductCurrentMonthPrice(self,current_month_price):
          self.__current_month_price=current_month_price
    def getChangePercentPrice(self):
          return ( self.__last_month_price-self.__current_month_price)/100
    

     #def main():
petroleum1 = Petroleum('Gasoline',3.5,3.32)
print(petroleum1.getPetroleumProductName())
print(petroleum1.getPetroleumProductLastMonth_Price())
print(petroleum1.getPetroleumProductCurrentMonthPrice())
print(petroleum1.getChangePercentPrice())
print(petroleum1.getPetroleumProductGrade())



          
    