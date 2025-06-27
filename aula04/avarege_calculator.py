def avarege_calculator(students_score: dict) -> str:
    response = ""
    for student, score in students_score.items():
        if not isinstance(score, (int, float)):
            raise ValueError(f"Score for {student} must be a number.")
        response += f"{student}: {score}\n"
        total = sum(students_score.values())
    average = total / len(students_score)
    response += f"Média das notas: {average:.2f}\n"

    return response

print(avarege_calculator({"Alice": 8.5, "Carlos": 9.0, "João": 7.8, "Maria": 9.2}))