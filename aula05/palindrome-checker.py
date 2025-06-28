def palindrome_checker(text: str) -> str:
    # 1. Normalizar o texto: remover espaços e pontuação, e converter para minúsculas
    normalized_text = "".join(caractere.lower() for caractere in text if caractere.isalnum())

    # 2. Verificar se o texto normalizado é igual ao seu inverso
    if normalized_text == normalized_text[::-1]:
        return "Sim"
    else:
        return "Não"

print(palindrome_checker("Arara"))
print(palindrome_checker("Socorram-me, subi no ônibus em Marrocos"))