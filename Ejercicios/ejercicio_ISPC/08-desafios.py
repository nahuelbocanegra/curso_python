#  8- Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
#  en el campusVitacura.
#  Una máquinadealimentos tiene productos de tres tipos, A, B y C, que valen
#  respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
#  $50 y$100.
#  Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
#  monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
#  del producto, el programa debe entregar las monedas de vuelto, una por una.4

def maquina_alimentos():

    dicc_productos={"A" : 270,"B" : 340 ,"C" : 390 }

    total=ingresar_monedas()

    precio=seleccion_productos(dicc_productos)

    if total < precio:
        return " no le alcanza para la compra " 
    
    vuelto=total-precio

    print(f"su vuelto es de : {vuelto}")

    for valor in [100,50,10]:
        while vuelto >= valor:
            vuelto -= valor
            print(valor)
        
    
def ingresar_monedas():
        
        total=0
        while True:
            try:
                monedas=int(input("ingrese las monedas (100,50,10) ponga 0 para terminar de agregar: "))
                if monedas == 0:
                    break
                elif monedas in [10,50,100]:
                    total+=monedas
                else:
                    print("moneda no valida, solo monedas de (10,50,100)")
            except:
                print("entrada invalidad, ingrese una moneda por favor")

        return total

def seleccion_productos(dicc_productos):
    print("¿Que producto desea?")
    for producto,precio in dicc_productos.items():
        print(f"{producto}:{precio}")

    while True:
        producto=input("Seleccione un producto(A,B,C): ").strip().upper()
        if dicc_productos[producto]:
            break
        else:
            print("ERROR, elije una de las 3 opciones")
        
    
    return  dicc_productos[producto]


maquina_alimentos()