from pywebcopy.configs import get_config
from cantidad_pag import extraer_num_pag_del_hilo
import os
import time
import logueador
import requests


"""Crea la carpeta de guardado de hilos en caso de no existir"""

folder = os.listdir()
if not "hilo" in folder:
    os.mkdir("hilo")

"""URL de la web"""

url_fc = "https://forocoches.com/foro/showthread.php?t="

thread_number = input("Introduzca número de hilo: ")

"""Inicio de sesion web"""

credentials = open("credenciales.txt","r")
credentials = credentials.readline()
credentials = credentials.split("PASWORD:")
pasword = credentials[1]
username = credentials[0]
username = username.split("USERNAME:")
username = username[1]

session = logueador.loguear_en_FC(username,pasword)

"""Extrae el título del hilo así como la cantidad de páginas en el"""

title_and_num_of_pag_hilo = extraer_num_pag_del_hilo(url_fc,thread_number,session)

titulo = title_and_num_of_pag_hilo[0]
page_amount = int(title_and_num_of_pag_hilo[1])

"""Si el titulo revela que no hay una cuenta iniciada avisa por consola y detiene el programa"""

if titulo == "Forocoches ":
    print("El hilo al que intenta acceder necesita una cuenta activa y/o tu cuenta no permite el acceso al hilo")

else:
    
    """Descarga el hilo"""

    print("Descargando hilo: " + titulo)


    old_page_amount = 1

    while 1:

        """Extrae la cantidad de páginas que contiene el hilo"""

        title_and_num_of_pag_hilo = extraer_num_pag_del_hilo(url_fc,thread_number,session)

        new_page_amount = int(title_and_num_of_pag_hilo[1])

        """Va descargando paginas mientras las páginas paginas descargadas sean inferiores al monto total"""

        if new_page_amount > old_page_amount:

            print("Descargando página: " + str(old_page_amount) + "/" + str(new_page_amount))

            url = url_fc + str(thread_number) + "&page=" + str(old_page_amount)

            conf = get_config(url,"hilo/"  + str(thread_number) )
            webpage = conf.create_page()
            webpage.session = session
            webpage.get(url)
            webpage.retrieve()
            webpage.save_complete()

            old_page_amount = old_page_amount +1

            """Cuando la cantidad de paginas descargadas es la misma que la cantidad de paginas a descargar solo descarga la ultima pagina a fin de tenerla siempre actualizada """

        else:

            print("Actualizando página: " + str(old_page_amount) + "/" + str(new_page_amount))

            url = url_fc + str(thread_number) + "&page=" + str(new_page_amount)

            conf = get_config(url,"hilo/"  + str(thread_number) )
            webpage = conf.create_page()
            webpage.session = session
            webpage.get(url)
            webpage.retrieve()
            webpage.save_complete()

        time.sleep(1)
        

    

