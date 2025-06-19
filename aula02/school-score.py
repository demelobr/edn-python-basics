def school_score(scores: list[float]) -> str:
    average, lowest, highest = 0.0, 0.0, 0.0
    for score in scores:
        if score < 0.0 or score > 10.0:
            raise ValueError("As notas precisam ser de 0.0 a 10.0!")
        else:
            average = sum(scores) / len(scores)
            lowest = min(scores)
            highest = max(scores)

    result = f"""
        As notas informadas foram: {', '.join(f'{score:.2f}' for score in scores)} \n
        A média das notas é: {average:.2f} \n
        A nota mais baixa é: {lowest:.2f} \n
        A nota mais alta é: {highest:.2f} \n
    """
    return result

print(school_score([7.5, 8.0, 6.5]))