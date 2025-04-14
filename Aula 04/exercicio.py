class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def teste(self):
        return "Olá"
    def calc_area(self):
        return self.b * self.h / 2
    

x = Triangulo()  #executa o metodo init
print(x)
print (x.b, x.h)
x.b = 10
x.h = 20
print (x.teste())
print (x.b, x.h)
print (x.calc_area()) #calc. area de x
#self é usado

y = Triangulo()
print (y)
print (y.b, y.h)
y.b = 15
y.h = 30
print (y.teste())
print (y.b, y.h)
print (y.calc_area()) #calc. area de y

