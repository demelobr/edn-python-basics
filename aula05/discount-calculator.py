def discount_calculator() -> str:
    price = float(input("Digite o preço do produto: "))
    discount = float(input("Digite o desconto que será dado(0 a 100): "))
    
    if discount < 0 or discount > 100:
        return "Porcentagem de disconto inválida. Precisa ser de 0 a 100!"
    
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return f"O preço final depois do desconto de {discount}% é: R$ {final_price:.2f}"

print(discount_calculator())