nums = [2,11,15,7]
target = 9
for i in range(len(nums)):
    #start the range at index 1 because we adding 1 to i index
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)


print("\n")


class Account:
    def __init__(self):
        self.balance = 0
        print("congrats account is created\n")

    def deposit(self):
        amount = float(input("enter a deposit amount: "))
        self.balance = self.balance + amount
        print("your account balance is %.2f$" % self.balance)

    def withdraw(self):
        amount = float(input("enter a amount to withdraw: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("your new account balance is %.2f$ " % self.balance)
        else:
            print("Sorry Insufficient funds your account only have %.2f$" %self.balance)

acc = Account()
print(acc.deposit())
print(acc.withdraw())