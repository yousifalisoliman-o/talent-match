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
            c = x["description"].ljust(23)
            d = f"{x['amount']:.2f}".rjust(7)
            e.append(f"{c}{d}")
        ledger_lines = "\n".join(e)
        total_line = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{ledger_lines}\n{total_line}"


def create_spend_chart(categories):
    pass