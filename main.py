from decimal import Decimal

from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import PhysicalProduct, DigitalProduct
from mce.domain.money import Money
from mce.domain.invoice import Invoice
from mce.domain.shipping import StandardShipping, HeavyShipping, FreeShipping
from mce.domain.payment import CreditCardProcessor, PaypalProcessor, CryptoProcessor
from mce.domain.shoppingcart import ShoppingCart


customer = Customer("1", "Sergio")

credit_card_processor = CreditCardProcessor()

book = PhysicalProduct(
    "1",
    "Book",
    Money(Decimal("35"), "USD"),
    StandardShipping()
)

tv = PhysicalProduct(
    "2",
    "TV",
    Money(Decimal("500"), "USD"),
    HeavyShipping(Decimal("15"))
)

headphones = DigitalProduct(
    "3",
    "E-Book",
    Money(Decimal("200"), "USD")
)

order = Order("1", customer, credit_card_processor)
order.add_product(book, 1)
order.add_product(tv, 1)
order.add_product(headphones, 2)

invoice = Invoice(order)

print("ORDER / INVOICE")
print(invoice.generate_text())
print("Total:", order.total())
order.checkout()

print("\nSHOPPING CART")
cart = ShoppingCart()
cart.add(book, 1)
cart.add(headphones, 2)

print("Cart total:", cart.total())




