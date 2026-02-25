from decimal import Decimal

from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import Product
from mce.domain.money import Money


# orders = []

# def create_order(customer_name, product_name, price, quantity):
#     total = price * quantity
#     orders.append({
#         "customer_name": customer_name,
#         "product": product_name,
#         "price": price,
#         "quantity": quantity,
#         "total": total
#     })
    
    
    
"""
A customer places an order containing multiple products.
Each product has a price.
An order contains multiple order lines.
Each line has a quantity.

Customer
Order
OrderLine
Product

Money

"""


customer = Customer("1", "John")

prod = Product("1", "x", Money(Decimal("10"), "USD"))
prod1 = Product("2", "y", Money(Decimal("20"), "USD"))

order = Order("1", customer, prod, 1)

order.add_product(prod1, 2)

print(order)


from mce.domain.invoice import Invoice

invoice = Invoice(order)

print()
print(invoice.generate_text())
