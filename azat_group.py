# abc = 12345
# print(str(abc))

# your_name = input('name')
# if your_name == 'Admin':
#     print('welcome')
# else:
#     print('buy')


# validate_male = '@gmail.com'
# your_mail = str(input('your email'))
# if your_mail.endswith('@gmail.com'):
#     print('Succesful')
# elif your_mail.endswith('@email.com'):
#     print('elcome')

# your_password = input('Введиет пароль')


# a = input('Введиет увлечение')
# if not a:
#     print('Пиши что то')
# else:
#     print(a,'это круто')

# a = 2**3
# b = 3**2
# def batman(a,b):
#     if a > b:
#         return False
#     elif a < b:
#         return True
#     else:
#         return None
# print(batman(a,b))

# a = int(input('÷


# shet_na_tri = []


# num = int(input('Введите число'))
# def all(num):
#     if num % 3 == 0:
#         return ('Делиться без остатка')
#     elif num % 3 != 0:
#         return ('Не делиться без остатка')
#     if num % 2 == 0:
#         return ('Четное число')
#     elif num % 2 != 0:
#         return('Нечетное')
#     if num ** 2 == 1000:
#         return ('Можно получить 1000')
#     elif num ** 2 != 1000:
#         return ('нельзя получить')
# print(all(num))


# a = 10//5
# b = 10/5
# if a > b:
#     print('Н')
# elif a < b:
#     print('И')
# else:
#     print('W')
#     if a == b:
#         print(a,b)

    

# def dont_give_me_five(start,end):

#     return len([i for i in range(start,end) if '5' not in str(i)])

# print(dont_give_me_five(1,19))

# num = int(input('Введите любое число'))
# def poland(num):
#     if num > 0:
#         return 'Это положиетольное число'
#     else:
#         return 'Это отрицательное число '
# print(poland(num))
# age = int(input('Укажите возраст'))
# def club(age):
#     if age > 18 or age == 18:
#         return 'Чувак заходи'
#     elif age < 4 or age < 18:
#         return 'Ребенок или несовершеннолетний'
# print(club(age))

per = int(input('First num'))
vtor = int(input('second num'))
def oper(per,vtor):
    if per > vtor:
        return per,'больше чем',vtor
    elif per < vtor:
        return per,'меньше чем',vtor
    else:
        return per,'и',vtor,'равны'
print(oper(per,vtor))
