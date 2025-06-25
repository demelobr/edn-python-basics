def age_classifier(age: int) -> str:
    if age < 0:
        return "Idade Invalida"
    elif age >= 0 and age <= 12:
        return "Criança"
    elif age >= 13 and age <= 17:
        return "Adolescente"
    elif age >= 18 and age <= 59:
        return "Adulto"
    else:
        return "Idoso"

print(age_classifier(10))  # Criança
print(age_classifier(15))  # Adolescente
print(age_classifier(30))  # Adulto
print(age_classifier(65))  # Idoso
print(age_classifier(-5))  # Invalid age