# ###################### 3 ####### вывести первый и последний элемент
# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# def itc(fruits):
#     return fruits[0],fruits[-1]
# print(itc(fruits))
# ###################### 1 ##### вывести элементы больше пяти
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# bigast = []
# def pogba(a):
#     for i in a:
#         if i > 5:
#             bigast.append(i)
#     return bigast
# print(pogba(a))
################## 1  # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# sign = str(input('Введите знак <+ - * :>: '))
# def calculator(number1,number2,sign):    
#     if sign == '+':
#         return number1 + number2
#     elif sign == '-':
#         return number1 - number2
#     elif sign == '*':
#         return number1 * number2
#     if sign == ':':
#         try:
#             answer = number1 / number2
#             print(answer)
#         except ZeroDivisionError:
#             return "Делить на 0 нельзя"
# print(calculator(number1,number2,sign))
############## 3 # Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.
# operat = input('1-permiteter\n2-square: ')
# long = int(input('Write long: '))
# def perimeter(long):
#     if operat == '1':
#         a = long * 4
#         return f'Периметр квадрата{a}'
#     elif operat == '2':
#         b = long * long
#         return f'Плашат квадрата {b}'
# print(perimeter(long))

################# 2 # digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# найти уникальнцю строку
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# digits2 = (113,118,-5,1,135,137,0,142,144,17,154,155,2,159,172)
# navi = (digits, digits2)
# for i in navi:
#     if len(set(i)) == len(i):
#         print (True)
#     else:
#         print(False)
#####  каждое число поделить на 9
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# # for i in digits:
# #     print(i // 9)
# def many(digits):
#     for i in digits:
#         yield i//9
# for i in  many(digits):
#     print(i)
######################################
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# bot1 = set(spisok_1)
# bot2 = set(spisok_2)
# def python(bot1):
#     bot2.difference(bot1)
#     return bot1
# print(python(bot1))
##############8
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# dva = []
# tri = []
# for i in numbers:
#     if i % 2 == 0:
#         dva.append(i)
#     if i % 2 != 0:
#         tri.append(i)
#         print(dva,tri)



# sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
# sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
# sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

# setarr = set(sequence_0)
# if len(sequence_0) == len(set(sequence_0)):#переконверт в сет так как они не повторяются и если обычный sequence == c конвертированым sequence то тру
#     print("Все элементы уникальны")
# elif len(sequence_0) != len(set(sequence_0)):
#     print("Есть одинаковые")

# sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
# if len(sequence_1) == len(set(sequence_1)):#ЕСЛИ ОБЫЧНЫЙ sequence == ПЕРЕКОНВЕРТРОВАННОМУ  В СЕТС sequence 
#     print('Посдедовательность уникальна')
# elif len(sequence_1) != len(set(sequence_1)):
#     print('Посдедовательность нифига не уникальна')

# sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# if len(sequence_2) == len(set(sequence_2)):
#     print('Последователность уникальна')
# elif sequence_2 != set(sequence_2):
#     print('Посдедовательность нифига не уникальна')

sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
for i in sequence_3:
    if (i) == set(i):
        print('Последователность уникальна')
    elif (i) != (set(i)):
        print('Посдедовательность нифига не уникальна')


        









