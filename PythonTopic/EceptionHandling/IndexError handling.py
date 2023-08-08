fruits=['Apple','banana','orange']
def make_pie(index):
    try:
        fruit=fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruits+"pie")

make_pie(4)