#This Lambda function returns the two number multiplication

# x=lambda a,b:a*b
#
# print(x(4,8))

#
# student=["rahul","rajesh", "sapna","naurangi","rachana"]
# for student in student:
#     if student == "sapna":# To avoid the a complete String  prticuler index
#         continue;
#     print(student)

# To call Global and Local Variable
#
# a =12
# def show():
#     x = 23
#     print("this is the local var",x)
#     print("This is theglobal var",a)
#     print(a*x)
#
# def my_function():
#     x=5
#     print(a+x)
#
# show()
# my_function()

#remove any number into a large integer to print

# i=0
# while i < 13:
#     i = i + 1 #if don't print to 1 then do that
#     print(i)
    #i=i+1 #if don't print to 1 then do tha


 #to seprate the string
# a="Rahul kumar"
# s=[]
# for i in a:
#     #i=i.split(a) #Ye String character ko one by one alg karta ha
#     s.append(i)#Ye String character ko ek baar me hi  alg kar deta hai
#     #print(i)
#     print(s)

# a=4
# b=5
# def add():
#     return a+b
# def sub():
#     return a-b
# def mul():
#     return a*b
# def div():
#     return a//b
# print(add(),sub(),mul(),div())




a=int(input("enter the first number:"))
b=int(input("enter the second number"))
def add():
    return a+b

def sub():
    return a-b

def mul():
    return a*b

def div():
    return a//b

print(add(),sub(),mul(),div())