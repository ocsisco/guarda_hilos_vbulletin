from bs4 import BeautifulSoup
import requests




def extraer_num_pag_del_hilo(url_fc,numero_de_hilo,sesion):

    url = url_fc + str(numero_de_hilo) + "&page=0"

    r = sesion.get(url)
    
    if r.status_code == 200:

        


        soup = BeautifulSoup(r.text, 'lxml')

        titulo_del_hilo = str(soup.title)
        titulo_del_hilo = titulo_del_hilo.replace("<title>","")
        titulo_del_hilo = titulo_del_hilo.split("-")
        titulo_del_hilo = titulo_del_hilo[0]


        enlaces = soup.find_all('a')

        url_bruta = ""
        numero_de_paginas_del_hilo = 0

        for enlace in enlaces:
            if ("showthread.php?t=" + str(numero_de_hilo) + "&amp;page=") and ("Mostrar Resultados") in str(enlace):
                    url_bruta = str(enlace)
                    

        if "page" in url_bruta:
            url_bruta = url_bruta.replace('<a href="showthread.php?t=' + str(numero_de_hilo) + "&amp;page=","")
            url_bruta = url_bruta.replace('"',"")
            url_bruta.split(" ")
            url_bruta = url_bruta[0]
            numero_de_paginas_del_hilo = int(url_bruta)

        if numero_de_paginas_del_hilo == 0:
            numero_de_paginas_del_hilo = 1




    return titulo_del_hilo,numero_de_paginas_del_hilo


