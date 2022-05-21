#zadanie 3
# modified = '''исследователи ESET с()()бщили/чт() в наст()ящее время активн()сть xDSpy прекратилась/
# и пр()из()шл() эт() п()сле предупреждения/ ()публик()ванн()г() бел()русским cert в феврале текущег() г()да!
# П() сути/ т()гда эксперты ()бнаружили ()дну из вред()н()сных кампаний хакер()в/ к()т()рая и была детальн() ()писана в д()кументе!
# именн() инф()рмация бел()русск()г() cert стала ()тправн()й т()чк()й для начала расслед()вания eset и п()м()гла аналитикам ()бнаружить пр()шлые ()перации XDSpy!'''
# def gucci(modified):
#     return modified.replace('()','о')
# print(gucci(modified))
#xadanie  6
# words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопк    у',]
# def sum(words):
#     for i in words:
#         if str(i)[0::] == str(i)[::-1]:
#             return i
# print(sum(words))

 # Задача 5:
   # Напишите программу для слияния нескольких словарей в один.
# my_friends = {
#        "Joomart": "+996555246810",
#        "Adinai": "+996555013579",
#        "Ermek": "+996777013579",
#        "Atai": "+996777246810",
#        "Aslan": "+996999246810",
# }
# his_her_friends = {
#        "Lyazat": "+996551123456",
#        "Salavat": "+996552234567",
#        "Daniyar": "+996553345678",
#        "Bolot": "+996554456789",
#        "Alymbek": "+996555501234",
#        "Dastan": "+996556678912",
#        "Maksat": "+996557789012",
#        "Aibek": "+996558890123",
# }
# our_friends = {}
# def anti_rasizm(my_friends,his_her_friends):
#     our_friends.update(my_friends)
#     our_friends.update(his_her_friends)
#     return our_friends
# print(anti_rasizm(my_friends,his_her_friends))





#prehakaton 
# 3 zadanoie

# from lib2to3.pytree import convert


# nuggets = '4729461084'
# num = []
# num2 = []
# def deb(nuggets):
#     l=','.join(nuggets)
#     s=l.split(',') 
#     for i in s:
#         num.append(int(i))
#     return sum(num)
# print(deb(nuggets))\


###########################################0000000##########################
a = [1,7,5,3,1]
print(a[3])
#Что больше: Количество троек в числе 17531 или число 5821?
first = '17531'
second = 5821
count_3 = 0
for i in first:
    if i == '3':
        count_3 = count_3 + 1
if count_3 > second:
    print(count_3, ' больше')
elif second > count_3:
    print(second, 'меньше ноликов')
else:
    print(count_3, ' равно ', second)
 # 2.Если остаток деления 4388 на 7 больше или равно 4 - умножьте остаток на 7.
    if 4388 % 7 >= 4:
      print((4388 % 7) * 7)
 #3.Если остаток деления 4292 на 5 меньше или равно 3 - разделите остаток на 3.
    if 4292 % 5 <= 3:
        print((4292 % 5) / 3)

# #4.Распишите по порядку шаги исполнения выражения: 7 + 5 * (3 * (27**3))
# first. (27**3)
# second. * 3
# thirth. * 5
# fourth. + 7
#Сколько получится если:    
a = 183 - 17
print(a)
b = a / 19
print(b)
c = b + 13.6
print(c)
d = c * 2
print(d)
v = d % 12
print(v)