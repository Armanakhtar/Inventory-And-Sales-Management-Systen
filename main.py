from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Style,Treeview,Scrollbar
from datetime import date,datetime
import time
from bean import *
from service import *
from PIL import Image,ImageTk


win=Tk()
win.state("zoomed")
win.title("Supermarket")
win.configure(bg="pink")
win.resizable(width=False, height=True)
ico=Image.open("icon.png")
photo=ImageTk.PhotoImage(ico)
win.wm_iconphoto(False,photo)

lbl_title=Label(win,text="India Super Market",bg='pink',fg='blue',font=('arial',55,'bold','underline'))
lbl_title.place(relx=.22,rely=.0)


# it function working for show the current time and date on the screen
def cur_time():
    lbl_date.config(text=date.today().strftime('%d-%b-%Y'))
    lbl_time.config(text=time.strftime("%I:%M %p"))
    lbl_time.after(15000,cur_time)

lbl_date=Label(win,font=('arial',14,'bold'),bg='pink')
lbl_date.place(relx=.9,rely=.03)

lbl_time=Label(win,font=('arial',14,'bold'),bg='pink')
lbl_time.place(relx=.919,rely=.07)

def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(x=0,rely=.17,relwidth=1,relheight=.85)

    def login_scr():
        id=entry_liginid.get()
        pws=entry_liginpwd.get()

        admin=Administrator()
        global name
        x,name=admin.loginAccess(id,pws)
        if x==1:
            frm.destroy()
            login_screen()
        else:
            messagebox.showinfo(title=x,message=name,icon="error")
            main_screen()


    def reset_scr():
        entry_liginid.delete(0,"end")
        entry_liginpwd.delete(0,"end")
        entry_liginid.focus()


    def forgot_pass():
        frm.destroy()
        forgot_screen()

    lbl_loginid=Label(frm,text="Login ID",font=("arial",20,"bold"),bg='powder blue')
    lbl_loginid.place(relx=.23,rely=.1)

    entry_liginid=Entry(frm,font=("arial",20,"bold"),bd=6)
    entry_liginid.place(relx=.4,rely=.1)
    entry_liginid.focus()

    lbl_loginpwd=Label(frm,text="Password",font=("arial",20,"bold"),bg='powder blue')
    lbl_loginpwd.place(relx=.23,rely=.2)

    entry_liginpwd=Entry(frm,font=("arial",20,"bold"),bd=6,show="*")
    entry_liginpwd.place(relx=.4,rely=.2)

    btn_login=Button(frm,command=login_scr,text="LogIn",font=("arial",20,"bold"),bg='pink',bd=5)
    btn_login.place(relx=.4,rely=.35)

    btn_reset=Button(frm,command=reset_scr,text='Reset',font=('arial',20,'bold'),bd=5,bg='pink')
    btn_reset.place(relx=.56,rely=.35)

    btn_forgot=Button(frm,command=forgot_pass,text='Forgot Password',width=17,font=('arial',20,'bold'),bd=5,bg='pink')
    btn_forgot.place(relx=.4,rely=.5)


