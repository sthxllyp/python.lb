#Вариант 2
n = 15
sum = 0
proizv = 1 
for i in range(1, n+1):
    num = float(input("Введите число i:"))
    sum += num
    proizv *= num 
    print("сумма введённых чисел", sum)
    print("произведение введённых чисел", proizv)
#Вариант 6
k = 3
sum = 0
for i in range(1000, 9999):
    if i%k == 0: 
        sum += i
    print("сумму 4-значных чисел, кратных k: " , sum)
