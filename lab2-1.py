print("\nПрограмма для перевода миль в километры")
error_message1 = "Требуется ввести положительное число"
while True:
    try:
        mi = float(input("\nРасстояние (ми): "))
        if mi > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
km = mi*1.60934
print("Расстояние к километрах равно",km)