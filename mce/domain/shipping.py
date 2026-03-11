from decimal import Decimal
from .money import Money

class ShippingCalculator:
    def calculate(self, price: Money) -> Money:
        raise NotImplementedError() 
    
    
class StandardShipping(ShippingCalculator):
    def calculate(self, price: Money) -> Money:
        return Money(Decimal("10"), price.currency)
    

class HeavyShipping(ShippingCalculator):
    def __init__(self, weight: Decimal):
        self._weight = weight
    
    def calculate(self, price: Money) -> Money:
        return Money(self._weight * Decimal("2"), price.currency)
    
    
class InternationalShipping(ShippingCalculator):
    def calculate(self, price: Money) -> Money:
        return Money(Decimal("50"), price.currency)


class FreeShipping(ShippingCalculator):
    def calculate(self, price: Money) -> Money:
        return Money(Decimal("0"), price.currency)
    

class PromotionalShipping(ShippingCalculator):
    def __init__(self, discount: Decimal):
        self._discount = discount
        
    def calculate(self, price: Money) -> Money:
        return Money(max(Decimal("0"), Decimal("10") - self._discount), price.currency)
        