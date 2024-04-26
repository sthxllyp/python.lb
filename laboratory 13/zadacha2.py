#Вариант 1
str = input("Введите строку: ") 
words = str.upper().split() 
UpWord = [] 
for word in words: 
    NewWord = "-".join(char for char in word) 
    UpWord.append(NewWord) 
res = " ".join(UpWord) 
print(res) 

#Вариант 3
nab_ch = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split())) 
beg, end = map(int, input("Введите два целых числа, начало и конец интервала для суммирования: ").split()) 
sum_ch= sum(nab_ch[beg:end+1]) 
print(f"Сумма чисел от {beg} до {end}: {sum_ch}") 

