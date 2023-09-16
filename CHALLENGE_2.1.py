''' Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. '''


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name}: ₹{self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a BankAccount instance
    account = BankAccount("1234567890", "Person", 1000)

    
    account.display_balance()
    account.deposit(600)
    account.withdraw(200)
    account.withdraw(1500)  
    account.deposit(-100)
    account.display_balance()
