
class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self._id = customer_id
        self._name = name
        
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name    


    

