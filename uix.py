# cars = {'Машины':['мерседес'],'Дома'   :['особняк']}
# print (cars)
# cars.update({'Спорт Кары':['астон' 'мартин' 'масерати' 'бугатти']})
# print(cars)
# cars.update({'Собаки':['овчарки','доберманы','питбули']})
# print(cars)
# cars.update({'Каналы':['cartoon network''nickelodeon']})
# print (cars)
# cars.update({'Игры':['gta5','mafia2','cod']})
# print (cars)
# cars.update({'Cartoons':['Adventure Time','Sponge Bob','Nicola','Barboskins']})
# print(cars)
# a = ['iphone','samsung','amg','MacBook']
# b = ['MacBook','China','AstonMartin','amg']
# c = []
# for i in a:
#     if i in b:
#         print(i)
# for j in b:
#     if j in a:
#         print(j)
# c = 0
# while True:
#     print(c)
#     c +=1
#     if c == 51:
#         break





# accounts = []
# login = input('Введите логин ')
# password = input('Введите пароль ')
# password2 = input('Повторите пароль ')
# if password != password2:
#     while password != password2:
#         print('Пароль не совпадает')
#         login = input('Введите логин ')
#         password = input('Введите пароль ')
#         password2 = input('Повторите пароль ')   
# elif password == password2 and login:
#     print('Аккаунт создан успешно')
#     accounts.append(login)
#     print(accounts)
    

# a = 21

# def round_to_next5(n):  
#     while n % 5 != 0:
#         n+=1
#     return n

# print(round_to_next5(a))

# def to_binary(n):
#     s = ''
#     while n != 0:
#         if n % 2 == 0:
#             s += '0'
#         else:
#             s += '1'
#         n = n//2
#     return s[::-1]

# print(to_binary(156))
# a = (i for i in range(1,1000))
# print(list(a))
# a = []
# i = 0
# while True:
#     print(i)
#     i +=1
#     if i == 50:
#         break
#     a.append(i)
#     print(a)
# class A:
#     def __run(self):
#         return 'run'
# a = A()
# print(a._A__run())


from django.forms import PasswordInput


user = {'aktan':12,
        'age':19,
        'height':178
}



# user.update({
#     'proffesions':'Python dev',
#     'game':'pubg'#добовляет в user 

# })
# # user.update({
# #     'profesions':'flutter'
# # })

# print(user)


# from traceback import print_exc


# user = {
#     '+996508080876':{
#         'name' : 'diedoneguy',
#         'age': 17,
#         'height':178,
#         'professions':'Python',
#         'cash':12222,
#         'car':'Mersedes gt63'
#     }
# }


# print(user['+996508080876']['car'])



# phone = input('Введите номер '),
# name = str(input('Ваша имя '))
# age = int(input('Укажите возраст '))
# height = int(input('Ваш рост '))
# profession = str(input('Ваша профессия '))
# cash = int(input('Ваш баланс '))
# car = str(input('Ваша машина '))

# user.update({
#     phone:{
#         'name':name,
#         'age':age ,
#         'height':height ,
#         'profession':profession,
#         'cash':cash,
#         'car':car
#     }
# })



# # user['+996508080876']['age'] = 12 ##########измененение ключа в user###########

# # print(user['+996508080876']['age']) ######берет из юзерс и выводит№№№№№№№№№

# print(user)
# o = (
#     '+996500', 
#     '+996501',
#     '+996502', 
#     '+996505', 
#     '+996507'
# )
# mega = (
#     '+996550',
#     '+996551',
#     '+996552',
#     '+996553',
#     '+996554',
#     '+996555',
#     '+996556',
#     '+996557',
#     '+996559',
#     '+996755',
#     '+996999'
# )
# beeline = (
#     '+996771',
#     '+996772',
#     '+996773',
#     '+996774',
#     '+996775',
#     '+996776',
#     '+996777',
#     '+996778',
#     '+996779',
#     '+996220',
#     '+996227'
# )
# phone = '+996500123456'
# # print(phone[0:7])
# # print(print('Количество цифр'),(len(phone)))
# if phone[0:7] in beeline:
#     print('это оператор Beeline')
# elif phone[0:7] in o :
#     print('это оператор O')
# elif phone[0:7] in mega:
#     print('Это оператор MegaCom')

