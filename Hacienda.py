import streamlit as st

st.markdown("Version 2. Bringing data from API")

import requests

import pandas as pd
import numpy as np
df=pd.read_html('https://www.monasterio-tattersall.com/precios-hacienda') #leo la tabla de la página
df[0] 
hacienda = df[0] #asigno una variable a la tabla
categoria = hacienda.Categoría #creo las series
promedio = hacienda.Promedio
tabla = pd.DataFrame({'categoria':categoria,'promedio':promedio}) #creo un dataframe con categoria y promedio
ternero=tabla[0:4] 
novillito=tabla[4:7]
ternera=tabla[7:11]
vaquillona=tabla[11:14]
vaca=tabla[19:20]
fecha=(tabla[25:26].values)[0][0]
ternero160=int(ternero.promedio[0][2:5])
ternero180=int(ternero.promedio[1][2:5])
ternero200=int(ternero.promedio[2][2:5])
ternero230=int(ternero.promedio[3][2:5])
novillo260=int(novillito.promedio[4][2:5])
novillo300=int(novillito.promedio[5][2:5])
novillo301=int(novillito.promedio[6][2:5])
ternera150=int(ternera.promedio[7][2:5])
ternera170=int(ternera.promedio[8][2:5])
ternera190=int(ternera.promedio[9][2:5])
ternera210=int(ternera.promedio[10][2:5])
vaquillona250=int(vaquillona.promedio[11][2:5])
vaquillona290=int(vaquillona.promedio[12][2:5])
vaquillona291=int(vaquillona.promedio[13][2:5])
vacas=int(vaca.promedio[19][2:8])
def constructor():
    tipo=input('ingrese tipo de hacienda: \n1 - Ternero\n2 - Novillito\n3 - Ternera\n4 - Vaquillona\n5 - Vaca\n')
    if tipo =='1':
        categoria='Ternero'
    elif tipo == '2':
        categoria='Novillito'
    elif tipo == '3':
        categoria='Ternera'
    elif tipo == '4':
        categoria='Vaquillona'
    elif tipo == '5':
        categoria='Vaca'
    cantidad=int(input('ingrese cantidad: '))
    peso=int(input('ingrese peso: '))
    def valores():
        if tipo == '1' and peso < 160:
            valor = ternero160*cantidad*peso
        elif tipo == '1' and peso < 180:
            valor = ternero180*cantidad*peso
        elif tipo == '1' and peso <= 200:
            valor = ternero200*cantidad*peso
        elif tipo == '1' and peso > 200:
            valor = ternero230*cantidad*peso
        elif tipo == '1' and peso == 0:
            valor = ternero200*cantidad*peso
        elif tipo == '2' or 'novillo' and peso < 260:
            valor = novillo260*cantidad*peso
        elif tipo == '2' or 'novillo'and peso <= 300:
            valor = novillo300*cantidad*peso
        elif tipo == '2' or 'novillo'and peso > 300:
            valor = novillo301*cantidad*peso
        elif tipo == '2' or 'novillo'and peso == 0:
            valor = novillo300*cantidad*peso
        elif tipo == '3' and peso < 150:
            valor = ternera150*cantidad*peso
        elif tipo == '3' and peso < 170:
            valor = ternera170*cantidad*peso
        elif tipo == '3' and peso <= 190:
            valor = ternera190*cantidad*peso
        elif tipo == '3' and peso > 190:
            valor = ternera210*cantidad*peso
        elif tipo == '3' and peso == 0:
            valor = ternera190*cantidad*peso
        elif tipo == '4' and peso < 250:
            valor = vaquillona250*cantidad*peso
        elif tipo == '4' and peso <= 290:
            valor = vaquillona290*cantidad*peso
        elif tipo == '4' and peso > 290:
            valor = vaquillona291*cantidad*peso
        elif tipo == '4' and peso == 0:
            valor = vaquillona290*cantidad*peso
        elif tipo == '5':
            valor = vacas*cantidad
        return valor
    valor=valores()
    d = [categoria, cantidad, peso, valor]
    return d
metalista=[]
def programa():
    while True:
        metalista.append(constructor())
        repite=input('¿Hay otra categoría más para cargar?: ')
        if repite in ['si','SI']:
            continue
        else:
            break
    from tabulate import tabulate
    return print(f'\n\n{tabulate(metalista, headers=["Categoría", "Cantidad", "Peso", "Valuación"])}\n\nLos precios considerados son de la {fecha}')
programa()
