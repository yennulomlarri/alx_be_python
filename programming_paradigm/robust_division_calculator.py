# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division and handles potential errors robustly.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            raise ZeroDivisionError
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."