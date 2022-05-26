# ########### 1 ##########
# values = ["Razakov 32", 10, 1005, ["tables", "chairs"], 23.00]
# list = []
# def makaron(values):
#     try:
#         for i in set(values):#конвертируем в сет
#             if i:
#                 list.append(True)
#             else:
#                 list.append(False)
#         if all(list) == True: #может ли пройтись по некоторым масивом  в values елси да то тру
#             print('can converting')
#         elif all(list) == False: #если нет то фолс
#             print('cant converting')
#         return list
#     except:
#         print('Neformal man')
# print(makaron(values))

# ######## 2 #########
# banan = []
# orange = int(input('number1 pleace: '))
# apple = int(input('number2 pleace: '))
# melon = int(input('number3 pleace: '))
# straw = int(input('number4 pleace: '))
# cherry = int(input('number5 pleace: '))
# def amg(orange):
#     banan.append(orange)#в банан добавляем orange 
#     banan.append(apple)#в банан добавляем apple
#     banan.append(melon)
#     banan.append(straw)
#     banan.append(cherry)
#     return f'little number is: {min(banan)}' #возврашяем самый мелкий число из orange apple
# print(amg(orange))
# ############################################
# funks = ['add','update','remove','difference_update','pop']
# course = input('funk please ')
# def super(funks):
#     if course in funks:
#         return 'Такой фунции ЕСТЬ'
#     else:
#         return 'такой функции НЕТ'
# print(super(funks))

# ############################
# at = 10
# ni = 15
# wo = 20
# for e in range(-at, at):
#     print('wo / e')
#     if at > 5:
#         print('at > 5')
# ############################
# lst = []
# for i in range(10):
#     lst.append(i)
# a = list(reversed(lst))
# sls_obj = slice('0','8')
# print(lst,sls_obj)
# ############################
# a = 0
# b = 1
# numbers = []
# while b > a:
#     b += 1
#     numbers.append(b)
#     if a == b:
#         break
#     print(numbers)
# #############################
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for x in dict_.values():
#     print(x)

# channel = {'name':'Aktan','car':'Amg 63','gi':'Ma'}
# for i in channel.values(): #проходиться по переменной и выводит только словарь или ключь на выбор
#     print(i)

# #####################################
# banan = []
# orange = int(input('number1 pleace: '))
# apple = int(input('number2 pleace: '))
# melon = int(input('number3 pleace: '))
# straw = int(input('number4 pleace: '))
# cherry = int(input('number5 pleace: '))
# def amg(orange):
#     banan.append(orange)#в банан добавляем orange 
#     banan.append(apple)#в банан добавляем apple
#     banan.append(melon)
#     banan.append(straw)
#     banan.append(cherry)
#     return f'little number is: {min(banan)}' #возврашяем самый мелкий число из orange apple
# print(amg(orange))
#######################################
# from unicodedata import decimal


# money=int(input('summ pleace: '))
# def bank(money):
#     if money<50000:
#         print('our bank can give money bigast also ',money)
#     else:
#         print('ok so good ')
#         a=money*(3.47 / 100)
#         return round(a, 2)
# print(bank(money))
sum = []
i = 0
while i < 4:
    a = input('Введите число')
    i +=1
    if i == 4:
        sum.append(i)
        print(sum)
        break

