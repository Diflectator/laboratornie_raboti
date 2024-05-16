import turtle
print("\nРисование квадрата\n")
error_message1 = "Требуется ввести целое положительное число"
while True:
    try:
        size = int(input("Введите сторону квадрата: "))
        if size > 0:
            break;
        else:
            print(error_message1)
    except ValueError:
        print(error_message1)
turtle.shape("arrow")
turtle.speed(1)
turtle.color("red")
turtle.penup()
turtle.backward(size/2)
turtle.right(90)
turtle.forward(size/2)
turtle.pendown()
for i in range(4):
    turtle.left(90)
    turtle.forward(size)
input("Нажмите любую клавишу")