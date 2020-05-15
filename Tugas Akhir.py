from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *
import time
import datetime

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Mata Uang")
        master.geometry("1000x300+0+0")
        master.configure(background='black')
        master.LeftMainFrame = Frame(root, width=660, height=400, bd=8, relief="raise")
        master.LeftMainFrame.pack(side=LEFT)
        master.RightMainFrame = Frame(root, width=200, height=400, bd=8, relief="raise")
        master.RightMainFrame.pack(side=RIGHT)

        self.value0 = StringVar()
        self.value1 = StringVar()
        self.convert = DoubleVar()
        self.currency = DoubleVar()
        self.DateofOrder = StringVar()
        self.time = self.DateofOrder.set(time.strftime("%d/%m/%Y"))

        self.entry = Entry(master.LeftMainFrame, font=('arial',20,'bold'), textvariable=self.convert, bd=2, width=28, justify='center')
        self.entry.grid(row=0, column=1)

        self.box= ttk.Combobox(master.LeftMainFrame, textvariable=self.value0, state='readonly', font=('arial',20,'bold'), width=20)
        self.box['values']= ('','Brazil','Kanada','Euro','India','Indonesia','Singapura','Filipina','Inggris','Malaysia','USA')
        self.box.current(0)
        self.box.grid(row=4, column=2)

        self.box1= ttk.Combobox(master.LeftMainFrame, textvariable=self.value1, state='readonly', font=('arial',20,'bold'), width=20)
        self.box1['values']= ('','USA','Inggris')
        self.box1.current(0)
        self.box1.grid(row=0, column=2)


        self.label1 = Label(master.LeftMainFrame, textvariable=self.currency,bd=2,width=25,bg='white',padx=2,pady=2,relief='sunken',font=('arial',20,'bold'))
        self.label1.grid(row=4,column=1)

        self.label2 = Label(master.RightMainFrame,font=('arial',20,'bold'),textvariable=self.DateofOrder,bd=2,width=12,fg="black",padx=2,pady=2,justify='center')
        self.label2.grid(row=0,column=0,sticky=W)


        self.con_button = Button(master.RightMainFrame, text="Convert", command=self.ConCurrency, padx=2, pady=2, bd=2, fg='black', font=('arial',20,'bold'), width=12, height=1)
        self.con_button.grid(row=1,column=0)

        self.res_button = Button(master.RightMainFrame, text="Reset", command=self.Reset, padx=2, pady=2, bd=2, fg='black', font=('arial',20,'bold'), width=12, height=1)
        self.res_button.grid(row=2,column=0)

        self.quit_button = Button(master.RightMainFrame, text="Exit", command=self.qExit, padx=2, pady=2, bd=2, fg='black', font=('arial',20,'bold'), width=12, height=1)
        self.quit_button.grid(row=3,column=0)


    def ConCurrency(self):
        if self.value1.get()=="USA" and self.value0.get()=="Inggris":
            convert1 = float(self.convert.get()* 0.80)
            convert2 = "British Pound", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="India":
            convert1 = float(self.convert.get()* 75.83)
            convert2 = "Indian Rupee", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Brazil":
            convert1 = float(self.convert.get()* 5.49)
            convert2 = "Brazilian Real", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Kanada":
            convert1 = float(self.convert.get()* 1.43)
            convert2 = "Canadian Dollar", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Malaysia":
            convert1 = float(self.convert.get()* 4.30)
            convert2 = "Malaysian Ringgit", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Filipina":
            convert1 = float(self.convert.get()* 50.57)
            convert2 = "Philippine Peso", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Indonesia":
            convert1 = float(self.convert.get()* 14678)
            convert2 = "Indonesian Rupiah", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Singapura":
            convert1 = float(self.convert.get()* 1.42)
            convert2 = "Singaporean Dollar", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="USA" and self.value0.get()=="Euro":
            convert1 = float(self.convert.get()* 0.90)
            convert2 = "Euro", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="India":
            convert1 = float(self.convert.get()* 92.36)
            convert2 = "Indian Rupee", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Brazil":
            convert1 = float(self.convert.get()* 7.09)
            convert2 = "Brazilian Real", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Kanada":
            convert1 = float(self.convert.get()* 1.71)
            convert2 = "Canadian Dollar", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Malaysia":
            convert1 = float(self.convert.get()* 5.31)
            convert2 = "Malaysian Ringgit", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Filipina":
            convert1 = float(self.convert.get()* 61.79)
            convert2 = "Philippine Peso", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Indonesia":
            convert1 = float(self.convert.get()* 18182)
            convert2 = "Indonesian Rupiah", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Singapura":
            convert1 = float(self.convert.get()* 1.74)
            convert2 = "Singaporean Dollar", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="Euro":
            convert1 = float(self.convert.get()* 1.13)
            convert2 = "Euro", str('%.2f'%(convert1))
            self.currency.set(convert2)
        elif self.value1.get()=="Inggris" and self.value0.get()=="USA":
            convert1 = float(self.convert.get()* 1.22)
            convert2 = "USA Dollar", str('%.2f'%(convert1))
            self.currency.set(convert2)

    def qExit(self):
        qExit= messagebox.askyesno("Alert!!!","Are you going to leaving the program?")
        if qExit > 0:
            "true"
        while "true":
            root.destroy()
            return
        

    def Reset(self):
        self.value0.set("")
        self.convert.set("0.0")
        self.currency.set("0.0")

root = Tk()
MyFirstGUI(root)
root.mainloop()
