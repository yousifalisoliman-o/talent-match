class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def get_balance(self):
        c = 0
        for x in self.ledger:
            c += x["amount"]
        return c

    def __str__(self):
        title = self.name.center(30, "*")
        e = []

        for x in self.ledger:
            c = x["description"][:23].ljust(23)
            d = f"{x['amount']:.2f}".rjust(7)
            e.append(f"{c}{d}")

        ledger_lines = "\n".join(e)
        total_line = f"Total: {self.get_balance():.2f}"

        return f"{title}\n{ledger_lines}\n{total_line}"


def create_spend_chart(categories):

    names = []

    for category in categories:
        names.append(category.name)


    s = []

    total = 0

    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])


    for category in categories:
        spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])

        percent = spent / total * 100
        s.append((percent // 10) * 10)


    max_length = 0

    for name in names:
        if len(name) > max_length:
            max_length = len(name)


    chart = "Percentage spent by category\n"


    for perc in range(100, -1, -10):
        row = []

        for c in s:
            if perc <= c:
                row.append("o  ")
            else:
                row.append("   ")

        chart += f"{perc:>3}| {''.join(row)}\n"


    chart += f"    {'-' * (len(s) * 3 + 1)}\n"


    for i in range(max_length):
        row = "     "

        for name in names:
            if i < len(name):
                row += name[i] + "  "
            else:
                row += "   "

        chart += row + "\n"


    chart = chart.rstrip("\n")

    return chart
