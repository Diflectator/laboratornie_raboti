print("\nПрограмма перевода стоимости валюты")
error_message1 = "Введите положительное число"
error_message2 = "Введите допустимое название валюты"
while True:
    try:
        money = float(input("\nВведите сумму в рублях: "))
        if money > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
while True:
    try:
        currency = input("Введите валюту для перевода (USD, EUR, RMB): ")
        if currency == "USD":
            money2=91.26
            break;
        elif currency == "EUR":
            money2=98.83
            break;
        elif currency == "RMB":
            money2=12.61
            break;
        else:
            print(error_message2)
    except ValueError:
        print(error_message2)
money2=money/money2
money2=round(money2, 2)
print(money,"рубля стоят",money2,"в указанной валюте")