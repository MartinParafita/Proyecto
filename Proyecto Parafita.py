
import csv

# Vamos a importar un listado del par Bitcoin/Dólar

def leer_datos():
    with open('BTCUSDT.csv') as datos:
        archivo = list(csv.DictReader(datos))
        print(archivo)
    # Abrimos y leemos todos los datos de la criptomoneda.
    # En la lista, cada fila representa 4 horas en el mes de octubre.
top_high = 0
def precio_max():
    with open('BTCUSDT.csv') as datos:
        top_high = 0
        archivo = list(csv.DictReader(datos))
        cantidad_filas = len(archivo)
        for i in range(cantidad_filas):
            barra = archivo [i]
            max = float(barra.get('High'))
            if top_high < max:
                top_high = max
    print('El precio maximo es: ',top_high)
    return top_high
top_low = 0
def precio_min():
    with open('BTCUSDT.csv') as datos:
        top_low = 0
        archivo = list(csv.DictReader(datos))
        cantidad_filas = len(archivo)
        for i in range(cantidad_filas):
            barra = archivo [i]
            min = float(barra.get('Low'))
            if top_low > min or top_low == 0:
                top_low = min
    print('El precio minimo es: ',top_low)
    return top_low
media = 0
def precio_medio():
    with open('BTCUSDT.csv') as datos:
        archivo = list(csv.DictReader(datos))
        cantidad_filas = len(archivo)
        sumatoria = 0
        for i in range(cantidad_filas):
            barra = archivo [i]
            cierre = float(barra.get('Close'))
            sumatoria += cierre
    media = sumatoria / cantidad_filas
    print('El precio medio es: ',round(media, 2))
    return media

def tendencia():
    with open('BTCUSDT.csv') as datos:
        archivo = list(csv.DictReader(datos))
        cantidad_filas = len(archivo)
        inicio_ciclo = archivo[0].get('Open')
        fin_ciclo = archivo[cantidad_filas-1].get('Close')
        print('Precio inicial: ',inicio_ciclo)
        print('Precio final: ',fin_ciclo)
        if fin_ciclo < inicio_ciclo:
            print('La tendencia es bajista. Porque el precio inicial es mayor al de cierre.')
        else:
            print('La tendencia es alcista. Porque el precio final es mayor al precio inicial.')
        

if __name__ == '__main__':

    leer_datos()
    precio_max()
    precio_min()
    precio_medio()
    tendencia()
    
    