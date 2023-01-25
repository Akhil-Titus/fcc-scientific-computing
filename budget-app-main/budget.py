def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    # Retrieve total expense of each category
    total      = 0
    expenses   = []
    names     = []
    len_names = 0
    for item in categories:
        expense    = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
        total     += expense

        if len(item.name) > len_names:
            len_names = len(item.name)

        expenses.append(expense)
        names.append(item.name)

    # Convert to percent + pad names
    expenses = [(x/total)*100 for x in expenses]
    names   = [name.ljust(len_names, " ") for name in names]

      # Format output
    for c in range(100,-1,-10):
        output += str(c).rjust(3, " ") + '|'
    for x in expenses:
        output += " o " if x >= c else "   "
    output += " \n"

    # Add each category name
    output += "    " + "---"*len(names) + "-\n"

    for i in range(len_names):
        output += "    "
    for name in names:
        output += " " + name[i] + " "
    output += " \n"

    return output.strip("\n")



class Category:

    def __init__(self, name):
        """
        instantiate objects based on different budget
        categories like food, clothing, and entertainment. When
        objects are created, they are passed in the name of the
        category. The class should have an instance variable
        called ledger that is a list.
        """
        self.name = name
        self.ledger = []



    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description
        If no description is given, it should default to an
        empty string. The method should append an object to the
        ledger list in the form of {"amount": amount,
        description": description}.
        """
        self.ledger.append({"amount": amount, "description": description})
        return None

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method,
        but the amount passed in should be stored in the ledger
        as a negative number. If there are not enough funds,
        nothing should be added to the ledger. This method
        should return True if the withdrawal took place, and
        False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        A get_balance method that returns the current balance
        of the budget category based on the deposits and
        withdrawals that have occurred.
        """
        total_fund = 0
        for item in self.ledger:
            total_fund += item['amount']
        return total_fund

    def transfer(self, amount, category_1):
        """
        A transfer method that accepts an amount and another
        budget category as arguments. The method should add a
        withdrawal with the amount and the description "Transfer to
        [Destination Budget Category]". The method should then add
        a deposit to the other budget category with the amount and
        the description "Transfer from [Source Budget Category]". If
        there are not enough funds, nothing should be added to
        either ledgers. This method should return True if the
        transfer took place, and False otherwise.
        """
        if self.withdraw(amount, "Transfer to " + category_1.name):
            category_1.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount as an argument.
        It returns False if the amount is greater than the balance
        of the budget category and returns True otherwise. This method
        should be used by both the withdraw method and transfer method.
        """
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = ""
        output = self.name.center(30,"*")+ "\n"

        total = 0
        for item in self.ledger:
            total += item['amount']

            output += item['description'].ljust(23, " ")[:23]
            output += "{0:>7.2f}".format(item['amount'])
            output += "\n"

        output += "Total: " + "{0:.2f}".format(total)
        return output
