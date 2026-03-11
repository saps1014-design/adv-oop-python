from decimal import Decimal
from .product import Product
from .giftcardmoney import GiftCardMoney
from .exceptions import GiftCardQuantityError

class GiftCardProduct(Product):
    def __init__(self, product_id: str, name: str, amount: Decimal, currency: str):
        super().__init__(product_id, name, GiftCardMoney(amount, currency))

    def validate_quantity(self, quantity: int):
        if quantity != 1:
            raise GiftCardQuantityError("Gift card quantity must be exactly 1")