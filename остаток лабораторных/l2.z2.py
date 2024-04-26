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