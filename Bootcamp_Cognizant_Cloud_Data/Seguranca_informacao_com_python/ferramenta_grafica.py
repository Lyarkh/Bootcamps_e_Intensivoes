# código referente à aula 05 - Desenvolvendo uma ferramenta gráfica para abrir um navegador
from tkinter import *
import webbrowser

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()
