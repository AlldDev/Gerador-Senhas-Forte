import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import string
import random
import time
# import pyperclip

_PASSWD = None

def gpasswd():
    global _PASSWD

    entry1.delete(0, 'end')
    upr = list(string.ascii_uppercase)
    low = list(string.ascii_lowercase)
    esp = list(string.punctuation)
    num = list(string.digits)
    n_carac = None
    data = ''

    if len_passwd.get() == '12 Digitos':
        n_carac = int(12 / 4)
    elif len_passwd.get() == '16 Digitos':
        n_carac = int(16 / 4)
    elif len_passwd.get() == '20 Digitos':
        n_carac = int(20 / 4)
    elif len_passwd.get() == '32 Digitos':
        n_carac = int(32 / 4)

    passwd = [random.sample(upr, n_carac), random.sample(low, n_carac), random.sample(esp, n_carac), random.sample(num, n_carac)]
    passwd = [item for sublist in passwd for item in sublist]
    passwd = random.sample(passwd ,len(passwd))

    for i in range(len(passwd)):
        data += passwd[i]

    _PASSWD = data
    entry1.insert(0, data)

def copy_passwd():
    global _PASSWD

    janela.clipboard_clear()
    janela.clipboard_append(_PASSWD)
    janela.update()

    msg_sucess = ttk.Label(janela, text='Copiado para área de transferência!')
    msg_sucess.grid(column=0, row=4, padx=0, pady=0)
    msg_sucess.after(5000, msg_sucess.destroy)

if __name__ == "__main__":

    ###############################################
    # Iniciando a Janela
    ###############################################
    #janela = tk.Tk()
    #janelas = ttk.Style()
    #janelas.theme_use('xpnative')
    #janelas.theme_names('Ag')
    #janela = ThemedTk(theme="default")
    #janela.title('GPasswd')
    #janela.iconbitmap('icon.ico')
    #janelas.theme_use('xpnative')
    #janela.geometry('300x200')

    janela = ThemedTk(theme='breeze')
    janela.title('GPasswd')
    #janela.iconbitmap('icon.ico')

    ################################################
    # Definindo textos e botoẽs ETC
    ################################################
    #label1 = ttk.Label(janela, text='Gerador de Senhas Fortes!')
    #label1.grid(column=0, row=1)

    # Definindo o Tamanho da Senha
    len_passwd_label = ttk.Label(janela, text='Defina o Tamanho da senha:')
    len_passwd_label.grid(column=0, row=0, padx=10, pady=0)

    len_passwd_vetor = ['12 Digitos', '16 Digitos', '20 Digitos', '32 Digitos']
    len_passwd = ttk.Combobox(janela,values=len_passwd_vetor, width=29)
    len_passwd.set(len_passwd_vetor[0])
    len_passwd.grid(column=0, row=1, padx=10, pady=10)

    # Tela de Resposta
    entry1 = ttk.Entry(janela, width=32)
    entry1.grid(column=0, row=2, padx=10, pady=10)

    # Espaço da resposta do copy
    espace_copy = ttk.Label(janela)
    espace_copy.grid(column=0, row=4, padx=0, pady=0)

    # Botao copy
    copy_botao = ttk.Button(janela, text='COPIAR', command=copy_passwd)
    copy_botao.grid(column=2, row=2, padx=10, pady=10)

    # Botão para Gerar
    botao = ttk.Button(janela, text='GERAR', command=gpasswd)
    botao.grid(column=2, row=1, padx=10, pady=10)

    ####################################################
    # Deixando a Janela em Loop
    ####################################################
    janela.mainloop()
