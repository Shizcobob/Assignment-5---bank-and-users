class bankaccount:

    def __init__(self, interest_rate=0.01, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance-amount>0:
            self.balance-=amount
            return self
        else: 
            print("Insufficient funds: Charging a $5 Fee")
            self.balance-=5
            return self

    def display_info(self):
        print(f"Balance : {self.balance} Interest Rate : {self.interest_rate}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self


class User:


    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
        self.account = bankaccount(0.02, 100)
        self.accountTwo = bankaccount(0.02, 500)

    def userDepo(self, selector):
        if selector == 1:
            self.account.deposit(200)
            print(f"Account Balance : {self.account.balance}")
            return self
        if selector == 2:
            self.accountTwo.deposit(100)
            print(f"Account Balance : {self.account.balance}")
            return self

    def userWith(self, selector):
        if selector == 1:
            self.account.withdraw(105)
            print(f"Account Balance : {self.account.balance}")
            return self
        if selector == 2:
            self.accountTwo.withdraw(25)
            print(f"Account Balance : {self.account.balance}")
            return self
        
    def transfer(self, target, amount):
        self.account.balance -= amount
        print(f"Account Balance : {self.account.balance}")
        target.account.balance += amount
        print(f"Account Balance : {target.account.balance}")
        return self
        


    def display_user_balance(self):
        print(f"Account Balance : {self.account.balance}")
        return self

    def display_info(self):
        print(f"First_name : {self.first_name}\nLast_name : {self.last_name}\nEmail: {self.email}\nAge : {self.age}\nIs_Reward_Member: {self.is_reward_member}\nGold_Card_Points : {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_reward_member == True:
            print("Already Memeber")
            return self
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            return self

    def spendPoints(self, spent):
        self.gold_card_points =self.gold_card_points - spent
        return self
    


Anna = User("Anna", "Last", "Hello@goodbye.com", 33)
Bob = User("Bob", "Last", "emaily@ohno.com", 55)
Cindy = User("Cindy", "Last", "emaily@ohno.com", 43)

Anna.userWith(1).display_user_balance()
Bob.transfer(Anna, 20)