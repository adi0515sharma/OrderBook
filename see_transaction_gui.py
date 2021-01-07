from tkinter import *
from databaseConnect import *

class transaction_gui:
    
    def make_gui(self,root):
        canvas = Canvas(root,width=200, height=200)
        canvas.grid(column=0, row=0, sticky=N+S+E+W)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        vscrollbar = Scrollbar(root)
        vscrollbar.grid(column=1, row=0, sticky=N+S)
        
        canvas.config(yscrollcommand=vscrollbar.set)
        vscrollbar.config(command=canvas.yview)
        self.f = Frame(canvas, borderwidth = 1)
        self.fetch_display()
        canvas.create_window((0,0), anchor=NW, window=self.f)
        self.f.update_idletasks() 
        canvas.config(scrollregion= self.f.bbox("all")  )

    def fetch_display(self,action="all trans"):
        
        for widget in self.f.winfo_children():
            widget.destroy()
        submitrequest=SubmitRequest()
        result=submitrequest.countget()
        Label(self.f,text="Action", width=10,fg="red",bg="white").grid(row=0,column=0)
        Label(self.f,text="company", width=10,fg="red",bg="white").grid(row=0,column=1)   
        Label(self.f,text="No Of Share", width=10,fg="red",bg="white").grid(row=0,column=2)   
        Label(self.f,text="price" ,width=10,fg="red",bg="white").grid(row=0,column=3)   
        Label(self.f,text="status" ,width=10,fg="red",bg="white").grid(row=0,column=4)   
        Label(self.f,text="stop_loss" ,width=10,fg="red",bg="white").grid(row=0,column=5)   
        Label(self.f,text="id", width=10,fg="red",bg="white").grid(row=0,column=6)
        Label(self.f,text="date", width=10,fg="red",bg="white").grid(row=0,column=7)

        index=0
        if(len(result)>=1):
            if action=="all trans":
            
                for i in range(1,len(result)+1):
                    for j in range(0,len(result[i-1])):
                        Label(self.f,text=result[i-1][j],width=10).grid(row=i,column=j)  
                index=i
            elif action=="all buy":
            
                for i in range(1,len(result)+1):
                    if(result[i-1][0]=="buy"):
                        for j in range(0,len(result[i-1])):
                            Label(self.f,text=result[i-1][j],width=10).grid(row=i,column=j)
                index=i

            elif action=="all sale":
            
                for i in range(1,len(result)+1):
                    if(result[i-1][0]=="sell"):
                        for j in range(0,len(result[i-1])):
                            Label(self.f,text=result[i-1][j],width=10).grid(row=i,column=j)
                index=i

            Button(self.f,text="Referesh", width=10,fg="red",bg="white",command=lambda: self.fetch_display()).grid(row=index+1,column=0)
            Button(self.f,text="All Transaction", width=10,fg="red",bg="white",command=lambda: self.fetch_display(action="all trans")).grid(row=index+1,column=1)
            Button(self.f,text="All Buys", width=10,fg="red",bg="white",command=lambda: self.fetch_display(action="all buy")).grid(row=index+1,column=2)
            Button(self.f,text="All Sales", width=10,fg="red",bg="white",command=lambda: self.fetch_display(action="all sale")).grid(row=index+1,column=3)
            
        else:
            Button(self.f,text="Referesh", width=10,fg="red",bg="white",command=lambda: self.fetch_display()).grid(row=1,column=0)
 