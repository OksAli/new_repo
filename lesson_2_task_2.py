def is_year_leap(year):
    return "True" if yers % 4 == 0 else "False"

yers = int(input("Введите год: "))
result = is_year_leap(yers)
print(f"Год {yers} : {result}")
    
