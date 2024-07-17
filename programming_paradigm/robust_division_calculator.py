def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Can not divide by zero."
        return num / den
    except ValueError:
        return "Error: Please enter numeric value only."


