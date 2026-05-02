def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def is_hot(celsius):
    """Returns True if temperature is above 30°C"""
    if celsius > 30:
        return True
    return False

def get_season(month):
    """Returns season name for a given month number (1-12)"""
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        raise ValueError(f"Invalid month: {month}")
