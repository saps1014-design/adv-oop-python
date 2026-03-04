### 1. Implement a New Product Type

Create a new class:
```python
GiftCardProduct
```

### Requirements:

- No tax is applied.
- Quantity must always be exactly 1.
- If quantity > 1, raise a custom exception.
- Must integrate seamlessly into the existing system.
- No modifications allowed in `OrderLine` to support this new type.

### Ensure:

- No `if product.type == ...`
- No `isinstance()` checks
- No category flags controlling behavior
- All behavior variation must be handled using polymorphism.
- All product subclasses must:
    - Behave correctly when used anywhere a `Product` is expected.
    - Not surprise the caller.
    - Not throw unexpected exceptions for normal usage.

---


## Bonus

Refactor shipping behavior into a separate class and inject it into `PhysicalProduct` instead of hardcoding shipping logic inside the product class.

---

## Submission Requirements

- Clean, working code
- No conditional logic controlling product behavior
- Proper use of polymorphism
- Meaningful commit history


---
