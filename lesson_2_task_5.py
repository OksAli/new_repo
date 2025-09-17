def month_to_season(num_mon):
    if 3 <= num_mon <= 5:
        return "Весна"
    elif 6 <= num_mon <= 8:
        return "Лето"
    elif 9 <= num_mon <= 11:
        return "Осень"
    elif 12 <= num_mon <= 2:
        return "Лето"
    
num_mon = int(input("Введите номер месяца (1-12): "))
print(month_to_season(num_mon))
