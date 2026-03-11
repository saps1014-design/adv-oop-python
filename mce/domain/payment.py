from .money import Money


class PaymentProcessor:
    def process(self, amount: Money):
        raise NotImplementedError()
    

class CreditCardProcessor(PaymentProcessor):
   
   def process(self, amount: Money):
       print(f"Charging credit card: {amount}") 


class PaypalProcessor(PaymentProcessor):
    
    def process(self, amount: Money):
        print(f"Processing PayPal payment of: {amount}")
        

class CryptoProcessor(PaymentProcessor):
    
    def process(self, amount: Money):
        print(f"Sending crypto payment of: {amount}")