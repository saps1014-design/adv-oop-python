#from .address import Address

class Customer:
    def __init__(self, customer_id: str, name: str):
        self._id = customer_id
        self._name = name

    def __str__(self):
        return f"{self._name} (ID: {self._id})"
        
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name    




