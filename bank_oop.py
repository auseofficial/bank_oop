#TASK_1_Encapsulation##

class Bank:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.acc_num = account_number
        self.acc_hol = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Total balance: {self.get_balance()}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Total balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance

acc1 = Bank(123456, "Akib Us Suny Eshan", 0)
acc1.deposit(10)
acc1.withdraw(500)


##TASK_2_##
class Item:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __str__(self):
        return self.get_info()

class Book(Item):
   def __init__(self,title,author,year,publisher,isbn):
     super().__init__(title,author,year)
     self.publisher=publisher
     self.isbn=isbn
