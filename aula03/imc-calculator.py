def imc_calculator(weight: float, height: float) -> str:
    imc = weight / (height ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obeso"

print(imc_calculator(70, 1.75))