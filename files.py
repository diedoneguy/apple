# a = open('brawl.txt','w')#создает файл по именем 
# word = input('word :')#позволяет добавлять слова через инпут в наш файл
# a.write(word)
# a.close

with open('saimpat.txt','w') as storm:
    email = input('Введите @email')
    password = input('Введите пароль')
    with open('saimpat.txt','a') as storm:
        storm.write(f'email: {email}\npassword: {password}')
        print(storm)
# with open('Google.txt','r') as karatel:
#     username = input('юзер нейм ')
#     password = input('пассворд')
#     for i in karatel.readlines():
#         if i[10:-1] in username and i[10:-1] in password:
#             username = i.replace(username,'')
#             password = i.replace(password,'')
#             with open('Google.text','w')as karatel:
#                 karatel.write(f'username: {username}\n password: {password}')
# karatel.close()