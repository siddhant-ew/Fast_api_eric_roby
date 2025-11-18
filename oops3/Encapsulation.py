# class bankaccount:

#     def __init__(self, account_number:int, balance:float):
#         self.__account_number = account_number
#         self.__balance = balance

#     def deposite(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("your deposite amount is added in you account")
#         else:
#             print("the amount must be positive")

#     def withdraw(self, amount):
#         print(f"DEBUG: amount = {amount} ({type(amount)}), balance = {self.__balance} ({type(self.__balance)})")
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"The amount rupees {amount} has been withdrawn successfully.")
#             print(f"Remaining balance: rupees {self.__balance}.")
#         else:
#             print(f"Your account balance is not sufficient to withdraw {amount} rupees, your current account balance is rupees {self.__balance}")
    
#     # def withdraw(self, amount):
#     #     if amount <= self.__balance:
#     #         self.__balance -= amount
#     #         print(f"The amount rupees{self.__balance} has been withdrawn successfully")
#     #     else:
#     #         print(f"Your account balance is not sufficient to withdraw {amount} rupees, your current account balance is rupees {self.__balance}")

#     def get_balance(self):
#         return self.__balance


class bankaccount:

    def __init__(self, account_number:int, balance:float):
        self.__account_number = account_number
        self.__balance = float(balance)

    def deposite(self, amount):
        amount = float(amount)
        if amount > 0:
            self.__balance += amount
            print("Your deposit amount is added to your account.")
        else:
            print("The amount must be positive.")

    def withdraw(self, amount):
        amount = float(amount)
        print(f"DEBUG: amount = {amount} ({type(amount)}), balance = {self.__balance} ({type(self.__balance)})")  # Debug line
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"The amount rupees {amount} has been withdrawn successfully.")
            print(f"Remaining balance: rupees {self.__balance}.")
        else:
            print(f"Your account balance is not sufficient to withdraw {amount} rupees, your current account balance is rupees {self.__balance}.")

    def get_balance(self):
        return self.__balance