def forgot_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(x=0,rely=.17,relwidth=1,relheight=.85)
    lbl_title=Label(frm,text="Forgot pasword page",bg='powder blue',fg='green',font=('arial',20,'bold','underline'))
    lbl_title.pack()

    def back_screen():
        frm.destroy()
        main_screen()

    def reset_scr():
        entry_acc.delete(0,"end")
        entry_mail.delete(0,"end")
        entry_mob.delete(0,"end")
        entry_acc.focus()

    def submit():
        id=entry_liginid.get()
        mail=entry_mail.get()
        mob=entry_mob.get()

        admin=Administrator()

        if admin.forgetPass(id,mail,mob)[0]==1:
           messagebox.showinfo("Hello "+admin.forgetPass(id,mail,mob)[1],"Password- "+admin.forgetPass(id,mail,mob)[2])
           main_screen()
        else:
            messagebox.showerror("Error",admin.forgetPass(id,mail,mob))
            forgot_screen()

    Button(frm,command=back_screen,text='back',font=('arial',20,'bold'),bd=5,bg='pink').place(relx=.92,rely=0)

    Label(frm,text='Login ID',bg='powder blue',font=('arial',20,'bold')).place(relx=.25,rely=.1)

    entry_liginid=Entry(frm,width=28,font=('arial',20,'bold'),bd=5)
    entry_liginid.place(relx=.35,rely=.1)
    entry_liginid.focus()

    lbl_mail=Label(frm,text='Email',bg='powder blue',font=('arial',20,'bold')).place(relx=.25,rely=.2)
    entry_mail=Entry(frm,width=28,font=('arial',20,'bold'),bd=5)
    entry_mail.place(relx=.35,rely=.2)

    lbl_mob=Label(frm,text='Mob No',bg='powder blue',font=('arial',20,'bold')).place(relx=.25,rely=.3)
    entry_mob=Entry(frm,width=28,font=('arial',20,'bold'),bd=5)
    entry_mob.place(relx=.35,rely=.3)

    Button(frm,command=submit,text='Submit',font=('arial',20,'bold'),bd=5,bg='pink').place(relx=.4,rely=.44)
    Button(frm,command=reset_scr,text='Reset',font=('arial',22,'bold'),bd=5,bg='pink').place(relx=.559,rely=.44)



