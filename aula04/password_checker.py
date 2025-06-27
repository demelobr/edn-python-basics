def password_checker(password: str) -> bool:
    if len(password) < 8:
        return False
    
    have_number = False

    for digit in password:
        if digit.isdigit():
            have_number = True
            break
    if not have_number:
        return False

    return True

print(password_checker("12345678"))  # True
print(password_checker("abcdefgh"))  # False