from .order import Order

class Invoice:
    
    def __init__(self, order: Order):
        self._order = order
        
    def total(self):
        return self._order.total()
    
    def generate_text(self) -> str:
        lines = []
        lines.append("INVOICE")
        lines.append(f"Order ID: {self._order.id}")
        lines.append(f"Customer: {self._order.customer}")
        lines.append("")
        lines.append("Items:")

        for line in self._order.lines:
            product = line.product
            lines.append(
                f"- {product.name} x {line.quantity} @ {product.price} = {line.line_total()}"
            )

        lines.append("")
        lines.append(f"TOTAL: {self.total()}")

        return "\n".join(lines)
        """
        Generate a text representation of the invoice.
        
        Returns:
            str: A formatted string containing the invoice details.
        """
    