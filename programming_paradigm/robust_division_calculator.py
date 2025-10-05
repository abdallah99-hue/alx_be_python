# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division while handling errors:
    - Division by zero
    - Non-numeric inputs
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
