from random import randint
n = randint(100,999)
print("Получено число" ,n,)
print('Его цифры {},{},{}'.format(n//100,n//10%10,n%10))