from decimal import Decimal
from .money import Money

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money):
        if not isinstance(price, Money):
            raise ValueError
        if price.amount <= Decimal("0"):
            raise ValueError("Price must be greater than zero")

        self._id = product_id
        self._name = name
        self._price = price
        
    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
    
    @property
    def price(self):
        return self._price
    
    
    def __str__(self):
        return f"Name: {self._name}; Price: {self.price}"