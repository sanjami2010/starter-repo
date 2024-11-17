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
          return  round(self.__last_month_price-self.__current_month_price/100,3)
    

     #def main():
petroleum1 = Petroleum('Gasoline',3.5,3.32)
print("Product Name is ",petroleum1.getPetroleumProductName())
print("Petroleum Last Month Price is ",petroleum1.getPetroleumProductLastMonth_Price())
print("Petroleum current month price is ",petroleum1.getPetroleumProductCurrentMonthPrice())
print("Petroleum change in price is ",petroleum1.getChangePercentPrice())
print("Petroleum Product Grade is ",petroleum1.getPetroleumProductGrade())



          
    