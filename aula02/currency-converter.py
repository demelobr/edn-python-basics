def currency_converter(amount: float , to_currency: str) -> str:
    if to_currency == "USD":
        conversion_rate = 5.20
    elif to_currency == "EUR":
        conversion_rate = 6.15        
    return f"{amount * conversion_rate:.2f} {to_currency}"

print(currency_converter(100.0, "USD"))
print(currency_converter(100.0, "EUR"))