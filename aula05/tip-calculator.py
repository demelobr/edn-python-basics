def tip_calculator(bill: float, percentage: float) -> float:
    return bill * (percentage / 100)

print(f"A gorgeta foi de R$ {tip_calculator(100, 10):.2f}")  # Exemplo de uso