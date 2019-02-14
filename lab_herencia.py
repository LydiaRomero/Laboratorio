class Producto():
    def __init__(self, nombre):
        self.nombre = nombre
    def dimeinformacion(self):
        return self.nombre
        
class Medicamento(Producto):
    def __init__(self, nombre, componente, porcentaje):
        self.nombre = nombre
        self.componente= componente
        self.porcentaje = porcentaje
    def dimeinformacion(self):
        return self.componente,self.porcentaje

paracetamol = Medicamento("parecetamol", "Ácido 1", 0.35)
ibuprofeno = Medicamento("ibuprofeno", "Ácido 2" , 0.40)
aspirina = Medicamento("aspirina", "Ácido 3", 0.30)
vaselina = Producto("vaselina")
vitamina = Producto("vitamina")
lista_nombre = []
lista_nombre.append(paracetamol)
lista_nombre.append(ibuprofeno)
lista_nombre.append(aspirina)
lista_nombre.append(vaselina)
lista_nombre.append(vitamina)


class Laboratorio():
    def __init__(self, laboratorio, med1, med2, med3, prod1, prod2):
        self.laboratorio = laboratorio
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3
        self.prod1 = prod1
        self.prod2 = prod2
    def informacionlab(self):
        return self.laboratorio, self.med1,self.med2, self.med3, self.prod1, self.prod2
Roche = Laboratorio("Roche",lista_nombre[0], lista_nombre[1], lista_nombre[2], lista_nombre[3], lista_nombre[4])
print("En el laboratorio tenemos los siguientes medicamentos:", Roche.med1.nombre, Roche.med2.nombre, Roche.med3.nombre)
print("Además, en el laboratorio tenemos los siguientes productos:", Roche.prod1.nombre, Roche.prod2.nombre)
print( Roche.med1.nombre, "contiende", Roche.med1.porcentaje, "de", Roche.med1.componente)        
print( Roche.med2.nombre, "contiende", Roche.med2.porcentaje, "de", Roche.med2.componente)         
print( Roche.med3.nombre, "contiende", Roche.med3.porcentaje, "de", Roche.med3.componente)

