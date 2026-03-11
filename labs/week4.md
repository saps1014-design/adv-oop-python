# Week 4 Homework  
## Composition & Object Collaboration


## Objective

This assignment reinforces:

- Prefer Composition over Inheritance  
- Strategy-style behavior injection  
- Loose coupling through delegation  
- Removing type-based conditionals  
- Designing collaborating objects  

You will refactor and extend your **Modular Commerce Engine (MCE)** system.

---

# Part 1 — Replace Shipping Inheritance with Composition (Required)

If you previously implemented shipping using inheritance (e.g., `PhysicalProduct`, `HeavyPhysicalProduct`, etc.), and haven't updated this during the class, you must refactor it.

## Step 1 — Create ShippingCalculator Abstraction

Create a shipping behavior abstraction (see work in class):

- `ShippingCalculator`
- Must define a `calculate(price)` method

## Step 2 — Implement At Least 3 Strategies

Implement at least three concrete shipping strategies:

- StandardShipping
- HeavyShipping (or weight-based)
- FreeShipping

Each must:

- Implement `calculate(price)`
- Contain only shipping logic
- Not depend on specific product subclasses

## Step 3 — Inject Shipping into Product

Refactor `Product` so that:

- It receives a `ShippingCalculator` object
- It delegates shipping cost calculation
- It does NOT use conditionals to determine shipping type
- No shipping logic inside product subclasses
- No conditional logic based on product type
- No subclass explosion for shipping variations

# Part 2 — Implement PaymentProcessor Strategy (Required)

The system must now support multiple payment types using composition.

## Step 1 — Create PaymentProcessor Abstraction

Define:

- `PaymentProcessor`
- Must define a `process(amount)` method

## Step 2 — Implement At Least 3 Payment Processors

For example:

- CreditCardProcessor
- PaypalProcessor
- CryptoProcessor

Each must:

- Implement `process(amount)`
- Contain only payment logic
- Not require changes to `Order` when adding new processors

## Step 3 — Inject Processor into Order

Refactor `Order` so that:

- It receives a `PaymentProcessor`
- It delegates payment processing
- It does NOT use `if` statements to determine payment type

Forbidden example:
```python
if payment_type == "credit":
    # payment specific logic here
```
# Part 3 — Eliminate Conditional Type Logic (Required)

Review your entire codebase.

You must eliminate:

- `if product_type == ...`
- `isinstance(...)` checks
- Branching logic based on category flags
- Type-based shipping or payment logic

Behavior differences must be expressed through composition and delegation.

If adding a new shipping or payment type requires modifying existing classes,
your design is not open for extension.

Refactor accordingly.

---

# Part 4 — Shopping Cart Collaboration (Required)

Implement or improve your `ShoppingCart` class.

The cart must:

- Allow adding products with quantity
- Calculate total using `OrderLine`
- Collaborate with product and shipping behavior
- Not duplicate pricing or shipping logic

The cart must delegate behavior — not calculate it directly.



# Code Quality Requirements

Your submission must:

- Use type hints
- Follow encapsulation principles
- Avoid exposing internal collections directly
- Avoid duplication
- Keep methods cohesive and focused
- Maintain readable class responsibilities

---

# Stretch Goals (Optional)

Choose one:

1. Create a `PromotionalShipping` strategy.
2. Create a `MockPaymentProcessor` for testing.
3. Allow runtime switching of shipping strategies.
4. Add logging behavior via composition (without modifying core logic).

---

# Deliverables

Submit your GitHub repository containing:

- Refactored product design
- Shipping strategies implemented
- PaymentProcessor strategies implemented
- No type-based conditionals
- Working ShoppingCart
- Clean commit history

---


### Engineering Reminder

If your solution required adding more subclasses  
when a small behavior object would have worked, refactor again.
