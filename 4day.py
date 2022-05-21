# #problem 0
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# def look(dates_of_birth):
#     dates_of_birth.add('7') #добавит 7
#     dates_of_birth.discard('7') #удалит 7
#     return dates_of_birth
# print(look(dates_of_birth))

# #problem 1
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# def tank(farm_1,farm_2):
#     farm_1.intersection_update(farm_2) #сравнил 2 сетс и вернул что есть и в лист1 и в лист2
#     return farm_1
# print(tank(farm_1,farm_2))

# #problem 2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# def tank2(farm_1,farm_2):
#     farm_2.difference(farm_1)
#     return farm_2
# print(tank2(farm_1,farm_2))

#problem 3
# set ={'Lamborghini','Ferrari','Lexus'}
# def claim(set):
#     set.add('Aston')
#     set.pop()
#     return set
# print(claim(set))

#problem 000    problem 10
# menu = {'Лагман': 120, 
#         'Плов': '120', 
#         'Боршь': 100}
# menu1 = set(menu)        
# def food(menu):
#     menu.update({'Беш-Бармак' : 130}) #добавит бешбармак
#     menu.update({'Беш-Бармак' : 135}) #удалить бешбармак
#     menu.pop('Боршь') #удалит боршь#
#     menu.update({'Напитки': ['Coca-Cola', 'Sprite', 'Fanta']})
#     return menu
# print(food(menu))

#problem 020
# set = {'update','remove','add','pop','clear','difference'}
# dict = {'clear','update','keys','get'}
# def vs(set,dict):
#     set.intersection_update(dict) #вернул что есть в сет и в дикт
#     dict.difference(set)
#     return  f'В set и в dict есть {set} В dict нет {dict}'
# print(vs(set,dict))

#probem 27
# i = 0
# empty = {}
# def identificate(empty):
#     name = input('Введите имя ')
#     job = input('Профессия ')
#     empty.update({name:job})
#     return f'Привет {empty.keys()} ты {empty.values()} это круто'
# print(identificate(empty))

#problem 11
# south_american_countries = ['Argentina', 
#                             'Bolivia','Brazil', 
#                             'Chile','Colombia', 
#                             'Ecuador','Guyana', 
#                             'Paraguay','Peru', 
#                             'Suriname','Suriname', 
#                             'Uruguay','Venezuela']
# def ukraine(south_american_countries):
#     return set(south_american_countries)#переобредилили в сетс так как сетс не добускает дубликатов
# print(ukraine(south_american_countries))




