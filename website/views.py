from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import CustomerInfo, AccountInfo
from . import db
import json

views = Blueprint('views', __name__)

'''
@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('NOte is too short!', category = 'error')
        
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()

    return  render_template("home.html", user = current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    
    note = json.loads(request.data)
    noteId = note['note']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
'''

class bankAccount:
    
    def __init__(self):
        self.balance = 0
        self.customerInfo_id = CustomerInfo.id

    @views.route('/deposit')
    @login_required
    def depositMoney(self):
        amountDeposit = float(input("Enter the amount needed to deposit: "))
        if amountDeposit <= 0: 
            flash('The deposit money has to be more than 0.00 dollars.', category='error')
        else:
            self.balance+= amountDeposit
            flash("You have sucessfully added $" + amountDeposit, category='sucess')
        
        return render_template('home.html')

    @views.route('/withdraw')
    @login_required
    def withdrawMoney(self):
        amountWithdraw = float(input("Enter the amount needed for withdrawal: "))
        if amountWithdraw > self.balance:
            flash("Can not withdraw more than balance amount", category = 'error')
        else:
            self.balance -= amountWithdraw
            flash('You have sucessfully withdraw $' + amountWithdraw, category = 'sucess')
        
        return render_template('home.html')
    @views.route('/balance')
    @login_required
    def checkBalance(self):
        print("Balance: " + self.balance)
        return render_template('home.html')
    

    
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
