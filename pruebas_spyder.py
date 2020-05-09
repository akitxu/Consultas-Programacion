# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import os
import pandas as pd
import pandas_datareader as pdr
import numpy as np
import datetime as dt
from datetime import datetime, date, time, timedelta
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import xlrd
from matplotlib import style
style.use('ggplot')
 
# Seleccionar fechas para el rango de análisis
def selecciona_fechas():
    #start = "2000-1-4"
    start = input("\nIntroduzca la fecha de inicio (YYYY-M-D: \n")
    opcion = input("\nEs la fecha final el día de hoy s/n:\n")
    if opcion == "s":
        end = dt. datetime.now()
        #end = date.today()
    else:
        end = input("\nIntroduzca la fecha de finalización (YYYY-M-D: \n")
    return start, end
start, end = selecciona_fechas() 

# Change directory 
#os.chdir("E:/Mi_Proyecto/Py_Proyecto_2020/Py_Paso_Peregrino/Ficheros/lista_valores_1.csv") 
os.chdir("/media/enri/Mi_Proyecto/Py_Proyecto_2020/Py_Paso_Peregrino/Ficheros/") 

# Importar el archivo "lista_valores.csv"
lista_valores = pd.read_csv("lista_valores_1.csv")
# Listas para acciones, Fodos de Inversión y Planes de Pensión. Ficheros .xlsx
lista_nombres = lista_valores["nombres"] 
lista_ficheros  = lista_valores["ficheros_xlsx"]  
dicc = dict(zip(lista_nombres ,lista_ficheros))
lista_nombres

# Seleccionar un valor y un indicador de referencia.
def selec_val_ind (lista_nombres):
    for counter, value in enumerate(lista_nombres):
        print(counter, value)      
    print ("\t20 - Salir")
    # solicitamos una opción de valor al usuario
    opcion_val = int (input("\nSeleccione un valor  \n") )
    nom_val = lista_nombres[opcion_val]
    file_valor = lista_ficheros[opcion_val]
    #file = dicc[nom_val]

    # solicitamos una opción de indice al usuario
    opcion_ind = int (input("\nSeleccione un indicador  \n") )
    nom_ind = lista_nombres[opcion_ind]
    file_ind = lista_ficheros[opcion_ind]
    
    if opcion_val == 17:
        raise SystemExit
    if opcion_val > 17 :
        input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar\n") 
    return nom_val, nom_ind, file_valor, file_ind

def test_run():    

    nom_val, nom_ind, file_valor, file_ind = selec_val_ind (lista_nombres)    
    return nom_val, nom_ind, file_valor, file_ind

if __name__ == "__main__":    
    nom_val, nom_ind, file_valor, file_ind = test_run()
    
    
def importa_cotizaciones(file ):
    # Importar de un archivo Excel y llamarlo xls
    xls = pd.ExcelFile(file) # pd.ExcelFile object
    cotizaciones = pd.read_excel(xls, sheet_name= "Sheet1", na_values='n/a' ) 
    # Convertir las fechas de la columna "Date" al tipo Datetime
    cotizaciones['Date'] = pd.to_datetime(cotizaciones['Date'], errors='coerce')
    cotizaciones = cotizaciones.set_index("Date")
    cotizaciones = cotizaciones.dropna()
    #cotizaciones.rename(columns={"Close":lista_nombres}, inplace=True )    
    
    return cotizaciones
os.chdir("/media/enri/Mi_Proyecto/Py_Proyecto_2020/Py_Paso_Peregrino/Ficheros_xlsx") 
#os.chdir("E:/Py_Proyecto_2020/Py_Paso_Peregrino/Ficheros_xlsx")
print ("Valor seleccionado :", nom_val)    
cotiz_valor = importa_cotizaciones(file_valor )
print (cotiz_valor.tail())    
print ("Indicador seleccionado :", nom_ind) 
cotiz_indicador = importa_cotizaciones(file_ind )
print (cotiz_indicador.head())


# graficando Adj Close
plot = cotiz_valor["2016-7":"2019-7"].plot(figsize=(10, 8))    
    
    

