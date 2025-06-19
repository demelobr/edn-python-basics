def discount_calculator(product: str, price: float, discount: float) -> str:
    return f"{product} com valor original de R$ {price:.2f}, após desconto de {discount}%, custará ao cliente R$ {price * (1 - discount / 100):.2f}."

print(discount_calculator("Camiseta", 50.00, 20))