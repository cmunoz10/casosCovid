# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:11:52 2021

@author: camun
"""

import numpy as np
import pandas as pd


url="Casos_positivos_de_COVID-19_en_Colombia.csv"
datos=pd.read_csv(url)
datos.count()

# 1 total de contagiados = numero total de filas (casos registrados)

print('El numero total de casos es :',datos.shape[0])

# 2 numero de municipios afectados

datos['Nombre municipio'].value_counts().size


# 3 numero de municipios afectados


"""  Numero de municipios sin repeticion:
    para ello usamos el primer comando que nos pasara todos los datos a mayusculas
    permitiendo de esta manera lograr "homogeneisar" los datos y evitar 
    repeticiones:
    
    """

datos['Nombre municipio']= datos['Nombre municipio'].str.upper()

""" luego de eso ejecutamos el contador de datos """

datos['Nombre municipio'].value_counts().size

# 4 numeros de personas que se encuentran en casa 

""" usaremos un procedimiento parecido al anterior para igualar 
las palabras repetidas ( se usara en los diferentes casos un metodo parecido)""" 

datos['Ubicación del caso']= datos['Ubicación del caso'].str.upper()

""" luego de eso ejecutamos el contador de datos  verificando que los datos
esten todos en mayuscula primero :"""
datos['Ubicación del caso'].value_counts()

print('numero de personas que se encuentran en casa  es :' ,datos['Ubicación del caso'].str.contains('CASA').value_counts()[True])


# 5 numero de personas que se encuentran recuperados
datos['Recuperado']= datos['Recuperado'].str.upper()

print('numero de personas que se encuentran recuperados  es :' ,datos['Recuperado'].str.contains('RECUPERADO').value_counts()[True])


# 6 numero de personas que han fallecido 

datos['Recuperado']= datos['Recuperado'].str.upper()


print('El numero de fallecidos es  :',datos['Recuperado'].str.contains('FALLECIDO').value_counts()[True])


#7 ordernar de mayor a menor por tipo de caso :
    
datos['Tipo de contagio'].value_counts(ascending=False) 
"""aunque por defecto el value_counts nos lo muestra de mayor a menor"""



#8 numero de departamentos




datos['Nombre departamento'].value_counts().sort_index(ascending=True)

print('El total de departamentos es  :',datos['Nombre departamento'].value_counts().size)
      

# 9 numero de departamentos sin repeticiones 


datos['Nombre departamento'] = datos['Nombre departamento'].str.upper()
print('El total de departamentos (sin repetidos) es  :',datos['Nombre departamento'].value_counts().size)

#10 ordene de mayor a menor por tipo de atencion

datos['Ubicación del caso'].value_counts().sort_index(ascending=True)

#11 . Liste de mayor a menor los 10 departamentos con mas casos de contagiados

departamentos = datos['Nombre departamento'].value_counts().keys().tolist()

print('los 10 departamentos con mas contagios son : ' , departamentos[0:9])

#12 liste de mayor a menor los 10 municipios con mas casos de contagiados

datos['Nombre municipio'] = datos['Nombre municipio'].str.upper()
municipios = datos['Nombre municipio'].value_counts().keys().tolist()
print('los 10 municipios con mas contagios son : ' , municipios[0:9]) 

#13 liste de mayor a menor el numero de contagiados por pais de procedencia 

datos['Nombre del país'] = datos['Nombre del país'].str.upper()
print('Los paises de procedencia son : ' , datos['Nombre del país'].value_counts()) 

#14 liste de mayor a menor las fechas donde se presentaron mas contagios
print('las fechas con mas contagios fueron:' , datos['fecha reporte web'].value_counts())

#15 Grafique las curvas de contagio muerte y recuperacion de colombia 


datos['fecha reporte web'].value_counts(ascending=True).plot()


#16 haga un grafico de barras por sexo de toda colombia

datos['Sexo'].str.upper().value_counts().plot(kind='bar')

#17 haga un grafico de barras por tipo de contagio en colombia

datos['Tipo de contagio'].str.upper().value_counts().plot(kind='bar')










