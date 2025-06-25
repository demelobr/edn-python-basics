def celsius_fahrenheit_kelvin(measurement: float, origin_unit: str, target_unit: str) -> str:
    match origin_unit.lower():
        case "celsius":
            if target_unit.lower() == "fahrenheit":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {((measurement * 9/5) + 32):.2f}°F"
            elif target_unit.lower() == "kelvin":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {(measurement + 273.15):.2f}K"
        case "fahrenheit":
            if target_unit.lower() == "celsius":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {((measurement - 32) * 5/9):.2f}°C"
            elif target_unit.lower() == "kelvin":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {((measurement - 32) * 5/9 + 273.15):.2f}K"
        case "kelvin":
            if target_unit.lower() == "celsius":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {(measurement - 273.15):.2f}°C"
            elif target_unit.lower() == "fahrenheit":
                return f"A conversão de {measurement:.2f} {origin_unit} para {target_unit} é de: {((measurement - 273.15) * 9/5 + 32):.2f}°F"
            
print(celsius_fahrenheit_kelvin(100, "Celsius", "Fahrenheit"))
print(celsius_fahrenheit_kelvin(32, "Fahrenheit", "Celsius"))
print(celsius_fahrenheit_kelvin(273.15, "Kelvin", "Celsius"))
print(celsius_fahrenheit_kelvin(100, "Celsius", "Kelvin"))
print(celsius_fahrenheit_kelvin(212, "Fahrenheit", "Kelvin"))
print(celsius_fahrenheit_kelvin(373.15, "Kelvin", "Fahrenheit"))