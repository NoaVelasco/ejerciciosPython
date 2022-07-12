class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.tot_led = 0

    def __str__(self):
        stars = 30
        stars -= len(self.name)
        stars /= 2
        stars = int(stars)
        stars *= '*'
        output_1 = stars + self.name.capitalize() + stars
        if len(output_1) < 30:
            output_1 = stars + self.name.capitalize() + stars + '*'

        amounts = []
        descrips = []
        for x in self.ledger:
            if len(str(int(x['amount']))) == 4:
                dsp_amount = str(f'{x["amount"]:.2f}')
                amounts.append(dsp_amount)
            elif len(str(int(x['amount']))) < 4:
                spaces = 4 - len(str(int(x['amount'])))
                dsp_amount = str(f'{spaces * " "}{x["amount"]:.2f}')
                amounts.append(dsp_amount)

            else:
                dsp_amount = str(f'{x["amount"]:.2f}')[-7:]
                amounts.append(dsp_amount)

            if len(x['description']) > 23:
                dsp_descrip = x['description'][0:23]
                descrips.append(dsp_descrip)
            else:
                spaces = 23 - len(x['description'])
                descrips.append(f"{x['description']}{spaces * ' '}")

        dsp_ledger = []
        for d, a in zip(descrips, amounts):
            dsp_ledger.append(d)
            dsp_ledger.append(a)
            dsp_ledger.append('\n')

        output_2 = ''.join(x for x in dsp_ledger)
        output_3 = (f'Total: {self.get_balance()}')

        output = ''.join(output_1 + '\n' + output_2 + output_3)
        return output

    def check_funds(self, amount):
        if amount > self.tot_led:
            return False
        else:
            return True

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.tot_led += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -amount, 'description': description})
            self.tot_led -= amount
            return True
        else:
            return False

    def get_balance(self):
        return f'{self.tot_led:.2f}'

    def total_withdrawals(self):
        withdrawals = 0
        for l in self.ledger:
            if l['amount'] < 0:
                withdrawals += l['amount']
        return withdrawals

    def transfer(self, amount, category):
        success = self.check_funds(amount)
        if success is True:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
        # return success


def create_spend_chart(class_list):
    categories = []
    total_spend = 0

    for l in class_list:
        name_tot_per = []
        name_tot_per.append(l.name)
        spend = l.total_withdrawals()
        name_tot_per.append(spend)
        total_spend += spend
        categories.append(name_tot_per)

    # sacar los porcentajes de cada categoría
    for c in categories:
        per = abs(c[1]) / abs(total_spend/100)
        per = f'{int(per):02d}'  # me aseguro de que <10% tiene 0 delante
        per = per[0]  # y ahora me quedo solo con las decenas
        c.pop()  # ya no necesito el total
        c.append(per)

    output01 = 'Percentage spent by category'
    output02 = []
    counter = 10
    for x in range(10):
        output02.append([f'{counter:2d}0| '])
        counter -= 1
    output02.append(['  0| '])

    counter = 10
    output02b = []
    for line in output02:
        for c in categories:
            if int(c[1]) >= counter:
                line.append('o  ')
            else:
                line.append('   ')
        if counter > 0:
            line.append('\n')
        counter -= 1
        line_join = ''.join(line)
        output02b.append(line_join)

    output03 = '    -' + ('-' * len(categories)*3)

    names = [x[0] for x in categories]
    max_let = map(len, names)
    rango = max(max_let)

    output04 = []
    for x in range(rango):
        output04.append('     ')
        for c in names:
            try:
                output04.append(c[x] + '  ')
            except IndexError:
                output04.append('   ')
        output04.append('\n')

    output04 = output04[0:-1]

    return f'{output01}\n{"".join(output02b)}\n{output03}\n{"".join(output04)}'


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
food.transfer(50, business)
business.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))
print(create_spend_chart([business, food, entertainment]))

# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()
# actual = food.ledger[2]
