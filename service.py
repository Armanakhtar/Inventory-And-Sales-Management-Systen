from dao import *
from  bean import *
from datetime import date


class Administrator:
    stockdao = StockDao()
    salesdao = SalesDao()
    logindao=LoginDao()
    def insertStock(self,stockobj):
        if stockobj is not None and len(stockobj.getproductName()) >= 2:
            product_id = self.stockdao.generateProductID(stockobj.getproductName())
            stockobj.setproductID(product_id)

            if self.stockdao.insertStock(stockobj) == 1:
                return product_id
            else:
                return "Data not Valid for insertion"
        else:
            return "Data not Valid for insertion"

    def deleteStock(self, ProductID):
        row=self.stockdao.deleteStock(ProductID)
        if row == 1:
            return 'deleted'
        else:
            return 'record cannot be deleted'

    def insertSales(self, salesobj):
        if salesobj == None:
            return "Object not valid for insertion"

        if self.stockdao.GetStock(salesobj.getproductID()) == None:
            return 'Unknown Product for sales'

        if self.stockdao.GetStock(salesobj.getproductID()).getquantityOnHand() < salesobj.getquantitySold():
            return "Not Enough Stock For Sales"

        current_date = date.today().strftime('%Y-%m-%d')

        if salesobj.getsalesDate() > current_date:
            return "Invalid date"

        SalesId=self.salesdao.generateSalesID(salesobj.getsalesDate())
        salesobj.setsalesID(SalesId)

        if self.salesdao.insertSales(salesobj) == 1:
            if self.stockdao.updateStock(salesobj.getproductID(),salesobj.getquantitySold()) == 1:
                return 'Sales Completed'
            else:
                return "Error"
        else:
            return "Error"

    def getSalesReport(self):
        return self.salesdao.getSalesReport()


    def stock_Details(self):
        return self.stockdao.get_Stock_Details()


    def loginAccess(self,id,pws):
        #logindao=LoginDao()
        tup=self.logindao.getLogin_data()

        if id == tup[0][0]:
            if pws == tup[0][1]:
                return 1,tup[0][2]
            else:
                return 'error',"Wrong Password"

        else:
            return 'error',"Wrong ID"

    def forgetPass(self,id,mail,mob):
        tup=self.logindao.getLogin_data()

        if id == tup[0][0]:
            if mail == tup[0][3]:
                if mob == tup[0][4]:
                    lis=[1,tup[0][2],tup[0][1]]
                    return lis
                else:
                    return "Wrong Mob No."
            else:
                return "Wrong Email"
        else:
            return "Wrong ID"

    def showShowProfile(self):
        logindao=LoginDao()
        tup=logindao.getLogin_data()
        lis=[tup[0][0],tup[0][2],tup[0][1],tup[0][4],tup[0][3]]
        return lis

    def updateProfile(self,id,name,pws,email,mob):
        tup=(id,pws,name,email,mob)
        if self.logindao.updateLogin_data(tup)==1:
            return "Done","Profile Updated"

        else:
            return "Done","Profile not Updated"