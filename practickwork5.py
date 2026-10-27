#  ЦИКЛ FOR

# № 1

# for x in range(1,11):
#     print(x)

# № 2

# for x in range(2,51,2):
#     print(x)

# № 3

# for x in range(10,0,-1):
#     print(x)

# № 4

# n = int(input("Введите число: "))
# summ = 0
# for x in range(1,n+1):
#     summ = summ + x
# print(summ)

# № 5

# n = int(input("Введите число: "))
# a = 1
# for x in range(1,n+1):
#     a = a * x    
# print(f"Факториал {n} равен {a}") 

# № 6

# n = int(input("Введите число: "))
# k = 0
# for x in range(1,11):
#     c = x * n
#     k += 1
#     print(f"{n} на {k} = {c}")

# № 7
# x = [-1,-2,1,2,-3,-4,4,5,3,]
# k=0
# for i in x:
#     if i > 0:
#         k+=1
# print(f"Количество положительных чисел {k}")

# № 8

# a = str(input("Введите слово: "))
# a = a.lower()
# letter = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
# k = 0
# for x in a:
#     if x in letter:
#         k+=1
# print(f"Количество гласных букв {k}")

# № 9
# list=[10,2,3,4,5,6,7,8,9,1]
# a = sorted(list)
# for x in a:
#     pass
# print(f"Наибольший элемент: {x}")

# № 10

# for x in range(1,10):
#     for i in range(1,10):
#         result = x * i
#         print(f"{result:2}", end = " ")
#     print()

# ЦИКЛ WHILE 
# № 1
# a = 0
# while a <10:
#     a+=1
#     print(a)    

# № 2

# a = int(input("Введите число: "))
# k = 0
# while a != 0:
#     k = a + k
#     a = int(input("Введите число: "))
# print(k)

# № 3
# a = 12049
# b = a
# k = 0
# while b > 0:
#     k +=1
#     b = b//10
# print(f"Количесвто цифр в числе {a} равно {k}")

# № 4
# a = int(input("Введите натуральное число: "))
# k = 0
# while a > 0:
#     k += a % 10
#     a = a //10  
# print(f"Сумма цифр: {k}")

# № 5

# a = 1234
# k = 0
# while a > 0:
#     b = a % 10
#     k = k * 10 + b
#     a = a//10
# print(f"Перевёрнутое число: {k}")

# № 6

# a = int(input("Введите число n: "))
# b = 1
# while b <= a:
#     print(b)
#     b = b * 2

# № 7

# a = 11111
# b = int(input("Введите пароль(5 символов): "))

# while a != b:
#     print("Неверный пароль, попробуйте ещё раз")
#     b = int(input("Введите пароль(5 символов): "))
# print("Верный пароль")

# № 8

# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
# limit = min(n1,n2)
# a = 1
# nod = 1
# while a < limit:
#     if n1 % a == 0 and n2 % a == 0:
#         nod = a
#     a += 1
# print(f"НОД равно {nod}")

# # № 9
# n = int(input("Введите число: "))
# a = 0
# b = 1
# while b <= n:
#     print(b)
#     a,b = b, a+b

# № 10
# import random
# print("Игра угадай число от 1 до 100")
# chislo = random.randint(1,101)
# k = 0
# while True:
#     otvet = int(input("Введите число: "))
#     if otvet < chislo:
#         print("Не угадал! Загаданное число больше")
#         k +=1
#     elif otvet > chislo:
#         print("Не угадал! Загаданное число меньше")
#         k+=1
#     else:
#         print(f"Угадал! Загаданное число: {chislo}")
#         print(f"Количество попыток: {k}")

# Словари

# № 1

# name = {'Ваня': 2, 'Дима': 5, 'Петя': 4}
# print(name['Ваня'])

# № 2
# name = {'Ваня': 2, 'Дима': 5, 'Петя': 4}
# name.update({'Прохор':3})
# name['Ваня'] = 5
# del name['Ваня']
# print(name)

# № 3

# name = {'Ваня': 2, 'Дима': 5, 'Петя': 4, 'Прохор': 5}
# a = name.get('Прохор', 'Нет такого ключа')
# print(a)

# № 4

# name = {'Ваня': 2, 'Дима': 5, 'Петя': 4,}
# print(f"Ключи словаря {name.keys()}")
# print(f"Значения словаря {name.values()}")
# print(f"Длина словаря {len(name)}")

# № 5

# korzina = {'bread': '2$', 'milk': '3$', 'water': '4$', 'fish': '10$', 'meat':'20$'}
# for key, value in korzina.items():
#     print(f"{key:5} - {value:3}")

# № 6

# korzina = {'bread': 2, 'milk': 3, 'water': 4, 'fish': 10, 'meat':20}
# print(f"Сумма всех цен {sum(korzina.values())}")
# print(f"Самый дорогой товар {max(korzina, key=korzina.get)}")

# № 7

# b = "Яблоко АНАНАС банан 8"
# k = 0
# a = {}
# alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890"
# for x in b.lower():
#     if x in alfavit:
#         k+=1
# a.update({'количество': k})
# print(a)

# № 8
# a = input("Введите строку: ")
# words = a.split()
# counts = {}
# for w in words:
#     counts[w] = counts.get(w, 0) + 1
# most_common = max(counts, key=counts.get)
# for w, c in counts.items():
#     print(f"{w}: {c}")
# print("Самое частое слово:", most_common)


# № 9

# a = {'a': 1, 'b': 2, 'c': 3}
# b = {v: k for k, v in a.items()}
# print(b)   


# № 10
country = ["Россия","Беларусь","Литва", "Латвия", "Эстония", "Италия", "Франция", "Великобритания"]
capital_city = ["Москва", "Минск", "Вильнюс", "Рига", "Таллин", "Рим", "Париж", "Лондон"]
quiz = dict(zip(country, capital_city)) 
#Zip - сшивает два объекта в один кортеж. 
# Например 
# a = [1,2,3], b = ["a","b","c"] превратится в [(1,"a"), (2,"b"), (3,("c"))]

while True:
    a = input("Введите название страны: ")
    if a in quiz:
        print(f"Столица {quiz[a]}")
        break
    else:
        print(f"Страны {a} нет в нашем списке")

