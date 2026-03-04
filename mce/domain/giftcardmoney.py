from decimal import Decimal
from .money import Money
from .exceptions import GiftCardQuantityError

class GiftCardMoney(Money):
    def __mul__(self, multiplier: int):
        if multiplier != 1:
            raise GiftCardQuantityError("Gift card quantity must always be exactly 1")
        return GiftCardMoney(self.amount, self.currency)