def login_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(x=0,rely=.17,relwidth=1,relheight=.85)


    # It function is working for Stock Detail show in home page
    def stoc_detail():
        ifrm1=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm1.configure(bg='white')
        ifrm1.place(relx=.797,rely=.1,relwidth=.2,relheight=.8)
        lbl_ifrmtitle.configure(text="Stocks Detail")

        tv=Treeview(ifrm1)
        tv.place(x=0,y=0,height=438,width=235)

        style = Style()
        style.configure("Treeview.Heading", font=('Arial',12,'bold'),foreground='black')

        sb=Scrollbar(ifrm1,orient='vertical',command=tv.yview)
        sb.place(relx=.93,rely=0,height=438)
        tv.configure(yscrollcommand=sb.set)

        tv['columns']=('col1','col2','col3')

        tv.column('col1',width=10,anchor='c')
        tv.column('col2',width=10,anchor='c')
        tv.column('col3',width=10,anchor='c')


        tv.heading('col1',text='P. ID')
        tv.heading('col2',text='P. Name')
        tv.heading('col3',text='Qnt')

        tv['show']='headings'
        admin=Administrator()
        cur=admin.stock_Details()
        for row in cur:
            tv.insert("","end",values=(row[0],row[1],row[2]))



    # this function is working for Insert Stock
    def insert_Stock():
        global ifrm
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.1,relwidth=.5,relheight=.5)
        lbl_title.configure(text="Insert Stock ")

        def reset_scr():
            enty_pro.delete(0,"end")
            enty_qnt.delete(0,"end")
            enty_uni.delete(0,"end")
            enty_reo.delete(0,"end")
            enty_pro.focus()

        def insert():
            flag=0
            try:
                product=(enty_pro.get()).capitalize()
                try:
                    Quantity=int(enty_qnt.get())
                    try:
                        perunit=float(enty_uni.get())
                        try:
                            reorder=int(enty_reo.get())
                            flag=1
                        except Exception:
                            messagebox.showerror("Error","Enter valid Reorder")
                    except Exception:
                        messagebox.showerror('Error','Enter valid Price per Unit')
                except Exception:
                    messagebox.showerror('Error','Enter valid Quantity')
            except Exception:
                messagebox.showerror('Error','Enter valid Product Name.')

            admin=Administrator()
            stock=Stock()

            if flag==1:
                if len(product) >= 2:
                    stock.setproductName(product)
                    if Quantity > 0:
                        stock.setquantityOnHand(Quantity)
                        if perunit > 0:
                            stock.setproductUnitPrice(perunit)
                            if reorder > 0:
                                stock.setreorderLevel(reorder)
                                messagebox.showinfo("Stock insert Detail",admin.insertStock(stock))
                                stoc_detail()
                                insert_Stock()

                            else:
                                messagebox.showerror("Error","Enter valid Reorder values")
                        else:
                            messagebox.showerror("Error","Enter valid Price per Unit")
                    else:
                         messagebox.showerror("Error","Enter valid Quantity")
                else:
                     messagebox.showerror("Error","Enter valid Product Name")


        Label(ifrm,text="Product Name",font=('',12),bg='white',fg='purple').place(relx=.005,rely=.1)
        enty_pro=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_pro.place(relx=.18,rely=.1)
        enty_pro.focus()

        Label(ifrm,text="Quantity on Hand",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.1)
        enty_qnt=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_qnt.place(relx=.69,rely=.1)

        Label(ifrm,text="Price Per Unit",font=('bold',12),bg='white',fg='purple').place(relx=.005,rely=.4)
        enty_uni=Entry(ifrm,text="Price Per Unit",font=('',12),bg='white',fg='purple',bd=5)
        enty_uni.place(relx=.18,rely=.4)

        Label(ifrm,text="Reorder Level",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.4)
        enty_reo=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_reo.place(relx=.69,rely=.4)

        Button(ifrm,command=insert,text="Submit",font=('bold',14),width=10,bg='pink',fg='purple').place(relx=.3,rely=.65)
        Button(ifrm,command=exit,text="Exit",font=('',14),width=10,bg='pink',fg='purple').place(relx=.6,rely=.65)

        reset_scr()

        enty_qnt.insert(0,0)
        enty_uni.insert(0,0)
        enty_reo.insert(0,0)



    # this function is working for Delete Stock
    def delete_Stock():
        global ifrm
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.1,relwidth=.5,relheight=.5)
        lbl_title.configure(text="Delete Stock ")

        def delete():
            id=enty_proID.get()
            admin=Administrator()
            str=admin.deleteStock(id)
            messagebox.showinfo("Done",str)
            stoc_detail()
            delete_Stock()

        Label(ifrm,text="Product ID",font=('bold',16),bg='white',fg='purple').place(relx=.35,rely=.1)
        enty_proID=Entry(ifrm,font=('bold',16),bg='white',fg='purple',bd=5)
        enty_proID.place(relx=.25,rely=.3)
        enty_proID.focus()

        Button(ifrm,command=delete,text="Submit",font=('bold',16),width=10,bg='pink',fg='purple').place(relx=.35,rely=.5)
        Button(ifrm,command=exit,text="Exit",font=('bold',16),width=10,bg='pink',fg='purple').place(relx=.35,rely=.7)



    # this function is working for Insert Sales
    def insert_Sales():
        global ifrm
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.1,relwidth=.5,relheight=.5)
        lbl_title.configure(text="Insert Sales ")

        def reset_scr():
            enty_date.delete(0,"end")
            enty_prodID.delete(0,"end")
            enty_saleQnt.delete(0,"end")
            enty_perU.delete(0,"end")
            enty_prodID.focus()


        def in_Sales():
            flag=0
            saledate=enty_date.get()
            id=enty_prodID.get()
            try:
                qnt=int(enty_saleQnt.get())
                try:
                    per=float(enty_perU.get())
                    flag=1
                except Exception:
                    messagebox.showerror("Error","Enter the valid price")
            except Exception:
                messagebox.showerror("Error","Enter the valid Quantity")

            admin=Administrator()
            sales=Sales()
            if flag==1:
                if len(saledate)>9:
                    sales.setsalesDate(saledate)
                    if len(id)>3:
                        sales.setproductID(id)
                        if qnt>0:
                            sales.setquantitySold(qnt)
                            if per>0:
                                sales.setsalesPricePerUnit(per)
                                messagebox.showinfo("Done",admin.insertSales(sales))
                                stoc_detail()
                                insert_Sales()
                            else:
                                 messagebox.showerror("Error","Enter the valid price")
                        else:
                            messagebox.showerror("Error","Enter the valid Quantity")
                    else:
                        messagebox.showerror("Error","Enter the valid product ID")
                else:
                    messagebox.showerror("Error","Enter the valid date")

        Label(ifrm,text="Enter Date",font=('',12),bg='white',fg='purple').place(relx=.005,rely=.1)
        enty_date=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_date.place(relx=.18,rely=.1)

        Label(ifrm,text="Product ID",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.1)
        enty_prodID=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_prodID.place(relx=.69,rely=.1)
        enty_prodID.focus()

        Label(ifrm,text="Quantity Sold",font=('bold',12),bg='white',fg='purple').place(relx=.005,rely=.4)
        enty_saleQnt=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_saleQnt.place(relx=.18,rely=.4)

        Label(ifrm,text="Price per Unit",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.4)
        enty_perU=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        enty_perU.place(relx=.69,rely=.4)

        Button(ifrm,command=in_Sales,text="Submit",font=('bold',14),width=10,bg='pink',fg='purple').place(relx=.3,rely=.65)
        Button(ifrm,command=exit,text="Exit",font=('',14),width=10,bg='pink',fg='purple').place(relx=.6,rely=.65)

        reset_scr()

        enty_date.insert(0,date.today())
        enty_saleQnt.insert(0,0)
        enty_perU.insert(0,0)

     # this function is working for  view Sales report
    def sales_report():
        global ifrm
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.1,relwidth=.5,relheight=.8)
        lbl_title.configure(text="View Sales Report ")


        tv=Treeview(ifrm)
        tv.place(x=0,y=0,height=438,width=630)

        style = Style()
        style.configure("Treeview.Heading", font=('Arial',10,'bold'),foreground='black')

        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(relx=.973,rely=.05,height=415)
        tv.configure(yscrollcommand=sb.set)

        tv['columns']=('col1','col2','col3','col4','col5','col6','col7','col8')

        tv.column('col1',width=10,anchor='c')
        tv.column('col2',width=10,anchor='c')
        tv.column('col3',width=10,anchor='c')
        tv.column('col4',width=10,anchor='c')
        tv.column('col5',width=10,anchor='c')
        tv.column('col6',width=10,anchor='c')
        tv.column('col7',width=10,anchor='c')
        tv.column('col8',width=10,anchor='c')


        tv.heading('col1',text='SalesID')
        tv.heading('col2',text='SaleDate')
        tv.heading('col3',text='Pro.ID')
        tv.heading('col4',text='Pro.Name')
        tv.heading('col5',text='Sold QTY')
        tv.heading('col6',text='Pro.rice')
        tv.heading('col7',text='SalePrice')
        tv.heading('col8',text='Profit')

        tv['show']='headings'
        admin=Administrator()
        objlis=admin.getSalesReport()
        for obj in objlis:
            tv.insert("","end",values=(
                        obj.getsalesID(),
                        obj.getsalesDate(),
                        obj.getproductID(),
                        obj.getproductName(),
                        obj.getquantitySold(),
                        obj.getproductUnitPrice(),
                        obj.getsalesPricePerUnit(),
                        obj.getprofitAmount()))

        Button(ifrm,command=exit,text="x",font=('',9),width=1,height=1,bg='red',fg='white').place(relx=.973,rely=0)

    # this function is working for Update Profile
    def update_profile():
        global ifrm
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.1,relwidth=.5,relheight=.5)
        lbl_title.configure(text="Update Profile ")

        admin=Administrator()
        def update_profile_afterlogin():
            id=entry_id.get()
            name=entry_name.get()
            pws=entry_pass.get()
            email=entry_email.get()
            mob=entry_mob.get()

            lis=list(admin.updateProfile(id,name,pws,email,mob))
            messagebox.showinfo(lis[0],lis[1])
            if "Profile Updated"==lis[1]:
                lbl_titlename.configure(text=("Welcome, "+name))

            update_profile()


        Label(ifrm,text="User ID",font=('',12),bg='white',fg='purple').place(relx=.005,rely=.1)
        entry_id=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        entry_id.place(relx=.18,rely=.1)
        entry_id.focus()

        Label(ifrm,text="User Name",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.1)
        entry_name=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        entry_name.place(relx=.69,rely=.1)

        Label(ifrm,text="Password",font=('bold',12),bg='white',fg='purple').place(relx=.005,rely=.4)
        entry_pass=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5,show="*")
        entry_pass.place(relx=.18,rely=.4)

        Label(ifrm,text="Mobile no.",font=('bold',12),bg='white',fg='purple').place(relx=.49,rely=.4)
        entry_mob=Entry(ifrm,font=('',12),bg='white',fg='purple',bd=5)
        entry_mob.place(relx=.69,rely=.4)

        Label(ifrm,text="Email",font=('bold',12),bg='white',fg='purple').place(relx=.005,rely=.7)
        entry_email=Entry(ifrm,font=('',12),width=30,bg='white',fg='purple',bd=5)
        entry_email.place(relx=.18,rely=.7)

        Button(ifrm,command=update_profile_afterlogin,text="Update",font=('bold',14),width=10,bg='pink',fg='purple').place(relx=.7,rely=.7)
        Button(ifrm,command=exit,text="x",font=('',9),width=1,height=1,bg='red',fg='white').place(relx=.973,rely=0)

        row=admin.showShowProfile()
        entry_id.insert(0,row[0])
        entry_name.insert(0,row[1])
        entry_pass.insert(0,row[2])
        entry_mob.insert(0,row[3])
        entry_email.insert(0,row[4])


    def insert_St():
        try:
            ifrm.destroy()
            insert_Stock()
        except Exception:
            insert_Stock()

    def delete_St():
        try:
            ifrm.destroy()
            delete_Stock()
        except Exception:
            delete_Stock()

    def insert_Sal():
        try:
            ifrm.destroy()
            insert_Sales()
        except Exception:
            insert_Sales()

    def sales_re():
        try:
            ifrm.destroy()
            sales_report()
        except Exception:
            sales_report()

    def update_p():
        try:
            ifrm.destroy()
            update_profile()
        except Exception:
            update_profile()

    def exit():
        ifrm.destroy()
        login_screen()

    def logout_screen():
        frm.destroy()
        main_screen()


    global lbl_titlename
    lbl_titlename=Label(frm,text=("Welcome, "+name),bg='powder blue',fg='green',font=('arial',20,'bold'))
    lbl_titlename.place(relx=0,rely=0)

    lbl_ifrmtitle=Label(frm,bg='powder blue',fg='green',font=('arial',18,'bold','underline'))
    lbl_ifrmtitle.place(relx=.845,rely=.035)


    lbl_title=Label(frm,text="Home Page",bg='powder blue',fg='green',font=('arial',22,'bold','underline'))
    lbl_title.pack()


    # After the login
    #It is options: 1 Insert Stock, 2 Delete Stock, 3 Insert Sales, 4 Update Profile, and 5 Log Out:-

    #It is Insert Stock Button
    Button(frm,command=insert_St,text='Insert Stock',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.1)

    #It is Delet Stock Button
    Button(frm,command=delete_St,text='Delete Stock',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.23)

    #It is Insert Sales Button
    Button(frm,command=insert_Sal,text='Insert Sales',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.36)

    #It is View Sales Report Button
    Button(frm,command=sales_re,text='View Sales Report',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.49)

    #It is Update Profile Button
    Button(frm,command=update_p,text='Update Profile',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.62)

    #It is Logout Button
    Button(frm,command=logout_screen,text='Logout',width=15,font=('arial',20,'bold'),bd=5,bg='pink').place(relx=0,rely=.75)

    # Call the stock_detail for show the Stocks in home page
    stoc_detail()






if __name__ == "__main__":
    main_screen()
    cur_time()
    win.mainloop()