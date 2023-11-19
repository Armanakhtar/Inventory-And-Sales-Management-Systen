from datetime import date

class Stock:
    def __init__(self):
        self.__productID=""
        self.__productName=""
        self.__quantityOnHand=0
        self.__productUnitPrice=0.0
        self.__reorderLevel=0
    def getproductID(self):
        return self.__productID
    def setproductID(self, id):
        self.__productID = id

    def getproductName(self):
        return self.__productName
    def setproductName(self, name):
        self.__productName = name

    def getquantityOnHand(self):
        return self.__quantityOnHand
    def setquantityOnHand(self, onhand):
        self.__quantityOnHand = onhand

    def getproductUnitPrice(self):
        return self.__productUnitPrice
    def setproductUnitPrice(self,price):
        self.__productUnitPrice = price

    def getreorderLevel(self):
        return self.__reorderLevel
    def setreorderLevel(self, level):
        self.__reorderLevel = level

#it is asales class start:

class Sales:
    def __init__(self):
        self.__salesID=""
        self.__salesDate=date
        self.__productID=""
        self.__quantitySold=0
        self.__salesPricePerUnit=0.0

    def getsalesID(self):
        return self.__salesID
    def setsalesID(self, saleid):
        self.__salesID = saleid

    def getsalesDate(self):
        return self.__salesDate
    def setsalesDate(self, saleDate):
        self.__salesDate = saleDate

    def getproductID(self):
        return self.__productID
    def setproductID(self, id):
        self.__productID = id

    def getquantitySold(self):
        return self.__quantitySold
    def setquantitySold(self, sold):
        self.__quantitySold = sold

    def getsalesPricePerUnit(self):
        return self.__salesPricePerUnit
    def setsalesPricePerUnit(self,unit):
        self.__salesPricePerUnit = unit

# it's a SalesReport class start:

class SalesReport:
    def __init__(self):
        self.__salesID=""
        self.__salesDate=""
        self.__productID=""
        self.__productName=""
        self.__quantitySold=0
        self.__productUnitPrice=0.0
        self.__salesPricePerUnit=0.0
        self.__profitAmount=0.0

    def getsalesID(self):
        return self.__salesID
    def setsalesID(self,id):
        self.__salesID = id

    def getsalesDate(self):
        return self.__salesDate
    def setsalesDate(self,date):
        self.__salesDate = date

    def getproductID(self):
        return self.__productID
    def setproductID(self,id):
        self.__productID = id

    def getproductName(self):
        return self.__productName
    def setproductName(self,name):
        self.__productName = name

    def getquantitySold(self):
        return self.__quantitySold
    def setquantitySold(self,sold):
        self.__quantitySold = sold

    def getproductUnitPrice(self):
        return self.__productUnitPrice
    def setproductUnitPrice(self,price):
        self.__productUnitPrice = price

    def getsalesPricePerUnit(self):
        return self.__salesPricePerUnit
    def setsalesPricePerUnit(self,unit):
        self.__salesPricePerUnit = unit

    def getprofitAmount(self):
        return self.__profitAmount
    def setprofitAmount(self,amount):
        self.__profitAmount = amount
