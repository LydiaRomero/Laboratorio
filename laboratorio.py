class Medicamento():
    def __init__(self, nombre, sustancia, porcentaje):
        self.nombre = nombre
        self.sustancia= sustancia
        self.porcentaje = porcentaje
    def dimeinformacion(self):
        return self.nombre, self.sustancia,self.porcentaje

paracetamol = Medicamento("parecetamol", "Ácido 1", 0.35)
ibuprofeno = Medicamento("ibuprofeno", "Ácido 2" , 0.40)
aspirina = Medicamento("aspirina", "Ácido 3", 0.30)

lista_nombre = []
lista_nombre.append(paracetamol)
lista_nombre.append(ibuprofeno)
lista_nombre.append(aspirina)


class Laboratorio():
    def __init__(self, laboratorio, med1, med2, med3):
        self.laboratorio = laboratorio
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3
    def informacionlab(self):
        return self.laboratorio, self.med1,self.med2, self.med3
Roche = Laboratorio("Roche",lista_nombre[0], lista_nombre[1], lista_nombre[2])
print("En el laboratorio tenemos los siguientes medicamentos:", Roche.med1.nombre, Roche.med2.nombre, Roche.med3.nombre) 
print( Roche.med1.nombre, "contiende", Roche.med1.porcentaje, "de", Roche.med1.sustancia)        
print( Roche.med2.nombre, "contiende", Roche.med2.porcentaje, "de", Roche.med2.sustancia)         
print( Roche.med3.nombre, "contiende", Roche.med3.porcentaje, "de", Roche.med3.sustancia)

