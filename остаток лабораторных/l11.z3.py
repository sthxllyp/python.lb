import random
b = [random.uniform(1,30) for x in range(15)]
print("Исходный список: ",b)
max_index = b.index(max(b))
b[-1], b[max_index] = b[max_index], b[-1]
print("Измененный список: ",b)