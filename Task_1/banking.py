def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient funds")
    return balance - amount

balance = int(input("How much is your balance?: "))
amount = int(input("How much would you like to withdraw?: "))
new_balance = withdraw(balance, amount)
print("Your new balance is: ", new_balance)