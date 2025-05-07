#POO

class Coche:

    #propiedades
    largo_chasis=250
    ancho_chasis=120
    ruedas=4
    enmarcha=False

    #comportamiento(metodos)

    def arrancar(self): #self => hace referencia al propio abjeto de la clase
        self.enmarcha= True

    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        
        return "el coche esta apagado"

# instanciar clase

coche1=Coche()


print(f"el coche tiene {coche1.ruedas} ruedas")

#metodo
coche1.arrancar()

print(coche1.estado())