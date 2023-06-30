from bs4 import BeautifulSoup



def extraer_num_pag_del_hilo(url_fc,thread_number,session):

    url = url_fc + str(thread_number) + "&page=0"

    r = session.get(url)
    
    if r.status_code == 200:

        


        soup = BeautifulSoup(r.text, 'lxml')

        thread_title = str(soup.title)
        thread_title = thread_title.replace("<title>","")
        thread_title = thread_title.split("-")
        thread_title = thread_title[0]


        page_links = soup.find_all('a')

        url_bruta = ""
        amount_pages_of_thread = 0
        urls_list = []

        for link in page_links:
            if ("showthread.php?t=" + str(thread_number) + "&amp;page=") and ("Mostrar Resultados") in str(link):
                url_bruta = str(link)
                url_bruta = url_bruta.replace('<a href="showthread.php?t=' + str(thread_number) + "&amp;page=","")
                url_bruta = url_bruta.replace('"',"")
                url_bruta = url_bruta.split(" ")
                url_bruta = url_bruta[0]
                amount_pages_of_thread = int(url_bruta)

                urls_list.append(amount_pages_of_thread)

        if urls_list == []:
            urls_list.append(1)
        
        urls_list = sorted(urls_list)

        amount_pages_of_thread = urls_list[-1]
        


    return thread_title,amount_pages_of_thread

