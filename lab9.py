studentList=["Вася","Петя"]
evaluations=["0","0"]
while True:
    answer=int(input("выберите действие\n1-добавить студента\n2-удалить студета\n3-посмотреть весь список студентов и оценок\n4-поставить оценку студенту\n0-выйти из программы\n"))
    if answer not in [1,2,3,4,0]:
        print("такой команды нет")
        continue
    elif answer==1:
        newStudent = input("введите имя студента")
        studentList.append(newStudent)
        evaluations.append("0")
    elif answer==2:
        delNumber=int(input("введите номер студента для удаления"))
        studentList.pop(delNumber)
        evaluations.pop(delNumber)
    elif answer==3:
        print(studentList)
        print(evaluations)
    elif answer==4:
        numStudent=int(input("введите номер студента для выставления оценки"))
        meaningEvaluations=input("введите оценку")
        evaluations[numStudent]=meaningEvaluations
    elif answer==0:
        break