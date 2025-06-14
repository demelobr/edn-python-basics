def total_price_calculator(product_name:str, price_of_product:float, amount:int):
    print("Demonstrativo da compra\n")
    print(f"Nome do produto: {product_name}\n")
    print(f"Preço da unidade do produto: R${price_of_product:.2f}\n")
    print(f"Quantidade do produto: {amount} unidade(s)\n")
    print(f"Preço total da compra: R${price_of_product*amount:.2f}\n")

total_price_calculator("Cadeira Infantil", 12.40, 3)