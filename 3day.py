#problem 1
# list1 = ['mersedes','bmw','maserati']
# list2 = ['honda','buggati']
# def moon(list1,list2):
#     list1.append(list2)
#     list1.extend(list2)
#     return list1
# print(moon(list1,list2))

#problem 2
# tuple = ('aktan','aman','atai')
# def call(tuple):
#     return tuple[2]# выводит атая так как он 2 по индексу
# print(call(tuple))

#problem 3
# a = ['macbook','atai']
# b = ''
# def app(a):
#     c = b.join(a)
#     return c
# print(app(a))

#problem 4
# listok1 = ['Atai is']
# listok2 = ['hero']
# def crasy_boy(listok1,listok2):
#     listok1.extend(listok2)
#     return listok1
# print(crasy_boy(listok1,listok2))

#problem 5
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# def foggy(names):
#     return names.count('Jack')    # считаем сколько раз всречается имя джон
# print(foggy(names))

#problem 6
# names = ['Jack','Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# def flex(names):
#     names.append('Oskar')
#     names.pop(-1)
#     return names
# print(flex(names))

#problem 7
# bio = []
# name = input('Ваше имя: ')
# brirth_day = input('Год рождение: ')
# lang = input('Любимый язык: ')
# def passport(bio):
#     bio.append(name)
#     bio.append(brirth_day)
#     bio.append(lang)
#     return bio
# print(passport(bio))

#problem 8
# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# def index(pythonList):
#     index = pythonList.index('loop')
#     rem = pythonList.pop(6)
#     return index,rem,pythonList
# print(index(pythonList))

#problem 9
# numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# def poling(numbers):
#     for i in numbers:
#         if i > 10:
#             s = numbers[0]*numbers[1]*numbers[2]*numbers[3]*numbers[4]*numbers[5]*numbers[6]*numbers[7]*numbers[8]*numbers[9]*numbers[10]*numbers[11]
#         return s
# print(poling(numbers))#каждое умножил на дру на друга но оренитровка по индексу

#problem 10
from operator import le


spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
sp = []
l = []
for i in spisok_1:
    convert = str(i)
    if convert.isalpha():
        sp.append(i)
    else:
        l.append(i)
print(sp,l)
for i in spisok_2:
    convert = str(i)
    if convert.isalpha():
        sp.append(i)
    else:
        l.append(i)
print(sp,l)




# def shadow(element):
#     letters = 0
#     numbers = 0
#     for char in element:
#         if char.isdigit():
#             numbers +=1
#         elif char.isalpha():
#             letters +=1
#     return letters, numbers     
# print(shadow(spisok_1))
            
# word = input('word number: ')
# a = []
# def qwe(word):
#     a.append(word)
#     elem = a * 5
#     return a, 'count:', len(elem)
# print(qwe(word))
# bash = []
# for i in range(1,10):
#     print (int(i[0,8]))

    

    

