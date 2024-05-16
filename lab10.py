import random
print("\nТипо голосовой помошник\n")
questions=["Какие вопросы можно задавать?","Столица Финляндии","Когда Вторая Пчелиная война?"]
answers0=["Какие вопросы можно задавать?","Столица Финляндии","Когда Вторая Пчелиная война?"]
answers1=["Хельсинки","Москва","Париж"]
answers2=["Нет","Её не будет","..."]
answers3=["А можно другой вопрос","Дальше","Лучше спросите какие вопросы можно задавать"]
q1=input("Введите вопрос, а я отвечу (для выхода напишите Выход): ")
while q1!="Выход":
    ran=random.randint(0,2)
    if q1==questions[0]:
        answ=answers0[ran]
    elif q1==questions[1]:
        answ=answers1[ran]
    elif q1==questions[2]:
        answ=answers2[ran]
    else:
        answ=answers3[ran]
    print(answ)
    q1=input("Давайте следующий вопрос: ")