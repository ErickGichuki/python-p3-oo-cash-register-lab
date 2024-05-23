#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self,title, price, quantity= 1):
        item_cost = price * quantity
        self.total += item_cost
        for _ in range(quantity):
            self.items.append(title)
        self.transactions.append(item_cost)

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_transaction_amount = self.transactions.pop()
            self.total -= last_transaction_amount
    