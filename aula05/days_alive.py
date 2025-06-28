import datetime

def days_alive(date_born: datetime) -> str:
    today = datetime.datetime.now()
    days_alive = (today - date_born).days
    return f"Você está vivo há {days_alive} dias!"

print(days_alive(datetime.datetime(1997, 2, 24)))  # Exemplo de data de nascimento