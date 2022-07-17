class Menu:
    def __init__(self,x='',y=''):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x + other.x ,self.y + other.y
        
a= Menu("idly ", 'vada ')
b= Menu("10", '20')
c=a+b
for i in c:
    print(i)
