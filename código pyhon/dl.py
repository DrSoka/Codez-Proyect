import wget

urlist = input("Ingrese la dirección URL que desea descargar: ")
urls = urlist.split(' ')

for url in urls:
    dl = wget.download(url, 'C:/YOUR_DIRECTORY')
