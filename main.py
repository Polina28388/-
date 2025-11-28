print("Привет,")
print("Сыиграем в игру!")
print("Давай посмотрим как ты провёл свой день.")
print("У тебя есть 3 категории: здоровье, выносливость, сила")
print("Ты можешь как заработать балл  за категорию за какое то действие,")
print("так и проиграть.")
print("В начале у тебя есть:")
z=5
v=5
s=5
print("Здоровье -",z)
print("Выносливость -",v)
print("Сила -",s)
print("Квест закончиться, когда ты ответишь на все вопросы")
print("Если ты наберёшь в какой то категории 10 или больше баллов, ты выиграешь,")
print("либо проиграешь")
print("")
def itog(z,v,s):
    if z>=10 or v>=10 or s>=10:
        print("Ты выиграл!")
    else:
        print("Ты проиграл!")
print("Придумай имя своему персонажу")
name=input()
print("Сколько часов ты сегодня спал?")
son=int(input())
if son>=6:
    print("Проверим твою удачу",name,"сегодня")
    print("Напиши любую цифру от 0 до 3")
    balli=int(input())
    sum1=0
    for i in range(balli):
        sum1+=i
        z+=i
        s+=i
    print("+",sum1,"здоровье")
    print("+",sum1,"сила")
else:
    z-=1
    s-=1
    print("-1 здоровье")
    print("-1 сила")
print("")
print("Здоровье -",z)
print("Выносливость -",v)
print("Сила -",s)
print("")
print("Завтракал ли ты утром?")
zavtrak=input()
if zavtrak=="Да" or zavtrak=="да":
    v+=1
    s+=1
    print("+1 выносливость")
    print("+1 сила")
else:
    v-=1
    s-=1
    print("-1 выносливость")
    print("-1 сила")
print("")
print("Здоровье -",z)
print("Выносливость -",v)
print("Сила -",s)
print("")
print("Заправил ли ты утром кровать?")
krovati=input()
if krovati=="Да" or krovati=="да":
    z+=1
    v+=1
    print("+1 здоровье")
    print("+1 выносливость")
else:
    z-=1
    v-=1
    print("-1 здоровье")
    print("-1 выносливость")
print("")
print("Здоровье -",z)
print("Выносливость -",v)
print("Сила -",s)
print("")
print(name,",сейчас у тебя будет возможность получить бонусные баллы за решение примеров")
print("+1 балл к здоровью, если решишь пример")
print("123+324=?")
otvet1=int(input())
if otvet1==447:
    z+=1
    print("+1 здоровье")
    print("")
else:
    print("Неправильно")
    print("")
print("+1 балл к выносливости, если решишь пример")
print("(43+57)*65/5=?")
otvet2=int(input())
if otvet2==1300:
    v+=1
    print("+1 выносливость")
    print("")
else:
    print("Неправильно")
    print("")
print("+1 балл к силе, если решишь пример")
print("32+5*6-6*4/2=?")
otvet3 = int(input())
if otvet3 == 50:
    s+=1
    print("+1 сила")
    print("")
else:
    print("Неправильно")
    print("")
print("Здоровье -", z)
print("Выносливость -", v)
print("Сила -", s)
print("")
print(name,"отгадай загадку")
print("Без голоса, но всех будит,")
print("Не свет, но гонит прочь туман.")
print("Он в каждом утреннем прибое,")
print("Хоть не вода и не океан.")
zagatka=input()
if zagatka=="Рассвет" or zagatka=="рассвет":
    z+=1
    v+=1
    s+=1
    print("+1 здоровье")
    print("+1 выносливость")
    print("+1 сила")
    print("")
else:
    print("Неправильно")
    print("")
print("Здоровье -", z)
print("Выносливость -", v)
print("Сила -", s)
print("")
print("+1 балл к здоровью, если решишь ")
print("Введи любе число от 1 до 40")
spisok_1=[]
chislo_1=int(input())
for i in range(1,100,chislo_1):
    spisok_1+=[i]
print(name,", сколько чисел вывелось?")
print(spisok_1)
otvet_1=int(input())
if otvet_1==len(spisok_1):
    z+=1
    print("+1 здоровье")
    print("")
else:
    print("Неправильно")
    print("")
print("+1 балл к выносливости, если решишь ")
print("Введи любе число от 1 до 40")
spisok_2=[]
chislo_2=int(input())
for i in range(1,100,chislo_2):
    spisok_2+=[i]
print("Сколько чисел вывелось?")
print(spisok_2)
otvet_2=int(input())
if otvet_2==len(spisok_2):
    v+=1
    print("+1 выносливость")
    print("")
else:
    print("Неправильно")
    print("")
print("+1 балл к силе, если решишь ")
print("Введи любе число от 1 до 40")
spisok_3=[]
chislo_3=int(input())
for i in range(1,100,chislo_3):
    spisok_3+=[i]
print("Сколько чисел вывелось?")
print(spisok_3)
otvet_3=int(input())
if otvet_3==len(spisok_3):
    s+=1
    print("+1 сила")
    print("")
else:
    print("Неправильно")
    print("")
print("Здоровье -", z)
print("Выносливость -", v)
print("Сила -", s)
print("")
print("До университета ты добрался пешком?")
doroga=input()
if doroga=="Да" or doroga=="да":
    z += 1
    v += 1
    print("+1 здоровье")
    print("+1 выносливость")
else:
    z -= 1
    v -= 1
    print("-1 здоровье")
    print("-1 выносливость")
print("")
print("Здоровье -",z)
print("Выносливость -",v)
print("Сила -",s)
print("")
print(name,"! Ты проснулся по первому будильнику, сразу встал?")
budilnik=input()
if budilnik=="Да" or budilnik=="да":
    v+=1
    s+=1
    print("+1 выносливость")
    print("+1 сила")
else:
    v -= 1
    s -= 1
    print("-1 выносливость")
    print("-1 сила")
print("")
print("Здоровье -", z)
print("Выносливость -", v)
print("Сила -", s)
print("")
print("Сколько пар у тебя уже прошло?")
pari=int(input())
if pari<3:
    v+=1
    s+=1
    print("-1 выносливость")
    print("+1 сила")
else:
    v -= 1
    s -= 1
    print("+1 выносливость")
    print("-1 сила")
print("")
print("Здоровье -", z)
print("Выносливость -", v)
print("Сила -", s)
print("")
print("Квест закончился")
print(name,",")
print(itog(z,v,s))
