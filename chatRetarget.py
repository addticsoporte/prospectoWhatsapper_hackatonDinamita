import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pywhatkit
import pymysql
from datetime import datetime
from decouple import config
MYSQL_PASSWORD = config('MYSQLPASS')

#Conexion a la base de datos.
connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = MYSQL_PASSWORD,
    db = "retargettingmysql"
)
cursor = connection.cursor()
hoy = datetime.today().strftime('%Y-%m-%d') #Obtener fecha actual

asunto = input("Ingrese asunto, esto es para guardarlo en la tabla Campania: ")
mensaje = "DILE ADIOS A LOS CARGOS NO RECONOCIDOS!! Felicidades su tarjeta de crédito Aqua ha sido aprobada, evita cargos no reconocidos, apagando tu tarjeta SIN COSTO y cada compra cuenta con un CVV único e irrepetible desde la App. Ingresa a https://hackaton-dinamita.gitlab.io/portal-contratacion/ para tener lista tu tarjeta!"




data = pd.read_csv("ProspectosSinTarjeta-20-10-2022 19-42-35.csv")
data_dict = data.to_dict('list')
telefonos =  data_dict['telefono']
first = True
for telefono in telefonos:


  time.sleep(4)
  web.open("https://web.whatsapp.com/send?phone=52_"+str(telefono)+"&text="+str(mensaje))
  if first:
    time.sleep(4)
    first = False
  width,height = pg.size()
  pg.click(width/2,height/2)
  time.sleep(5)
  pg.press('enter')
  time.sleep(3)
  pg.hotkey('ctrl','w')

  #Registrar las campanias en una tabla de una base de datos. 
  sql = "INSERT INTO campania(fecha,tipoCanal,asunto,email,telefono,costo) VALUES('{}','whatsapp','{}','{}',' ',{})".format(hoy,str(asunto),telefono,0)
  cursor.execute(sql)
  connection.commit()

print('============================================')
print('= Programa ejecutado y finalizado correctamente =')
print('============================================')
