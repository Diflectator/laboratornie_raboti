print("\nПрограмма для подсчёта среднего арифметического 5 чисел")
error_message1 = "Требуется ввести положительное число"
while True:
    try:
        num = float(input("\nПервое число: "))
        if num > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
num_average = num
while True:
    try:
        num = float(input("Второе число: "))
        if num > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
num_average += num	
while True:
    try:
        num = float(input("Третие число: "))
        if num > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
num_average += num			
while True:
    try:
        num = float(input("Четвёртое число: "))
        if num > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
num_average += num			
while True:
    try:
        num = float(input("Пятое число: "))
        if num > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
num_average = (num_average+num)/5				
print("Среднее число равно",num_average)