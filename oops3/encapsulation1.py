from oops3.Encapsulation import bankaccount

acc = bankaccount(12345,1000)

add_money = acc.deposite(100)
print(add_money)

acc.withdraw(1)
acc.get_balance()


# Encapsulation = Locking things + giving safe doors to use them
# Just like:
# You don’t touch the inside of a computer, you use buttons
# You don’t touch the engine of a car, you use the steering and pedals
# You don’t touch the bank vault, you withdraw using ATM

# Same in code!