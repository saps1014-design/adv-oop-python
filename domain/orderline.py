from product import Product
from money import Money

class OrderLine:
    
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be >0")

        self._product = product
        self._quantity = quantity
    
    @property
    def product(self) -> Product:
        return self._product
    
    def line_total(self) -> Money:
        return self._product.price * self._quantity
    
    def __str__(self) -> str:
        return f"{self._product.id} x {self._quantity} = {self.line_total()}"