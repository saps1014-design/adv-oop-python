from .money import Money
from .shipping import ShippingCalculator, FreeShipping
from decimal import Decimal

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator):
        self._id = product_id
        self._name = name
        self._price = price
        self._shipping_calculator = shipping_calculator
    
    @property
    def price(self) -> Money:
        return self._price
    
    def calculate_shipping(self) -> Money:
        return self._shipping_calculator.calculate(self._price)    
        
    def get_total_price(self) -> Money:
        return self._price  + self.calculate_shipping()
    
    def calculate_tax(self) -> Money:
        return Money(Decimal("0"), self.price.currency)
    
    def validate_quantity(self, quantity: int):
        return
    
    def __str__(self):
        return f"{self._name}\nPrice:\n---Base: {self.get_total_price()}\n---Tax: {self.calculate_tax()}"
    
    
class PhysicalProduct(Product):
    
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator):
        super().__init__(product_id, name, price, shipping_calculator)
    
    def calculate_tax(self) -> Money:
        return self.price * Decimal("0.15")

class DigitalProduct(Product):
    
    def __init__(self, product_id: str, name: str, price: Money):
        super().__init__(product_id, name, price, FreeShipping())

class SubscriptionProduct(Product):

    def __init__(self, product_id, name, price, months: int):
        super().__init__(product_id, name, price, FreeShipping())
        self._months = months
        
    def get_total_price(self) -> Money:
        return self._price * self._months

class FreeProduct(Product):

    def __init__(self, product_id: str, name: str, currency: str):
        super().__init__(product_id, name, Money(Decimal("0"), currency), FreeShipping())
    
    
class LimitedQuantityProduct(Product):
    pass
