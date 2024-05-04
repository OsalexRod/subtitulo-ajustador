from datetime import datetime, timedelta
from Bloque import Bloque
import sys
import re

# Expresión regular
patron_con_caracter_raro = r"^\uFEFF[0-9]+$"
patron_solo_numeros = r"^[0-9]+$"

# Nombre del archivo .srt
nombre_archivo = "Kimi no na wa_2016_eric paroissien_JAPANESE_SUBS.srt"

# Abrir el archivo en modo lectura
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# variables importantes
contenido = []
lista_de_bloques = []
empieza = False
contador = 1

for linea in lineas:
    lineActual = linea.strip()
    print(f"Linea:     {lineActual}  ,  cantidad {len(lineActual)}")

    if re.match(patron_con_caracter_raro, lineActual) or re.match(patron_solo_numeros, lineActual):
        empieza = True
        if lineActual != chr(65279)+chr(49) and int(lineActual) != contador:
            sys.exit(1)
        contador+=1
        continue
    if empieza:
        contenido.append(lineActual)
    if lineActual == "" and contenido:
        empieza = False
        print(contenido)
        #sys.exit(0)
        rangos_de_tiempo = contenido[0]
        contenido.pop(0)
        parrafo_traducido = "\n".join(contenido)
        nuevoBloque = Bloque(rangos_de_tiempo[0:12], rangos_de_tiempo[17:29], parrafo_traducido)
        contenido = [] #limpiamos
        lista_de_bloques.append(nuevoBloque)
        print("Nuevo bloque guardado")

print("Listo !!!")
print(lista_de_bloques[1193])

# otras variables
tiempo_a_quitar = 13 #segundos
formato = "%H:%M:%S,%f"

for bloqueActual in lista_de_bloques:
    inicio = bloqueActual.inicio
    fin = bloqueActual.fin

    objeto_inicio = datetime.strptime(inicio, formato)
    objeto_fin = datetime.strptime(fin, formato)

    tiempo_modificado_inicio = objeto_inicio - timedelta(seconds=tiempo_a_quitar)
    tiempo_modificado_fin = objeto_fin - timedelta(seconds=tiempo_a_quitar)
    bloqueActual

    bloqueActual.inicio = str(tiempo_modificado_inicio.strftime(formato)[0:12])
    bloqueActual.fin = str(tiempo_modificado_fin.strftime(formato)[0:12])

print(lista_de_bloques[1193])

archivo_salida= "salida.srt"

# Guardar los cambios en el archivo
with open(archivo_salida, "w", encoding="utf-8") as archivo:
    contador_bloque = 1
    for bloqueActual in lista_de_bloques:
        archivo.write(str(contador_bloque)+"\n")
        archivo.write(f"{bloqueActual.inicio} --> {bloqueActual.fin}\n")
        archivo.write(bloqueActual.parrafo)
        archivo.write("\n")
        contador_bloque += 1

print("\n¡Subtítulos modificados y guardados con éxito!")
