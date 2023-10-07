# import pywhatkit as kit
#
# from PIL import Image
#
#
# handwrite=input("enter text")
#
# kit.text_to_handwriting(handwrite,save_to="img.png")
#
# Image.open("img.png")


import random
import string

def pasword():


    lenght = int(input("Enter the lengh of password"))
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    symbol=string.punctuation
    combine =str(numbers)
    x=random.sample(combine,lenght)
    password="".join(x)
    print(password)

pasword()
