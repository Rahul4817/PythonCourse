class A:
    def __init__(self,n="",m=0):
        self.n=n
        self.m=m

    def display(self):

        print("Hello",self.n)
        print("my address",self.m)


a=A("Hello","567")
a.display()