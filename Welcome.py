"""
Note : Before start should read Readme File.

"""

import tkinter as tk                     
from tkinter import ttk 
from OrderBook import *
from see_transaction_gui import *
root = tk.Tk() 
root.title("Order Book") 
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl) 

  
tabControl.add(tab1, text ='Market Order') 
tabControl.add(tab2, text ='Limit Order') 
tabControl.add(tab3, text ='StopLoss Order')
tabControl.add(tab4, text ='All Transaction') 
tabControl.pack(expand = 1, fill ="both") 


orders_class=orderbook()
trasaction=transaction_gui()

orders_class.Market(tab1)
orders_class.Limit(tab2)
orders_class.StopLoss(tab3)

trasaction.make_gui(tab4)

root.geometry("500x200")
root.mainloop()   
