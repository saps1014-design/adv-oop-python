from decimal import Decimal
from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import PhysicalProduct
from mce.domain.money import Money
from mce.domain.invoice import Invoice
from mce.domain.giftcardproduct import GiftCardProduct

customer = Customer("1", "John")

prod = PhysicalProduct("1", "VideoGame", Money(Decimal("25"), "USD"), Money(Decimal("2.5"), "USD"))
gift = GiftCardProduct("GC1", "Gift Card", Decimal("50"), "USD")

order = Order("1", customer)

order.add_product(prod, 1)
order.add_product(gift, 1)

invoice = Invoice(order)
print(invoice.generate_text())
