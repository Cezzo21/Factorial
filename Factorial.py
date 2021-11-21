#factorial(6) = 6 * 5 * 4 * 3 * 2
#factorial(5) = 6 * factorial(5)

def factorial(x):
    if x <= 0:
        return(1)
    elif x == 1:
        return(x)
    else:
        y = x - 1
        return(x*factorial(y))


x = int(input("Give me a number: "))
print(factorial(x))
