print("\nПрограмма проверка лимита")
error_message1 = "Введите положительное число"
limit = 60
while True:
    try:
        speed = float(input("\nВведите свою скорость (км/ч): "))
        if speed > 0:
            if speed <= limit:
                print("Можете ехать дальеше")
            else:
                print("Вы превысили скоростной режим",limit,"км/ч")
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)