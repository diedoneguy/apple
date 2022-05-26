# ############ 1 ################
# with open('users.txt','w') as proger:
#     login = input('Login: ')
#     password = input('Password: ')
#     with open('users.txt','a') as proger:
#         proger.write(f'Login: {login}\nPassword: {password}')
# proger.close()

# ############ 2 ################
# with open('dolce.txt','w') as milk:#создает папку долче тхт 
#     text = input('Введите текст ')
#     if 'w' in text: #если в тексте есть буква даблю
#         print('В тексте есть [w]')
#     elif 'w' not in text:
#         print('Тексте нет [w]')
#         with open('dolce.txt','w') as milk:# открываем этот тхт файл  пишеи либо читаем
#             milk.write(f'text: {text} ')
# milk.close()

# ############# 4 ###############

# with open('python3.txt','w') as amd1:
#     amd1.write('''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords, and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java''')
# amd1.close()
# with open('python3.txt','r') as amd2:
#     t_words = []
#     data = (amd2.read().split())
#     for i in data:
#         if 't' in i:
#             t_words.append(i)
#     amd2.close()
#     print(t_words)

############## 5 #############





# with open('database.txt', 'r') as files:
#     username = input('username: ')
#     password = input('password: ')
#     if username and password in files.read():
#         print('Username and password already exists')
#     else:
#         with open('database.txt', 'a') as files:
#             files.write(f'username: {username}\npassword: {password}\n')
#             print('Success!')
# files.close()


with open('image.txt','r') as photo:
    german = input('photo please ')
    if german in photo.read():
        print('user_name is not free')
    else:
        with open('image.txt','a')as photo:
            photo.write(f'photo {photo}')
            print('Succes')
photo.close()
    


    
    
