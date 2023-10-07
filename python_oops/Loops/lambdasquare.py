# item=[1,2,3,4,5,6,7,8,9]
# square=[]
# #Using loops
# for i in item:
#     square.append(i**2)
# print(square)



#Using Lambda Function
item=[1,2,3,4,5,6,7,8,9]
square=list(map(lambda x:x**2,item))
print(square)