import tkinter as tk


def gerar_resposta():
    entry2.delete(0, 'end')
    txt = entry.get()
    opc = c11.get()

    if (c11.get()) == True:
        entry2.insert(0, txt)
    else:
        entry2.insert(0, 'Erro')

    #print(saida)


if __name__ == "__main__":

    ###############################################
    # Iniciando a Janela
    ###############################################
    janela = tk.Tk()
    janela.title('Tkinter - teste')
    janela.geometry('300x200')



    ################################################
    # Definindo textos e botoẽs ETC
    ################################################
    texto = tk.Label(janela, text="Digite aqui")
    texto.grid(column=0, row=1)

    entry = tk.Entry(janela)
    entry.grid(column=0, row=2)

    texto2 = tk.Label(janela, text="Saida:")
    texto2.grid(column=0, row=3)

    entry2 = tk.Entry(janela)
    entry2.grid(column=0, row=4)

    c11 = tk.BooleanVar() # Declarando variavel do CheckBox
    c1 = tk.Checkbutton(janela, text="Opção 1",variable=c11, onvalue=True, offvalue=False)
    c1.grid(column=0, row=5)


    botao = tk.Button(janela, text="Gerar", command=gerar_resposta)
    botao.grid(column=0, row=6)



    ####################################################
    # Deixando a Janela em Loop
    ####################################################
    janela.mainloop()
