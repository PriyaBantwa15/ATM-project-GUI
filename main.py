import tkinter as tk
import tkinter.messagebox as messagebox

class ATM:
    def __init__(self):
        self.balance = 10000
        self.transactions = []
        self.last_transactions = []
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.transactions.append(-amount)
            self.last_transactions.append(-amount)
            if len(self.last_transactions) > 5:
                self.last_transactions.pop(0)
            return "Withdrawal successful"
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)
        self.last_transactions.append(amount)
        if len(self.last_transactions) > 5:
            self.last_transactions.pop(0)
        return "Deposit successful"
        
class GUI:
    def __init__(self, atm):
        self.atm = atm
        
        self.window = tk.Tk()
        self.window.title("ATM")
        
        self.balance_label = tk.Label(self.window, text="Balance: {}".format(self.atm.balance))
        self.balance_label.pack()
        
        self.amount_label = tk.Label(self.window, text="Amount:")
        self.amount_label.pack()
        
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()
        
        self.withdraw_button = tk.Button(self.window, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()
        
        self.deposit_button = tk.Button(self.window, text="Deposit", command=self.deposit)
        self.deposit_button.pack()
        
        self.last_transactions_label = tk.Label(self.window, text="Last 5 Transactions:")
        self.last_transactions_label.pack()
        
        self.last_transactions_listbox = tk.Listbox(self.window)
        self.last_transactions_listbox.pack()
        
        for transaction in self.atm.last_transactions:
            self.last_transactions_listbox.insert(tk.END, transaction)
        
        self.window.mainloop()
        
    def withdraw(self):
        amount = int(self.amount_entry.get())
        message = self.atm.withdraw(amount)
        self.balance_label.config(text="Balance: {}".format(self.atm.balance))
        self.last_transactions_listbox.delete(0, tk.END)
        for transaction in self.atm.last_transactions:
            self.last_transactions_listbox.insert(tk.END, transaction)
        self.amount_entry.delete(0, tk.END)
        messagebox.showinfo("Withdraw", message)
        
    def deposit(self):
        amount = int(self.amount_entry.get())
        message = self.atm.deposit(amount)
        self.balance_label.config(text="Balance: {}".format(self.atm.balance))
        self.last_transactions_listbox.delete(0, tk.END)
        for transaction in self.atm.last_transactions:
            self.last_transactions_listbox.insert(tk.END, transaction)
        self.amount_entry.delete(0, tk.END)
        messagebox.showinfo("Deposit", message)

# create an ATM object
atm = ATM()

# create a GUI object
gui = GUI(atm)
