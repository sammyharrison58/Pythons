def get_phone(country_code, area, first, last):
    """Return the full phone number with country code."""
    return f"+{country_code}-{area}-{first}-{last}"


phone_num = get_phone(country_code=1, area=234, first=567, last=8900)
print(phone_num)


def print_address(**kwargs):
    """Print a formatted address from keyword arguments."""

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


print_address(
    name="Farher looks", street="123 Main St", city="Anytown", state="CA", zip="12345"
)


def ship_label(*args, **kwargs):
    """Print a shipping label from positional and keyword arguments."""
    print("Shipping Label:")
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


ship_label("Father Looks", "123 Main St", city="Anytown", state="CA", zip="12345")
print_address(
    name="Father Looks", street="123 Main St", city="Anytown", state="CA", zip="12345"
)
