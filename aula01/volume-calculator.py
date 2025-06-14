def volume_calculator(x:float, y:float, z:float, measure:str)->str:
    return f"{x * y * z}{measure}³"

print(volume_calculator(12,14,20,"cm"))