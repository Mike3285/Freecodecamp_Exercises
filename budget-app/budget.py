class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def get_balance(self):
        balance = [x["amount"] for x in self.ledger]
        return sum(balance)

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        s_1 = (self.name.center(30, '*')) + '\n'
        for i in self.ledger:
            s_1 = s_1 + str(i["description"])[:23].ljust(23) + "{:.2f}".format(i["amount"]).rjust(7) + '\n'
        s_1 = s_1 + "Total: " + str(self.get_balance())
        return s_1


food = Category("Food")
food.deposit(100, "First Deposit")
food.withdraw(70, "Stuff")
food.withdraw(10, "Nice Stuff")
entertainment = Category("Entertainment")
entertainment.deposit(100, "First Deposit")
entertainment.withdraw(30, "Things")
entertainment.withdraw(20, "Cool Things")
business = Category("Business")
business.deposit(100, "First Deposit")
business.withdraw(10, "Things")


def create_spend_chart(categories):
    final = ''
    data = [{"name": cat.name, "total_expenses": abs(sum([a["amount"] for a in cat.ledger if a["amount"] < 0]))} for cat
            in categories]
    total = sum(cat["total_expenses"] for cat in data)
    for cat in data:
        cat["percentage"] = (cat["total_expenses"] * 100) // total
    max_line_l = 4 + (len(categories) * 3) + 1
    numbers = [i for i in range(0, 101, 10)]
    numbers.reverse()
    final += "Percentage spent by category\n"
    for i in numbers:
        text = str(i).rjust(3) + '|'
        for d in data:
            if d["percentage"] >= i:
                text += ' o '
            else:
                text += '   '
        final += text.ljust(max_line_l) + '\n'
    final += '    '.ljust(max_line_l, '-') + '\n'
    names = [cat["name"] for cat in data]
    max_l = max([len(n) for n in names])
    names = [name.ljust(max_l) for name in names]
    for i in range(max_l):
        my = ''
        for j in range(len(names)):
            my += ' ' + names[j][i] + ' '
        final += my.rjust(max_line_l-1) +' '+ '\n'
    return final[:-2]+" "