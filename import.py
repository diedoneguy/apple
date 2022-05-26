import os
# os in notebook
print(os.name)

# name notebook
print(os.getlogin())

print(os.getcwd())

#из кого файла идет запуск
import sys
print(sys.argv)


print(sys.executable)

print(sys.platform)

print(sys.version)

print(sys.copyright)

# import csv
# with open('studios.csv','w')as files:
#     write = csv.writer(files)
#     write.writerow('id','name','duration')
#     write.writerow([1,'Aktan','python'])
#     write.writerow([2,'Ravil','python'])

from datetime import date, datetime
# print(datetime.now())

# birth = input('your birth')
# today = date.today
# print(int(today.year) - int(birth[0:4]))

# import time

# for i in range(10):
#     print(i)
#     time.sleep(2)#считать с задержкой 
#     print(i)


# now = datetime.now()
# t = now.strftime('%d:%Y:%S')#получить время
# print(t)

import random
a=['aktan','ravil','ilim']
print(random.choice(a))
random.shuffle(a)####поменяет местами список
print(a)
print(random.randint(1,10))