# if phone.startswith('+996'):
#     print('KG номер')
# elif phone.startswith('+792'):
#     print('Moscow номер')
# elif phone.startswith('+742'):
#     print('Vladivostok номер')
# elif phone.startswith('+1'):
#     print('U.S.A номер')

# max_length = len(phone)
# print('Количество цифр =',max_length)

# base = {
#     'login':'a',
#     'password':'12345678'
    
# }
# a = int(input('Хай Bitches это крч банк хочешь зарегаться нажми на 1'
# 'хочешь авторизоавться то нажми на 2/n хочешь посмотреть на базу то на 3 жmи лол >>>'))
# if a == 1:
#     log = input('Введите логин ')
#     rasim1 = input('Введите пароль не меньше 8 ми символов ')
#     rasim2 = input('Повторите пароль пожалуйтса')
#     while len(rasim1) < 8 and rasim1 == rasim2:
#         print('Ты че тупой сказал же больше 8ми символов,либо ты неправильно ввел число лол ')
#         log = input('Введите логин')
#         rasim1 = input('Введите пароль не меньше 8 ми символов ')
#     if rasim1 == 8 and rasim1 > 8:
#         print('Лох аккаунт создан успешно лол')

#     base.update({
#     'login':log,
#     'password':rasim1
#     })
#     print(base)
# if rasim1 in base:
#     print('этот пароль занят')


# def square(x):
'''
#     print('Квадрат числа', x ,'=', x**2)
# for i in range(1,11):
# (square(i)
'''
# def funk(abc):   
#     a = '123456789'
#     for i in abc:

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# oper = str(input('Введите операцию: '))
# def calculator(num1,num2,oper):
#     if oper == '+':
#         return num1 + num2
#     elif oper == '-':
#         return num1 - num2
#     elif oper == '*':
#         return num1 * num2
#     elif oper == '//':
#         return num1 // num2
#     if num1 == 0 // num2:
#         return '0 не делиться'
# print(calculator(num1,num2,oper))
# print(len(input('Введите что то')))


# i = 0
# boot = True
# while boot:
#     if i == 2:
    
#     print(i,'bitch')
#     i = i + 1
#     if i == 10:
#         break
# i = 0
# while True:
#     if i == 3:
#         i +=1
#         continue
#     print(i,'bitch')
#     i +=1
#     if i == 10:
#         break
# print('Добро пожаловать')
# password = input('Введите пароль')
# password2 = input('Введите парол еше раз')
# while password != password2:
#     print('Пароль веден неправильно')
#     password = input('Введите пароль')
#     password2 = input('Введите парол еше раз')
# if password == password2:
#     print('Аутентификация прошла успешно')
    
# while True:
#     num1 = int(input('Введите число'))
#     num2  = int(input('Ввелите второе число'))
#     z = str(input('Введите знак'))
#     if z == '+':
#        print(num1 + num2)
#     elif z == '-':
#         print(num1 - num2)
#     elif z == '*':
#         print(num1 * num2)
#     elif z == ':':
#         print(num1 // num2) 
symbols = ('!','@','$','%','+','=','-','.','/','~',':','|')
password1 = input('Введите пароль: ')
password2 = input('Подвердите пароль: ')    
def confifrim_password(password1,password2):
    for i in password1:
        if i in symbols:
            return 'Пароль не должен содержать знаков'
    if password1 == password2:
        return 'Вы авторизовались успешно'
    elif password1 != password2:
        return 'Пароль введен неправильно,повторите попытку'
print(confifrim_password(password1,password2))


