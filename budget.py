class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0
        self.cost = 0.0
        self.costper = 0.0
        self.message = "{:*^30}".format(name) + "\n"
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount":amount, "description":description})
        self.balance = self.balance + amount
        if len(description) > 29 - len(format(amount, '.2f')):
            description = description[0:(29 - len(format(amount, '.2f')))]
        self.message = self.message + description + (30 - len(description) - len(format(amount, '.2f'))) * " " + format(amount, '.2f') + "\n"
    def check_funds(self, amount):
        if amount > self.balance: return False
        else: return True
    def withdraw(self, amount, description = ""): 
        if self.check_funds(amount) == True:
            self.ledger.append({"amount":-amount, "description":description})
            self.balance = self.balance - amount
            if len(description) > 29 - len(format(amount, '.2f')):
                description = description[0:(29 - len(format(-amount, '.2f')))]
            self.message = self.message + description + (30 - len(description) - len(format(-amount, '.2f'))) * " " + format(-amount, '.2f') + "\n"
            self.cost = self.cost + amount
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.name) 
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
    def __str__(self):
        self.message = self.message + "Total: " + str(self.balance)
        return self.message
    def __repr__(self):
        return self.message

def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    totalcost = 0.0
    maxlen = 0
    for category in categories:
        totalcost = totalcost + category.cost
    for category in categories:
        category.costper = 100 * category.cost / totalcost
    for i in range(11):
        output = output + "{: >3}".format((10 - i) * 10) + "| "
        for category in categories:
            if category.costper / 10 >= 10 - i:
                output = output + "o  "
            else: 
                output = output + "   "
        output = output + "\n"
    output = output + "    -"
    for category in categories:
        output = output + "---"
        if maxlen < len(category.name):
            maxlen = len(category.name)
    output = output + "\n"
    for i in range(maxlen):
        output = output + "     "
        for category in categories:
            if len(category.name) > i:
                output = output + category.name[i] + "  "
            else:
                output = output + "   "
        output = output + "\n"
    output = output.rstrip("\n")
    return output
        