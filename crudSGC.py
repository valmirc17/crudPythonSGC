# Sistema de Gerenciamento de Celulares

# Importações
from tkinter import *
import tkinter as tk
import pymongo

# Funções
def Salvar() :
    codigo = txt_codigo.get()
    marca = txt_marca.get()
    modelo = txt_modelo.get()
    memoria = txt_memoria.get()
    sistema = txt_sistema.get()
    cor = txt_cor.get()
    
    txt_codigo.delete(0,tk.END)
    txt_marca.delete(0,tk.END)
    txt_modelo.delete(0,tk.END)
    txt_memoria.delete(0,tk.END)
    txt_sistema.delete(0,tk.END)
    txt_cor.delete(0,tk.END)
    
    celular = {"codigo": codigo, "marca": marca, "modelo": modelo, "memoria" : memoria, "sistema" : sistema, "cor" : cor}
    collection.insert_one(celular)

def Alterar() :
    codigo = txt_codigo.get()
    marca = txt_marca.get()
    modelo = txt_modelo.get()
    memoria = txt_memoria.get()
    sistema = txt_sistema.get()
    cor = txt_cor.get()
    
    txt_codigo.delete(0,tk.END)
    txt_marca.delete(0,tk.END)
    txt_modelo.delete(0,tk.END)
    txt_memoria.delete(0,tk.END)
    txt_sistema.delete(0,tk.END)
    txt_cor.delete(0,tk.END)
    
    celular = {"marca": marca, "modelo": modelo, "memoria" : memoria, "sistema" : sistema, "cor" : cor}
    collection.update_one({"codigo": codigo},{"$set":celular})

def Excluir() :
    codigo = txt_codigo.get()
    collection.delete_one({"codigo": codigo})

def Consultar() :
    codigo = txt_codigo.get()
    resultado = collection.find_one({"codigo": codigo})

    if resultado :
        txt_marca.insert(END, f"{resultado['marca']}\n")
        txt_modelo.insert(END, f"{resultado['modelo']}\n")
        txt_memoria.insert(END, f"{resultado['memoria']}\n")
        txt_sistema.insert(END, f"{resultado['sistema']}\n")
        txt_cor.insert(END, f"{resultado['cor']}\n")
        
    else :
        lbl_resultado.config(text="Nenhum resultado encontrado!")


# Configuração da janela
janela = Tk()
janela.title("Sistema de Gerenciamento de Celulares")

largura_janela = 800
altura_janela = 600

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 12)

# Frame para centralizar os itens na tela
tela = Frame(janela)
tela.pack(expand=True, padx=20, pady=20)

# Conexão com o BD
banco = pymongo.MongoClient("mongodb://localhost:27017/")
db = banco["banco"]
collection = db["celulares"]

# Importação de ícones
ft_salvar = PhotoImage(file=r"icones\salvar.png")
ft_alterar = PhotoImage(file=r"icones\alterar.png")
ft_excluir = PhotoImage(file=r"icones\excluir.png")
ft_procurar = PhotoImage(file=r"icones\procurar.png")
ft_sair = PhotoImage(file=r"icones\sair.png")

# Componentes da tela
Label(tela, text="Sistema de Gerenciamento de Celulares", font=("Arial", 18)).grid(row=0, columnspan=2, pady=10)

lbl_codigo = Label(tela, text='Código:', font=fonte)
lbl_codigo.grid(row=1, column=0)
txt_codigo = Entry(tela)
txt_codigo.grid(row=1, column=1, pady=5)

lbl_marca = Label(tela, text='Marca:', font=fonte)
lbl_marca.grid(row=2, column=0)
txt_marca = Entry(tela)
txt_marca.grid(row=2, column=1, pady=5)

lbl_modelo = Label(tela, text='Modelo:', font=fonte)
lbl_modelo.grid(row=3, column=0)
txt_modelo = Entry(tela)
txt_modelo.grid(row=3, column=1, pady=5)

lbl_memoria = Label(tela, text='Memoria:', font=fonte)
lbl_memoria.grid(row=4, column=0)
txt_memoria = Entry(tela)
txt_memoria.grid(row=4, column=1, pady=5)

lbl_sistema = Label(tela, text='Sistema:', font=fonte)
lbl_sistema.grid(row=5, column=0)
txt_sistema = Entry(tela)
txt_sistema.grid(row=5, column=1, pady=5)

lbl_cor = Label(tela, text='Cor:', font=fonte)
lbl_cor.grid(row=6, column=0)
txt_cor = Entry(tela)
txt_cor.grid(row=6, column=1, pady=5)

btn_salvar = Button(tela, text='Salvar', font=fonte, command=Salvar, image=ft_salvar, compound= TOP, width=60, height=60)
btn_salvar.grid(row=7, column=0, pady=5, padx=5)

btn_alterar = Button(tela, text='Alterar', font=fonte, command=Alterar, image=ft_alterar, compound = TOP, width=60, height=60)
btn_alterar.grid(row=7, column=1, pady=5, padx=5)

btn_excluir = Button(tela, text='Excluir', font=fonte, command=Excluir, image=ft_excluir, compound = TOP, width=60, height=60)
btn_excluir.grid(row=8, column=0, pady=5, padx=5)

btn_consultar = Button(tela, text='Consultar', font=('Arial', 11), command=Consultar, image=ft_procurar, compound = TOP, width=60, height=60)
btn_consultar.grid(row=8, column=1, pady=5, padx=5)

btn_sair = Button(tela, text='Sair', font=fonte, command=janela.quit, image = ft_sair, compound = TOP, width=60, height=60)
btn_sair.grid(row=9, column=0, pady=5, padx=5)

lbl_resultado = Label(tela, text='', font=fonte)
lbl_resultado.grid(row=9, column=1)

tela.mainloop()