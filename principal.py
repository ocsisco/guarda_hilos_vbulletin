from pywebcopy import save_website
from cantidad_pag import extraer_num_pag_del_hilo
import os
import time
import logueando


"""Crea la carpeta de guardado de hilos en caso de no existir"""

carpetas = os.listdir()
if not "hilo" in carpetas:
    os.mkdir("hilo")

"""URL de la web"""

url_fc = "https://forocoches.com/foro/showthread.php?t="


numero_de_hilo = input("Introduzca número de hilo: ")
numero_de_pagina = 0

"""Inicio de sesion web"""

sesion = logueando.logearse("usuario","contraseña")

"""Extrae el título del hilo así como la cantidad de páginas en el"""

title_and_num_of_pag_hilo = extraer_num_pag_del_hilo(url_fc,numero_de_hilo,sesion)

titulo = title_and_num_of_pag_hilo[0]
cantidad_paginas = int(title_and_num_of_pag_hilo[1])

"""Descarga el hilo"""

print("Descargando hilo: " + titulo)

for numero_de_pagina in range(cantidad_paginas):

    print("Descargando la página: " + str(numero_de_pagina +1) + "/" + str(cantidad_paginas))

    url = url_fc + str(numero_de_hilo) + "&page=" + str(numero_de_pagina +1)

    save_website(url,project_folder="hilo/" + str(numero_de_hilo))
               
print("Hilo descargado con exito ")
print("")


"""Activar vigilia para que el hilo descargado este constantemente actualizado"""

vigilia = input("¿Desea que la aplicación entre en modo vigilia y actualice el hilo? Si o No?")


if vigilia == "SI" or "si" or "Si" or "sI":
    vigilia = True
else:
    vigilia = False


actualizacion_cantidad_paginas_anterior = cantidad_paginas

while vigilia:

    title_and_num_of_pag_hilo = extraer_num_pag_del_hilo(url_fc,numero_de_hilo,sesion)

    actualizacion_cantidad_paginas = int(title_and_num_of_pag_hilo[1])

    if actualizacion_cantidad_paginas > actualizacion_cantidad_paginas_anterior:

        print("Actualizando hilo: " + str(actualizacion_cantidad_paginas) + "/" + str(actualizacion_cantidad_paginas))

        url = url_fc + str(numero_de_hilo) + "&page=" + str(actualizacion_cantidad_paginas_anterior)
        save_website(url,project_folder="hilo/" + str(numero_de_hilo))

        url = url_fc + str(numero_de_hilo) + "&page=" + str(actualizacion_cantidad_paginas)
        save_website(url,project_folder="hilo/" + str(numero_de_hilo))

        actualizacion_cantidad_paginas_anterior = actualizacion_cantidad_paginas

    else:

        print("Actualizando hilo: " + str(actualizacion_cantidad_paginas) + "/" + str(actualizacion_cantidad_paginas))

        url = url_fc + str(numero_de_hilo) + "&page=" + str(actualizacion_cantidad_paginas)
        save_website(url,project_folder="hilo/" + str(numero_de_hilo))



    time.sleep(10)

