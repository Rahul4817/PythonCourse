x=lambda a,b,c:a+b*c
print(x(3,5,9))

def my_function(n):
    return lambda a:a*n
myDoubler=my_function(2)
print(myDoubler(11))