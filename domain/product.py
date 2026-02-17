from money import Money

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money):
        self._id = product_id
        self._name = name
        self._price = price
        
    @property
    def price(self):
        return self._price
    
    
