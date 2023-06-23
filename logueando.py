import requests
import cantidad_pag



def logearse(nombre_usuario,contrasenya):

    payload = {
        "do":"login",     
        "vb_login_username":nombre_usuario,
        "vb_login_password":contrasenya,
    }

    sesion = requests.Session()
    sesion.post('https://forocoches.com/login' , data=payload)

    return sesion


