from oops3.Encapsulation import bankaccount

acc = bankaccount(12345,1000)

add_money = acc.deposite(100)
print(add_money)

acc.withdraw(1)
acc.get_balance()