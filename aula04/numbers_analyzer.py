def numbers_analyzers() -> str:
    pair_count = 0
    odd_count = 0

    while True:
        try:
            number = int(input("Digite um número (ou digite sair para encerrar o programa): "))
            if number % 2 == 0:
                print(f"{number} é par")
                pair_count += 1
            else:
                print(f"{number} é ímpar")
                odd_count += 1
        except ValueError:
            return f"{pair_count} número(s) pares contados\n{odd_count} número(s) ímpares contados"

print(numbers_analyzers())