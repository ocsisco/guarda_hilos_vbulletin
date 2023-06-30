import requests
import time


def loguear_en_FC(username,pasword):

    print("Logueando cuneta...  " + str(username) + "  " + str(pasword))

    payload = {
            'do': 'login',
            'forceredirect': '1',
            'url': '/',
            'vb_login_md5password':'' ,
            'vb_login_md5password_utf':'',
            's':'',
            'securitytoken': 'guest',
            'vb_login_username': username,
            'vb_login_password': pasword,
            'cookieuser': '1',
            'logb2': 'Iniciar sesión',
        }

    """sesion.headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #"Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"es-ES,es;q=0.9",
            #"Cache-Control":"max-age=0",
            #"Content-Length":"195",
            #"Content-Type":"application/x-www-form-urlencoded",
            #"Cookie":"_fbp=fb.1.1687172361317.924207212; euconsent-v2=CPtnAkAPtnAkABcAIBESDJCgAP_AAH_AAAiQIzER_C9MQWNjUX58Afs0aYxHxgACoGQABACJgygBCBPA8IQEwGAYIAVAAogKAAAAoiJBAAAhCAlAAAEAQAAAACCMAEAAAAAAIKAAgAARAgEACAhBEQAAEAIAAABBABAAgAAEQBoAQAAAAAAAAAAAAAAgAACBAAQAAAAAAQAAAAAAAAgAAAAAAAAAAAAAAFBGYAEwVJiABsSgwJgAwihRACCMAAAAQAAAAQMEAAAQIAHBCACgwCAAAAABEBAAAAFERAIAAAIAEIAAAACAAAAAABAAAAAAAAAAQAAAAAIAAAAAEAACAAAAAAAAAIAAAAEAAAAAIACAAAAAAEAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.x9tEJO4.4U6gEABZAKkAksCJIEsQUGAoRBTqAEIAcACAAKgAyADQAIQAhABgAQABQA; _cc_id=5e471b52571cfa6d72a1c6380b2cb67a; panoramaId_expiry=1687777165039; panoramaId=18ab58638f45f4264dc85f3ff0b14945a7026d3a1aefefabec3ff6cc68348dda; panoramaIdType=panoIndiv; _gid=GA1.2.1036825845.1687441145; _ga_6BEFL2KW6S=GS1.2.1687442526.3.0.1687442526.0.0.0; _ga=GA1.1.52073007.1619794693; __cf_bm=rUiGmrgaR4bQh2Pj3UVEeIhaQydjay.cgtf.Qm59zZA-1687604247-0-ATHlAnvt1nblaLTfFuIQ8BAXCJkxRNgqO0MPZwst+3HMZE9j5XHiGIuNPZpIg1ONVA==; cto_bundle=WlV8719OTU5paW1IYkN4TEpKJTJGUyUyRmo2bGVNVkFBTjBhTlN0d2lhRjkxNCUyQmM5WmJGcFQ1aWlEYzhaNGRnM1BXSnFlMTlGRmpUdGwxcXZ5R1REJTJCNm9HUDdJTE5INnVFMDBzUzdGcDdnVkFHOVpub2xhWTglMkZWT3Y1TllaT1dhTXlVSHpUQWtLJTJCV2dBeXozc09PZEZhNkpjbEpHT3clM0QlM0Q; __gads=ID=1b0623027a5d808e:T=1687172365:RT=1687604935:S=ALNI_MYzrEjfcQBjr2cjcJhyiuV3LUTOzg; __gpi=UID=00000c4acf5be2cd:T=1687172365:RT=1687604935:S=ALNI_MatSLGj8_ezqQgx0eEzFFGqQUKylQ; bbsessionhash=c1a1caa48f5c609a152f4f6d8fc0a2e0; bblastvisit=1687605023; bblastactivity=0; _ga_QCY7DPM9MZ=GS1.1.1687604248.11.1.1687605094.59.0.0",
            #"Origin":"https://forocoches.com",
            #"Referer":"https://forocoches.com/foro/misc.php?do=page&template=ident",
            #"Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            #"Sec-Ch-Ua-Mobile":"?0",
            #"Sec-Ch-Ua-Platform":'"Windows"',
            #"Sec-Fetch-Dest":"document",
            #"Sec-Fetch-Mode":"navigate",
            #"Sec-Fetch-Site":"same-origin",
            #"Sec-Fetch-User":"?1",
            #"Upgrade-Insecure-Requests":"1",
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        }"""


    session = requests.Session()

    """Si no se han introducido usuario y contraseña en credenciales no hay post para el logueo, a fin de evitar exceso de logueos y bloqueo temporal de acceso"""
    if not "username" in username and not "pasword" in pasword:
        session.post('https://forocoches.com/foro/login.php' , data=payload)
        
    else:
        print("Modo de funcionamiento sin cuneta, si dispone de cuneta inserte nombre de usuario y contraseña en 'credenciales.txt'")

    time.sleep(10)

    return session
