from decimal import Decimal


class Money:
    
    def __init__(self, amount: Decimal, currency: str) -> None:
        self._amount: Decimal  = amount
        self._currency: str = currency
        
    @property
    def currency(self) -> str:
        return self._currency

    @property
    def amount(self) -> Decimal:
        return self._amount

    def __mul__(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)
    
    def __add__(self, other: "Money") -> "Money":
        if self._currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self._amount + other.amount, self.currency)
    
    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"
    
    @property
    def amount(self):
        return self._amount