from .customer import Customer
from .product import Product
from .orderline import OrderLine
from .money import Money
from .payment import PaymentProcessor

class Order:
    def __init__(self, order_id: str, customer: Customer, payment_processor: PaymentProcessor):
        self._id = order_id
        self._customer = customer
        self._lines = []
        self._payment_processor = payment_processor
        
        
    def  add_product(self, product: Product, quantity: int):
        product.validate_quantity(quantity)
        self._lines.append(OrderLine(product, quantity))
        
    def total(self) -> Money:
        total = None
        for line in self._lines:
            if total is None:
                total = line.line_total()
            else:
                total = total + line.line_total()
        return total
    
    def checkout(self):
        order_total = self.total()
        self._payment_processor.process(order_total)
    
    @property
    def lines(self):
        return list(self._lines)
    
    def __str__(self):
        ret_val = "Order: \n"
        for line in self._lines:
            ret_val +=  str(line)
            ret_val += "\n"
        return ret_val
    

#I used "if total is None:" just a way to initialize the sum.
