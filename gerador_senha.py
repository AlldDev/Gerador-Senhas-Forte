import tkinter as tk
from tkinter import ttk


def gpasswd():
    return


if __name__ == "__main__":

    ###############################################
    # Iniciando a Janela
    ###############################################
    janela = tk.Tk()
    style = ttk.Style()

    janela.title('GPasswd')
    style.theme_use('alt')
    #janela.geometry('300x200')



    ################################################
    # Definindo textos e botoẽs ETC
    ################################################

    label1 = tk.Label(janela, text='Gerador de Senhas Fortes!')
    label1.grid(column=0, row=1)

    entry1 = tk.Entry(janela)
    entry1.grid(column=0, row=2, padx=20)

    botao = tk.Button(janela, text='GERAR', command=gpasswd)
    botao.grid(column=0, row=3, padx=20, pady=20)

    #entry = tk.Entry(janela)
    #entry.grid(column=0, row=2)

    #texto2 = tk.Label(janela, text="Saida:")
    #texto2.grid(column=0, row=3)

    #entry2 = tk.Entry(janela)
    #entry2.grid(column=0, row=4)

    #c11 = tk.BooleanVar() # Declarando variavel do CheckBox
    #c1 = tk.Checkbutton(janela, text="Opção 1",variable=c11, onvalue=True, offvalue=False)
    #c1.grid(column=0, row=5)


    #botao = tk.Button(janela, text="Gerar", command=gerar_resposta)
    #botao.grid(column=0, row=6)



    ####################################################
    # Deixando a Janela em Loop
    ####################################################
    janela.mainloop()
