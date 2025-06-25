def leap_yaer_calculator(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leap_yaer_calculator(2020))  # True
print(leap_yaer_calculator(2021))  # False