print("\nПрограмма расчёта скорости")
additionally = 1
error_message1 = "Требуется ввести целое положительное число"
while True:
    try:
        s = int(input("\nРасстояние (км): "))
        if s > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
while True:
    try:
        t = int(input("Время (ч): "))
        if t > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
v = s / t
print("Скорость движения равна",v,"км/ч")