# def add(**num):
#     for key,value in num.items():
#
#         print(f"{key} is a {value}")
# test = { "Name":"Rahul","age":"21","salary":"600000"}
# add(**test)
# from functools import reduce

# num =[2,3,4,5,6]
# squre = list(map(lambda x :x*x, num))
# print(squre)

# l = [0,2,3,4,5,6]
# a = filter(lambda x:x%2==0,l)
# print(list(a))
# l = [0,2,3,4,5,6]
# a = list(filter(lambda x:x%2==0,l))
# print(a)

# l = [4,5,6,7,8]
# result = reduce(lambda a,b : a*b,l)
# print(result)

# name = ['rahul','chanchal','Naurangi lal']
# marks = [99,77,98]
# roll_no = [122,345,678]
# total = zip(name,marks,roll_no)
# print(list(total))


# list = [1,2,3,4,5]
# def multiply(item):
#     return  item*5
# result = list(map(multiply,list))
# print(result)
# for i in range(10,21):
#     for j in range(1,11):
#         print('{:4}'.format(i*j),end=" ")
#     print()


# def func(a,b):
#     for i in range(a,b):
#         for j in range(a,b):
#             print('{:4}'.format(i*j),end="")
#         print()
# print(func(1,11))

# def even_odd(list):
#     for i in range(len(list)):
#         if i%2==0:
#             print("even number",i)
# list=[1,2,3,4,5,6,7,8,9]
# even_odd(list)
#
# def even_odd(lst):
#     for i in range(len(lst)):
#         if i%2==0:
#             print("even number",i)
#
# lst=[1,2,3,4,5,6,7,8,9]
# e=even_odd(lst)
# print(list(lst))









