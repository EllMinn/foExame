
import tkinter as tk 
from tkinter import *
import tkinter.messagebox
import datetime
import pandas as pd



root = tk.Tk()
 
root.title("Конвертер по основной валюте евро")
 
Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Конвертер по основной валюте евро ',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
 
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("валюта")
variable2.set("валюта")
#Function To For Real Time Currency Conversion
 
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 1, 17)
    dataset = pd.date_range(start='1/1/2018', end='1/17/2023')
    #print(dataset)
    df_data = pd.DataFrame() 
    df_carr = pd.DataFrame() 
    df_valuem = pd.DataFrame() 


    df = pd.DataFrame()
    

   
    from_currency = variable1.get()
    to_currency = variable2.get()
 
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Сумма не найдена.\n Введите сумму.")
 
    elif (from_currency == "валюта" or to_currency == "валюта"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Валюта не указана.\n Введите конвертируемые валюты.")
 
    else:
    
#///////////////////////////////////////////////////////
        for val in dataset:
            new_amt=  c.get_rate(from_currency, to_currency, val)
            new_amount = float("{:.6f}".format(new_amt))
            print(new_amount)
            new_row = {'Валюта':from_currency, 'Дата':val, 'Значение':new_amount}
            df = df.append(new_row, ignore_index=True)

        exportToExel(df,from_currency)
        #date_obj = datetime.datetime(2023, 1, 16)
        #new_amt=  c.get_rate(from_currency, to_currency, date_obj)
#///////////////////////////////////////////////////////

        #new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        #new_amount = float("{:.6f}".format(new_amt))
        #Amount2_field.insert(0, str(new_amount))
 

def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

def exportToExel(df,from_currency):

    df.to_excel('C:\qwerty\kurs_'+ from_currency + '.xlsx')
 
CurrenyCode_list = ["USD", "GBP", "RUB", "EUR"]
 
root.configure(background='#e6e5e5')
root.geometry("700x400")
 
Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Сумма  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    ИЗ  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    В  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Сумма конвертации  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Сформировать  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Очистить  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()