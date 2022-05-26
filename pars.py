# import urllib.request
# from urllib import response

# response = urllib.request.urlopen('https://www.itcbootcamp.com')
# print(response.getcode())

from ctypes import string_at
import math
print(math.sin(10))


import secrets
print(secrets.choice([212,21211]))

token = secrets.token_hex(16)
print(token)


import string
password = string.digits+string.ascii_letters
generate = ''.join(secrets.choice(password)for i in range(8))
print(generate)#рандомно выбрать пароль для пароля