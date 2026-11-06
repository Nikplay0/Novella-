import random
print("ЭПИДЕМИЯ ЧУМЫ")
print("Иркутск. Обычный осенний день. Дима спокойно гулял по городу. Внезапно раздался звук сирены! \nГолос из рупора: ВНИМАНИЕ! ОБЪЯВЛЕН КАРАНТИН!\nПричина карантина - неизвестная чума.")
input("Нажмите Enter чтобы продолжить.... \n")
print("Прошел месяц...\nУлицы Иркутска опустели. Повсюду брошенные автомобили и здания. \nСвязь полностью пропала. В городе появились чумные. \nПосле укуса человек сразу превращается в чумного.\nДима решил найти лекарство и спасти город.")
input("Нажмите Enter чтобы продолжить.... \n")
character = {'health': 5, 'food': 2, 'firstmidkit': 1, 'weapon': None}

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: нет.")
print("Дима собирает походный рюкзак.\nОн может взять один из инструментов")
print("1 - Топор\n2 - Нож\n3 - Монтировка")
a = input("Выбери предмет: ")
if a == "1":
        character['weapon'] = 'Топор'
        print("Дима взял топор.")
elif a == "2":
     character['weapon'] = 'Нож'
     print("Дима взял нож.")
elif a == "3":
     character['weapon'] = 'Монтировка'
     print("Дима взял монтривку.")
else:
     print("Дима отправился без оружия.")
     character['weapon'] = None
input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("Дима вышел из дома и услышал странный звук.\nИз-за машины появился чумной!")
print("1 - Сражаться\n2 - Убежать")
b = input("Твой выбор: ")
if b == "1":
    if character["weapon"] != None:
        print("Дима отбился от чумного!")
    else:
        character['health'] -= 1
        print("Дима отбился, но получил ранение.")
else:
    print("Дима убежал через соседний двор.")
input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("Дима нашел заброшенный магазин.\nНа полках остались некоторые припасы.")
print("1 - Взять еду\n2 - Взять аптечку")
a = input("Что взять? ")
if a == "1":
    character['food'] += 2
    print("Дима нашел две порции еды.")
elif a == "2":
    character['firstmidkit'] += 1
    print("Дима нашел аптечку.")
else:
    print("Дима ничего не взял.")
input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("На выходе из магазина появились разбойники.\nОни потребовали отдать еду")
print("1 - Отдать еду\n2 - Попытаться убежать")
b = input("Твой выбор: ")
if b == "1":
     if character['food'] > 0:
         character['food'] = None
         print("Разбойники забрали еду и отпустили Диму.")
         print(f"Еда: {character['food']}")
     else:
        character['health'] -= 1
        print("Разбойники разозлились и ударили Диму.")
else:
     character['health'] -= 1
     print("Дима сбежал, но поранился.")
input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("Дима заметил здание старой больницы.\nИзнутри доносились крики о помощи.")
print("1 - Зайти внутрь\n2 - Осмотреть здание")
a = input("Твой выбор: ")
input("Нажмите Enter чтобы продолжить....\n")

if a == "1":
    print("Дима зашел внутрь и встретил врача.")
else:
     print(f"Еда: {character['food']} Аптечки: {character['firstmidkit']} Здоровье: {character['health']} Оружие: {character['weapon']} ")
     print("Пока, Дима обходил больницу, он нашёл заброшеную машину в которой лежали две аптечки ")
     character['firstmidkit'] += 2
     print("Дима обошел больницу и нашел черный вход.\nВнутри он встретил выжившего врача.")
     input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("Врач: Меня зовут Андрей.\nРаньше здесь изучали неизвестную вид чумы. Один ученый, возможно, знает способ как её остановить.\nЕго зовут Станислав. Последний раз его видели в ратуше - путь туда очень опасен! \nДима решил найти загадочного ученого.")
print("Дима проверил припасы и приготовился к дороге.")
input("Нажмите Enter чтобы продолжить....\n")

print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
print("Дима вышел из больницы. Впереди виднелась дорога к центральной ратуше.\nОн поправил рюкзак и продолжил путь. ")
print(f"Еда: {character['food']}. Аптечки: {character['firstmidkit']}. Здоровье: {character['health']}. Оружие: {character['weapon']}.")
input("Нажмите Enter чтобы продолжить....\n")

# 2 часть
print("Но внезапно впереди раздался громкий крик...")
