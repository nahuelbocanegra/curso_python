#trabajando con fechas y horas en pyhon
import locale
from datetime import datetime,timedelta,timezone

locale.setlocale(locale.LC_TIME,"es_ES.UTF-8") #CAMBIAR DE INGLES A ESPAÑOL



print(datetime.now()) #fecha actual y hora actual 
now=datetime.now()

#2 crar fecha y hora especifica
hora_especifica=datetime(2025,1,12)
print(hora_especifica)

#formatar fechas

#pasarle el objeto datetime u el formato especificado (formato en documentacion)
#formato : 
format_date=now.strftime("%A/%B/%y  %H:%M:%S")

print(format_date)


#OPERACIONES  CON FECHAS

ayer=datetime.now() - timedelta(days=1,hours=3) #restar dias 

mañana=datetime.now() + timedelta(days=1)


#obtener los componentes individuales 
year= now.year
print(year)

#calcular la diferencia entre dos fechas

date1=datetime.now()
date2=datetime(2025,2,12)

diferencia=date1-date2
print(diferencia)


