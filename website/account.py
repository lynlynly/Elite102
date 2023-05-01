'''
from .models import CustomerInfo, AccountInfo
from flask import flash, render_template, url_for
class bankAccount:
    
    def __init__(self):
        self.balance = 0
        self.customerInfo_id = CustomerInfo.id

    
    def depositMoney(self):
        amountDeposit = float(input("Enter the amount needed to deposit: "))
        if amountDeposit <= 0: 
            flash('The deposit money has to be more than 0.00 dollars.', category='error')
        else:
            self.balance+= amountDeposit
            flash("You have sucessfully added $" + amountDeposit, category='sucess')

    def withdrawMoney(self):
        amountWithdraw = float(input("Enter the amount needed for withdrawal: "))
        if amountWithdraw > self.balance:
            flash("Can not withdraw more than balance amount", category = 'error')
        else:
            self.balance -= amountWithdraw
            flash('You have sucessfully withdraw $' + amountWithdraw, category = 'sucess')

    def checkBalance(self):
        return self.balance
    

    
class SavingAccount(bankAccount):
    interestRate = 0.05
    def __init__(self, balance):
        super().__init__(balance)

    def add_interest(self):
        interest = self.balance * self.interestRate
        self.balance += interest


class CheckingAccount(bankAccount):

    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self):
        fee = 4.00
        minBalance = 10.00
        withdrawAmount = float(input("Enter the withdrawl amount: "))
        self.balance -= withdrawAmount
        if(self.balance <= 0 or self.balance < minBalance):
            self.balance -= fee
            flash('you have exceeded the minimum balance - a fee of 4.00 dollars was added', cateogyr = 'error')


    

'''