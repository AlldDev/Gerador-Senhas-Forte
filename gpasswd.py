import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import string
import random


def gpasswd():
    entry1.delete(0, 'end')
    upr = list(string.ascii_uppercase)
    low = list(string.ascii_lowercase)
    esp = list(string.punctuation)
    num = list(string.digits)
    data = ''

    passwd = [random.sample(upr, 5), random.sample(low, 5), random.sample(esp, 5), random.sample(num, 5)]
    passwd = [item for sublist in passwd for item in sublist]
    passwd = random.sample(passwd ,len(passwd))

    for i in range(len(passwd)):
        data += passwd[i]

    entry1.insert(0, data)

if __name__ == "__main__":

    ###############################################
    # Iniciando a Janela
    ###############################################
    #janela = tk.Tk()
    #style = ttk.Style()
    janela = ThemedTk(theme="breeze")
    janela.title('GPasswd')
    #janela.iconbitmap('icon.ico')
    #style.theme_use('alt')
    #janela.geometry('300x200')



    ################################################
    # Definindo textos e botoẽs ETC
    ################################################
    label1 = ttk.Label(janela, text='Gerador de Senhas Fortes!')
    label1.grid(column=0, row=1)

    entry1 = ttk.Entry(janela, width=25)
    entry1.grid(column=0, row=2, padx=20)

    botao = ttk.Button(janela, text='GERAR', command=gpasswd)
    botao.grid(column=0, row=3, padx=20, pady=20)

    ####################################################
    # Deixando a Janela em Loop
    ####################################################
    janela.mainloop()
