from decimal import Decimal

from customer import Customer
from product import Product
from orderline import OrderLine
from money import Money

class Order:
    def __init__(self, order_id: str, customer: Customer) -> None:
        self._id = order_id
        self._customer = customer
        self._lines: list[OrderLine] = []
        
    def  add_product(self, product: Product, quantity: int) -> None:
        self._lines.append(OrderLine(product, quantity))
        
    def remove_product(self, product_id: str) -> None:
        self._lines = [line for line in self._lines if line.product.id != product_id]

    def total(self) -> Money:
        total_money = Money(Decimal("0"), "CAN")
        for line in self._lines:
            total_money = total_money + line.line_total()
        return total_money
    
    def __str__(self) -> str:
        lines_text = "\n".join(str(line) for line in self._lines)
        return (
            f"Order {self._id}\n"
            f"Customer: {self._customer.name}\n"
            f"{lines_text}\n"
            f"Total: {self.total()}"
        )