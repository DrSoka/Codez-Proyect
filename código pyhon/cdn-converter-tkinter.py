import clipboard
from tkinter import Tk, Button, Entry, StringVar

main = Tk()
main.title('CDN converter v2.1')
main.geometry("300x60")
# Usar 300x60 para una entrada solamente

def validar_entrada(ent):
    return ent

def CDN():
    url = entrada.get()
    urlp = url.split('/')
    user = urlp[3]
    repo = urlp[4]
    di = urlp[6:]
    file = '/'.join(di)
    dir_ = f'https://cdn.jsdelivr.net/gh/{user}/{repo}@{file}'
    clipboard.copy(dir_)

def clear():
    caja.delete(0, 'end')
    return

entrada = StringVar()

caja = Entry(main, textvariable=entrada)
caja.pack()
caja.place(x=20,y=20, height=20, width=200)
oc = Button(main, text="CDN", command=lambda:[CDN(), clear()]).place(x=230, y=19)

main.mainloop()
