def fuel_consumption_calculator(amount_of_fuel: float, distance: float) -> str:
    if amount_of_fuel <= 0.0 or distance <= 0.0:
        raise ValueError("A quantidade de combustível e a distância devem ser maiores que zero!")

    consumption = distance / amount_of_fuel

    result = f"""
        A quantidade de combustível utilizada foi: {amount_of_fuel:.2f} litros \n
        A distância percorrida foi: {distance:.2f} km \n
        O consumo médio do veículo é: {consumption:.2f} km/l \n
    """
    return result

print(fuel_consumption_calculator(25.0, 300.0))