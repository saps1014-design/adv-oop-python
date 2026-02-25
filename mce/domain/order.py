from .customer import Customer
from .product import Product
from .orderline import OrderLine
from .money import Money

class Order:
    def __init__(self, order_id: str, customer: Customer, product: Product, quantity: int):
        self._id = order_id
        self._customer = customer
        
        self._lines = [OrderLine(product, quantity)]
    
    @property
    def id(self):
        return self._id
    
    @property
    def customer(self):
        return self._customer
    
    def  add_product(self, product: Product, quantity: int):
        self._lines.append(OrderLine(product, quantity))
        
    def total(self) -> Money:
        total = self._lines[0].line_total()
        for line in self._lines[1:]:
            total = total + line.line_total()
        return total

    @property
    def lines(self):
        return list(self._lines)
    
    def __str__(self):
        ret_val = "Order: \n"
        for line in self._lines:
            ret_val += str(line)
            ret_val += "\n"
        return ret_val