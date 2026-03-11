from .product import Product
from .money import Money


class OrderLine:
    
    def __init__(self, product: Product, quantity: int):
        self._product = product
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self._quantity = quantity
    
    @property 
    def product(self) -> Product:
        return self._product
    
    @property
    def product(self) -> Product:
        return self._product
    
    def line_total(self) -> Money:
        unit_total = self._product.get_total_price() + self._product.calculate_tax()
        return unit_total * self._quantity
    
    def __str__(self):
        return f"\nProduct: {self._product}\nQuantity: {self._quantity}"
    
    def __repr__(self):
         return f"{self._product} {self._quantity}\n"