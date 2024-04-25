#вариант 2
import math
a = -0.5
b = 1.7
t = 0.44
x = b*math.sin(a*t**2*(math.cos(2*t)))-1
print(x)

#вариант 3
import math
def main():
    a = float(input('\n'"a = "))
    b = float(input("b = "))
    x = float(input("x = "))
    Y = math.sqrt(x**2 + b) - b**2 * (math.sin(x + a)**3)/x
    sys.stdout.write("a=%f, b=%f, t=%f, X=%f" % (a, b, x, Y))
    sys.stdout.flush()
    sys.exit()
if __name__ == "__main__":
    main()

#вариант 5
import math
a = 0.7
b = 0.05
x = 0.5
y = (x**2*(x+1))/(b-math.sin(x+a)**2)
print(y)