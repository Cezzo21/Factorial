def hailstorm(x):
    if x == 1:
        return("Finished on 1")
    if x%2 == 0:
        print(x/2)
        return(hailstorm(x/2))
    else:
        print(3*x+1)
        return(hailstorm(x*3 + 1))

x = int(input("number: "))
print(hailstorm(x))


