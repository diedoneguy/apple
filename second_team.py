# Первое Задание
# Выведите числа из списка, которые больше предыдущего
a = [1,2,2,1,6,4,7,8,6,5]
c = []
b=[2,6,7,8]
for i in range(len(a) -1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(c)
# for i in range(len(b) -1):
#     n = a[i]
#     i +=1
#     m = a[i]
#     if n > m:
#         c.append(m)
# print(c)
# Второе Задание
# Сгенеруйте 300 чисел, пусть цикл прекратится на цыфре 254, и каждая цыфра должна быть четной
# i = 0
# xeon = []
# while i < 300:
#     i +=2
#     if i == 258:
#         break
#     print(i)
# car = ['Лексус','Тайота']
# print(car)
# cars = input('Марка автомобиля: ') 
# year = ['2004','2002']
# print(year)
# years = input('Год выпуска: ')
# km = ['150000']
# print(km)
# kms = input('Пробег макс: ')
# rule = ['Левый / Правый']
# print(rule)
# rules = input('Сторона руля: ')



# car = ['Лексус','Тайота']
# print(car)
# cars = input('Марка автомобиля: ')
# if cars == 'Лексус' or cars == 'Тайота':
#     year = ['2004','2002']
#     print(year)
#     years = input('Год выпуска: ')
# else:
#     print('Такой машины нет')  
#     if years == '2004' or years < '2002':
#         km = ['150000']
#         print(km)
#     else:
#         print('Мне не нужен хлам')
#         kms = input('Пробег макс: ')
#         if kms == '150000' or kms < '150000':
#             rule = ['Левый / Правый']
#             print(rule)
#             rules = input('Сторона руля: ')

for i in range(1,10):
    if i % 2 ==0:
        print(i)




