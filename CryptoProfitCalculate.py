import tkinter as tk
import pandas as pd


try:
    transactions_df = pd.read_excel("CryptoProfitCalculate.xlsx")
except FileNotFoundError:
    transactions_df = pd.DataFrame(columns=['Currency', 'Buy Price', 'Sell Price', 'Amount', 'ROL', 'Profit'])

def calculate_profit():
    currency = entry_currency.get()
    Buy_price = float(entry_Buy_price.get())
    Sell_price = float(entry_Sell_price.get())
    amount = float(entry_amount.get())

     
    ROL = ((Sell_price - Buy_price) / Buy_price) * 100

   
    quantity = amount / Buy_price

     
    profit = (Sell_price * quantity) - amount

     
    if profit >= 0:
        label_ROL.config(text="ROL: {:.2f}%".format(ROL), fg='green')
        label_profit.config(text="Profit: ${:.2f}".format(profit), fg='green')
    else:
        label_ROL.config(text="ROL: {:.2f}%".format(ROL), fg='red')
        label_profit.config(text="Profit: ${:.2f}".format(profit), fg='red')

    
    transactions_df.loc[len(transactions_df)] = [currency, Buy_price, Sell_price, amount, ROL, profit]

def save_to_excel():
    transactions_df.to_excel("CryptoProfit.xlsx", index=False)
    print("Data saved to CryptoProfit.xlsx")

root = tk.Tk()
root.title("Crypto Profit Calculator")

label_currency = tk.Label(root, text="Currency:")
label_currency.grid(row=0, column=0, padx=5, pady=5)
entry_currency = tk.Entry(root)
entry_currency.grid(row=0, column=1, padx=5, pady=5)

label_Buy_price = tk.Label(root, text="Buy Price:")
label_Buy_price.grid(row=1, column=0, padx=5, pady=5)
entry_Buy_price = tk.Entry(root)
entry_Buy_price.grid(row=1, column=1, padx=5, pady=5)

label_Sell_price = tk.Label(root, text="Sell Price:")
label_Sell_price.grid(row=2, column=0, padx=5, pady=5)
entry_Sell_price = tk.Entry(root)
entry_Sell_price.grid(row=2, column=1, padx=5, pady=5)

label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=3, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=3, column=1, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate Profit", command=calculate_profit)
button_calculate.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_save_excel = tk.Button(root, text="Save to Excel", command=save_to_excel)
button_save_excel.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

label_ROL = tk.Label(root, text="")
label_ROL.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

label_profit = tk.Label(root, text="")
label_profit.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()


