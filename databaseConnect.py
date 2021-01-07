import mysql.connector
import tkinter
from tkinter import messagebox


class SubmitRequest:
    def __init__(self):
        
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="internshipproject"
        )
        self.mycursor = self.mydb.cursor()
        
    def countget(self):
        sql = "select * from order_by_customer ORDER BY date DESC;"
        self.mycursor.execute(sql)
        size=self.mycursor.fetchall()
        self.count = len(size)+1
        return size

    def requestForMarketOrder(self,company,number_of_share,buy_or_sell):
        self.countget()
        if(company=="" or number_of_share=="" or buy_or_sell==""):
            messagebox.showerror(title="error", message="Please Enter All field")
            return
        elif(buy_or_sell!="buy" and buy_or_sell!="sell"):
            messagebox.showerror(title="error", message="incorrect buy_or_sell value")
            return
        print(number_of_share," ",buy_or_sell)
        self.sql = "INSERT INTO order_by_customer (company,id,no_of_share, action) VALUES (%s,%s,%s, %s)"
        self.val = (company,self.count,number_of_share, buy_or_sell)
        self.mycursor.execute(self.sql,self.val)
        self.marketOrder_trigger(number_of_share,buy_or_sell,company)
        

    def requestForLimitOrder(self,company,number_of_share,price,buy_or_sell):
        self.countget()
        if(company=="" or number_of_share=="" or buy_or_sell=="" or price==""):
            messagebox.showerror(title="error", message="Please Enter All field")
            return
        elif(buy_or_sell!="buy" and buy_or_sell!="sell"):
            messagebox.showerror(title="error", message="incorrect buy_or_sell value")
            return
        
        self.sql = "INSERT INTO order_by_customer (company,id,no_of_share, action, price) VALUES (%s,%s,%s, %s, %s)"
        self.val = (company,self.count,number_of_share, buy_or_sell, price)
        self.mycursor.execute(self.sql,self.val)
        self.limitOrder_trigger(number_of_share,buy_or_sell,price,company)
        

    def requestForStopOrder(self,company,number_of_share,price,stop_loss,buy_or_sell):
        self.countget()
        if(company=="" or number_of_share=="" or buy_or_sell=="" or price=="" or stop_loss==""):
            messagebox.showerror(title="error", message="Please Enter All field")
            return
        elif(buy_or_sell!="buy" and buy_or_sell!="sell"):
            messagebox.showerror(title="error", message="incorrect buy_or_sell value")
            return
        
        self.sql = "INSERT INTO order_by_customer (company,id,no_of_share, action,price, stop_loss) VALUES (%s,%s,%s, %s, %s, %s)"
        self.val = (company,self.count,number_of_share, buy_or_sell,price,stop_loss)
        self.mycursor.execute(self.sql,self.val)
        self.stopOrder_trigger(number_of_share,price,stop_loss,buy_or_sell,company)
        

    def marketOrder_trigger(self,quantity,order_for_what,company):
        qrystr=""
        trigger_name="order"+str(self.count)
        if order_for_what=="buy":
            qrystr = f"CREATE DEFINER=`root`@`localhost` TRIGGER {trigger_name} AFTER INSERT ON `company` FOR EACH ROW UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"'"
        elif order_for_what=="sell":
            qrystr = f"CREATE DEFINER=`root`@`localhost` TRIGGER {trigger_name} AFTER INSERT ON `company` FOR EACH ROW UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"'"
        self.mycursor.execute(qrystr)
        
        messagebox.showinfo(title="message", message="Record Submitted Successfully")

    def limitOrder_trigger(self,quantity,order_for_what,price,company):
        qrystr=""
        trigger_name="order"+str(self.count)
        if order_for_what=="buy":
            qrystr = f"CREATE TRIGGER {trigger_name} AFTER INSERT ON company FOR EACH ROW BEGIN IF NEW.price = {int(price)} THEN UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"';END IF;END;"
        elif order_for_what=="sell":
            qrystr = f"CREATE TRIGGER {trigger_name} AFTER INSERT ON company FOR EACH ROW BEGIN IF NEW.price = {int(price)} THEN UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"';END IF;END;"
        self.mycursor.execute(qrystr)
    
        messagebox.showinfo(title="message", message="Record Submitted Successfully")
    
    
    def stopOrder_trigger(self,quantity,price,stop_loss,order_for_what,company):
        qrystr=""
        trigger_name="order"+str(self.count)
        if order_for_what=="buy":
            qrystr = f"CREATE TRIGGER {trigger_name} AFTER INSERT ON company FOR EACH ROW BEGIN IF NEW.price >= {int(price)} AND NEW.price <= {int(stop_loss)}  THEN UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"';END IF;END;"
        elif order_for_what=="sell":
            qrystr = f"CREATE TRIGGER {trigger_name} AFTER INSERT ON company FOR EACH ROW BEGIN IF NEW.price <= {int(price)} AND NEW.price >= {int(stop_loss)}  THEN UPDATE order_by_customer SET status='sucessfull' WHERE no_of_share={int(quantity)} AND company='"+str(company)+"';END IF;END;"
        self.mycursor.execute(qrystr)
        
        messagebox.showinfo(title="message", message="Record Submitted Successfully")
        

    
    def deleteTran(self,name,id):
        sql=f"DROP TRIGGER IF EXISTS {name}"
        self.mycursor.execute(sql)