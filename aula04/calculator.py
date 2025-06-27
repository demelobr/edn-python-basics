def calculator(operation: str, operator_one: float, operator_two: float) -> float:
    match operation:
        case "+":
            return operator_one + operator_two
        case "-":
            return operator_one - operator_two
        case "*":
            return operator_one * operator_two
        case "/":
            if operator_two == 0:
                raise ValueError("Cannot divide by zero.")
            return operator_one / operator_two

print(calculator("+", 5, 3))  # Output: 8
print(calculator("-", 5, 3))  # Output: 2
print(calculator("*", 5, 3))  # Output: 15
print(calculator("/", 5, 3))  # Output: 1.6666666666666667
print(calculator("/", 5, 0))  # Raises ValueError: Cannot divide by zero.