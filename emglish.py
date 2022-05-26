################################ 1 ###########
# import random
# i = 0
# command = []
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# while i < 4:
#     a = random.choices(names)
#     print(a) #выводить рандомно 4 имени но не добавит в команд
#     i +=1
#     if i == 4:
#         break
# pol = 0
# while pol < 4:
#     command.append(random.choice(names))#добавить 4 имени и добавит в команд
#     pol +=1
# print(command)
# hh = 0
# for i in range(4):
#     command.append(random.choice(names))
#     print(command)
#     import time
#     time.sleep(5)
# print(command)
#################################### 2 ###########
# import os
# print(os.name)
#################################### 3 ###########
# i = 0
# chery = []
# for i in range(5):
#     a=input('Write the text: ')
#     i +=1
#     chery.append(a)
#     if i == 5:
#         break
#     print(chery)
################################### 4 ##############
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]


# from random import shuffle, randrange
# a= ['Бегимай', 'Akhmad', 'Кылыч', 'Актан', 'Аскар', 'Равиль', 'Илим', 'Adil', 'Элдар', 'Алтынбубу', 'Айгерим', 'Чингиз', 'Artem']

# import os,random
# os.mkdir('Halal')
# i = 0
# while i < 4:
#     a = random.randint(0,100)
#     os.mknod(f'ok{a}.py')
#     print(a)
# NAMES = [
# "AIBEK", "JOOMART", "ADINAI", "ERMEK", "ATAI", "ASLAN", "LYAZAT", "SALAVAT", "DANIYAR", "BOLOTBEK", "ALYMBEK", "DASTAN", "MAKSAT"
# ]

# ПОВТОРЕНИЕ:

# ЗАДАНИЕ 1:

# ls = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# cd = []
# for i in range(len(ls) -1):
#     cd.append(ls[i]+ls[i+1])
# print(cd)
# print(ls[-1] + ls[1])
# for i in range(1, len(ls) - 1):
#     print(ls[i - 1] + ls[i + 1])
# print(ls[-2] + ls[0])
# # С ПОМОЩЬЮ ЦИКЛА ПРОЙДИТЕ ПО ЛИСТУ NUMBERS И ВЫВОДИТЕ НА ЭКРАН СУММУ ДВУХ СОСЕДНИХ ЧИСЕЛ.

# # ЗАДАНИЕ 2:
# # В PYTHON ЕСТЬ МОДУЛЬ DATETIME А В МОДУЛЕ ЕСТЬ ОСОБЕННЫЕ ФУНКЦИИ КОТОРЫЕ ПОКАЗЫВАЮТ НАСТОЯЩЕЕ ВРЕМЯ.
# # С ПОМОЩЬЮ МОДУЛЯ DATETIME ВЫВЕДИТЕ НА ЭКРАН СКОЛЬКО ВРЕМЕНИ В ДАННЫЙ МОМЕНТ.
# ###########################################

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# for i in range(1,len(names),4):
#     print(names[i:i+4])
#     if i 
# import os
# a = int(input('Text: '))
# b = os.urandom(a)
# print(a,b)
# import secrets
# import string
# pas = int(input('password len'))
# password = string.digits+string.ascii_letters#значит что справишает из чего пароль будет состоять данн момент из букв и цифр
# genetate = ''.join(secrets.choice(password)for i in range(pas))#через жойн получаем на пароль и секретно генерируем пароль 
# print(genetate)
import random
import string
import secrets
import time
a = random.randrange(1,12)
print(a)
p = 0
pas = int(input('len for password: '))
password = string.digits+string.ascii_letters
generate = ''.join(secrets.choice(password)for i in range(pas))
while p < 10:
    print(generate)
    time.sleep(4)
    print(generate)

    
