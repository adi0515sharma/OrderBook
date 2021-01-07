import tkinter
from tkinter import * 
from databaseConnect import *

submitrequest=SubmitRequest()

class orderbook:
    
    def Market(self,top):
        comapny=Label(top, text = "Name of company :")
        company_name = Entry(top) 
        l1 = Label(top, text = "Number of share :",width=30) 
        l2 = Label(top, text = "Buy Or Sell:")
        e1 = Entry(top) 
        e2 = Entry(top)
        b1=Button(top, bg="yellow" ,text ="place order" ,command=lambda:  submitrequest.requestForMarketOrder(company_name.get(),e1.get(),e2.get()))
        
        l1.grid(row=1,column=0)
        e1.grid(row=1,column=1)
        l2.grid(row=2,column=0)
        e2.grid(row=2,column=1)
        b1.grid(row=3,column=0)
        comapny.grid(row=0,column=0)
        company_name.grid(row=0,column=1)
        
        
    def StopLoss(self,top):
        
        
        comapny=Label(top, text = "Name of company :")
        company_name = Entry(top) 
        
        l1 = Label(top, text = "Number of share :",width=30) 
        l2 = Label(top, text = "Buy Or Sell:")
        l3 = Label(top, text = "Price:")
        l4 = Label(top, text = "End Price:")

        e1 = Entry(top) 
        e2 = Entry(top)
        e3 = Entry(top)
        e4 = Entry(top)
        
        b1=Button(top,bg="yellow" ,text ="place order",command=lambda:  submitrequest.requestForStopOrder(company_name.get(),e1.get(),e3.get(),e4.get(),e2.get()))

        l1.grid(row=1,column=0)
        e1.grid(row=1,column=1)
        l2.grid(row=2,column=0)
        e2.grid(row=2,column=1)
        l3.grid(row=3,column=0)
        e3.grid(row=3,column=1)
        l4.grid(row=4,column=0)
        e4.grid(row=4,column=1)
        b1.grid(row=5,column=0)
        comapny.grid(row=0,column=0)
        company_name.grid(row=0,column=1)
        
        
        
    def Limit(self,top):
        
        comapny=Label(top, text = "Name of company :") 
        l1 = Label(top, text = "Number of share :", width=30) 
        l2 = Label(top, text = "Buy Or Sell:")
        l3 = Label(top, text = "Price:")

        company_name = Entry(top)
        e1 = Entry(top) 
        e2 = Entry(top)
        e3 = Entry(top)
        b1=Button(top, bg="yellow" ,text ="place order" ,command=lambda: submitrequest.requestForLimitOrder(company_name.get(),e1.get(),e3.get(),e2.get()))
        company_name.grid(row=4,column=1)
        l1.grid(row=1,column=0)
        e1.grid(row=1,column=1)
        l2.grid(row=2,column=0)
        e2.grid(row=2,column=1)
        l3.grid(row=3,column=0)
        e3.grid(row=3,column=1)
        b1.grid(row=4,column=0)
        comapny.grid(row=0,column=0)
        company_name.grid(row=0,column=1)
       
        
        
