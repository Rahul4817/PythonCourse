def factorial(n):
    if n==1:
        return n
    else:
        print(n)
        return n*factorial(n-1)

print(factorial(5))

def fib(n):
    if n in [0,1]:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(7))

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)

print(openRussianDoll(4))