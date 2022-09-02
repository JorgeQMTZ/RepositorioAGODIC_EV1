class Circulo:
    pi=3.14159
    def __init__(self, radio):
        self.radio=radio
    def area(self):
        return Circulo.pi * self.radio**2
    
c1=Circulo(2)
c2=Circulo(3)
print(c1.area())

print(c2.area())

print(c1.pi)

print(c2.pi)