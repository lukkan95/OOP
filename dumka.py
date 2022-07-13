import csv

class Item:
    pay_rate = 0.8 #Pay rate after 20% discount - It's class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f'Sorry but {price} is not greater than zero'
        assert quantity >= 0, f'Sorry but {quantity} is not greater than zero'

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

Item.instantiate_from_csv()
print(Item.all)


