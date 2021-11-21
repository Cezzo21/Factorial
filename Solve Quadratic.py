#ask for your name
#says "hello carol, i can solve ax^2 + bx + c = 0"
#input a, b, c
#get both roots

def root(a,b,c):
    delta = b**2 - (4*a*c)
    x = (-b)/(2*a)
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    if delta == 0:
        return(x)
    elif delta < 0:
        print("No real roots :("), quit()
    else:
        return(x1,x2)

Name = input("Name: ")
print("Hello", Name.capitalize(), "I can solve ax^2 + bx + c = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("x =", root(a,b,c))
