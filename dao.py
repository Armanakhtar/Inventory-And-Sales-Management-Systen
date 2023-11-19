from Util import DBUtil
from bean import *

class SalesDao:
    def insertSales(self, sale):
        tup=(sale.getsalesID(),sale.getsalesDate(),sale.getproductID(),sale.getquantitySold(),sale.getsalesPricePerUnit())
        try:
            con=DBUtil.connection()
            cur=con.cursor()
            row=cur.execute("insert into tbl_sales values(%s,%s,%s,%s,%s)", tup)
            con.commit()
            con.close()

            if row > 0:
                return 1
            else:
                return 0
        except Exception:
            print(Exception,"insert")
            return 0

    def generateSalesID(self, date):
        try:
            con=DBUtil.connection()
            cur=con.cursor()
            cur.execute("select max(sales_id) from tbl_sales")
            tup = cur.fetchone()
            con.commit()
            con.close()

            if tup[0] == None:
                dates = date[2:4]
                seq = dates + "1000"
                return seq
            else:
                dates = date[2:4]
                s =str(int((tup[0])[2:])+1)
                seq = dates + s
                return seq
        except Exception:
            print(Exception)
            return 0
    def getSalesReport(self):
        try:
            con=DBUtil.connection()
            cur = con.cursor()
            cur.execute("select * from v_sales_report")
            tup = cur.fetchall()
            con.commit()
            con.close()
            lis=list()
            for i in tup:
                obj=SalesReport()
                obj.setsalesID(i[0])
                obj.setsalesDate(i[1])
                obj.setproductID(i[2])
                obj.setproductName(i[3])
                obj.setquantitySold(i[4])
                obj.setproductUnitPrice(i[5])
                obj.setsalesPricePerUnit(i[6])
                obj.setprofitAmount(i[7])
                lis.append(obj)
            return lis

        except Exception:
            return 0

class StockDao:
    def insertStock(self,obj):
        tup=(obj.getproductID(),obj.getproductName(),obj.getquantityOnHand(),obj.getproductUnitPrice(),obj.getreorderLevel())
        try:
            con = DBUtil.connection()
            cur = con.cursor()
            row=cur.execute("insert into tbl_stock values(%s,%s,%s,%s,%s)", tup)
            con.commit()
            con.close()

            if row > 0:
                return 1
            else:
                return 0

        except Exception:
            return 0

    def generateProductID(self, productName):
        try:
            cur = DBUtil.connection().cursor()
            cur.execute("select max(product_id) from tbl_stock")
            tup = cur.fetchone()
            DBUtil.connection().commit()
            DBUtil.connection().close()
            id = tup[0]
            id =str(int(id)+1)
            return id

        except Exception:
            return 0

    def updateStock(self, productID, soldQty):
        try:
            con=DBUtil.connection()
            cur = con.cursor()
            row = cur.execute("update tbl_stock set quantity_on_hand=quantity_on_hand-%s where product_id=%s",(soldQty, productID))
            con.commit()
            con.close()

            if row > 0:
                return 1
            else:
                return 0

        except Exception:
            return 0

    def GetStock(self, productID):
        try:
            con=DBUtil.connection()
            cur = con.cursor()
            cur.execute("select * from tbl_stock where product_id=%s",productID)
            tup = cur.fetchall()
            con.commit()
            con.close()

            obj=Stock()

            obj.setproductID(tup[0][0])
            obj.setproductName(tup[0][1])
            obj.setquantityOnHand(int(tup[0][2]))
            obj.setproductUnitPrice(float(tup[0][3]))
            obj.setreorderLevel(tup[0][4])
            return obj

        except Exception:
            return 0

    def deleteStock(self, productID):
        try:
            con=DBUtil.connection()
            cur=con.cursor()
            row1=cur.execute("delete from tbl_sales where product_id=%s",productID)
            row=cur.execute("delete from tbl_stock where product_id=%s",productID)
            con.commit()
            con.close()

            if row > 0 and row1 > 0:
                return 1
            else:
                return 0

        except Exception:
            return 0

    def get_Stock_Details(self):
        try:
            con=DBUtil.connection()
            cur = con.cursor()
            cur.execute("select Product_ID,Product_Name,Quantity_On_Hand from tbl_stock")
            tup = cur.fetchall()
            con.commit()
            con.close()
            return tup
        except Exception:
            return 0

class LoginDao:
    def getLogin_data(self):
        try:
            con=DBUtil.connection()
            cur =con .cursor()
            cur.execute("select * from login")
            tup = cur.fetchall()
            con.commit()
            con.close()

            return tup

        except Exception:
            tup=((0,0),)
            return tup

    def updateLogin_data(self,tup):
        try:
            con=DBUtil.connection()
            cur =con .cursor()
            row=cur.execute("update login set userid=%s,password=%s,name=%s,email=%s,mobile_no=%s;",tup)
            con.commit()
            con.close()

            if row > 0:
                return 1
            else:
                return 0

        except Exception:
            return 0