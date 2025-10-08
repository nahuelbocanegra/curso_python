from datetime import date,datetime


"""Tienes una lista de empleados con sus fechas de ingreso. 
Tu tarea es encontrar al empleado que ha trabajado más tiempo
en la empresa (es decir, el que tiene la fecha de ingreso más antigua"""

empleados = [
    {'nombre': 'Carlos', 'fecha_ingreso': '2015-06-20'},
    {'nombre': 'Ana', 'fecha_ingreso': '2012-01-15'},
    {'nombre': 'Luis', 'fecha_ingreso': '2018-09-30'},
    {'nombre': 'Marta', 'fecha_ingreso': '2010-03-10'}
]
def mayor_antiguedad(empleados):
    today=date.today()
    fechas=[fecha["fecha_ingreso"] for fecha in empleados]    

    #convertir los strings en datetime
    fechas_date = [datetime.strptime(f, '%Y-%m-%d').date() for f in fechas]
    mas_antiguedad=today


    

    for fecha in fechas_date:
        
        if fecha<mas_antiguedad:
                mas_antiguedad=fecha

    emp=[empleado for empleado in empleados if empleado["fecha_ingreso"] == f"{mas_antiguedad}"]

    return emp

print(mayor_antiguedad(empleados))



