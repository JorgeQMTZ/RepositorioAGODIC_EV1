class Tarjeta:
    def __init__(self, id, cantidad =0):
        self.id = id
        self.saldo = cantidad
        return
    def mostrar_saldo(self):
        print('El saldo es', self.saldo, '$.')
        return
    
class Tarjeta_descuento(Tarjeta):
    def __init__(self, id, descuento, cantidad = 0):
        self.id = id
        self.descuento = descuento
        self.saldo=cantidad
        return
    def mostrar_descuento(self):
        print('Descuento de', self.descuento,'% en los pagos.')
        return

t = Tarjeta_descuento('0123456789', 2, 1000)
t.mostrar_saldo()

t.mostrar_descuento()