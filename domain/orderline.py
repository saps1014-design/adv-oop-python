from product import Product
from money import Money

class OrderLine:
    
    def __init__(self, product: Product, quantity: int):
        self._product = product
        self._quantity = quantity
    
    
    
    def line_total(self) -> Money:
        return self._product.price * self._quantity