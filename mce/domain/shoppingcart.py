from .orderline import OrderLine
from .money import Money

class ShoppingCart:
    
    def __init__(self):
        self._items = []
        
    def add(self, product, quantity: int):
        product.validate_quantity(quantity)
        self._items.append(OrderLine(product, quantity))
        
    
    def total(self) -> Money:
        total = None 
        for line in self._items:
            if total is None:
                total = line.line_total()
            else:
                 total = total + line.line_total()
        return total
    
    @property
    def items(self):
        return list(self._items)
    