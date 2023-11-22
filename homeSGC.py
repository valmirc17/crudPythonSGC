# Sistema de Gerenciamento de Celulares

# Importações
from tkinter import *
import tkinter as tk
import subprocess

# Funções

def abrir_crud() :
    subprocess.run(["python","crudSGC.py"])

def lougout() :
    tela.destroy()
    subprocess.run(["python","loginSGC.py"])

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

# Importação de ícones
ft_celular = PhotoImage(file=r"icones\celular.png")
ft_logout = PhotoImage(file=r"icones\logout.png")

menu = Menu(tela)


op_menu_arquivos = Menu(menu)
op_menu_sobre = Menu(menu)

menu.add_cascade(label="Arquivo",menu=op_menu_arquivos)
menu.add_cascade(label="Sobre",menu=op_menu_sobre)

# Menu Arquivo
op_menu_arquivos.add_command(label="Abrir")
op_menu_arquivos.add_command(label="Salvar")
op_menu_arquivos.add_command(label="Salvar como")
op_menu_arquivos.add_separator
op_menu_arquivos.add_command(label="Sair",command=tela.quit)

# Menu Sobre
op_menu_sobre.add_command(label="Sobre")

janela.config(menu=menu)
# Componentes da tela

btn_salvar = Button(tela, text='Controle de Celulares', font=fonte,command=abrir_crud, image=ft_celular, compound= TOP, width=150, height=150)
btn_salvar.grid(row=7, column=0, pady=5, padx=5)
btn_salvar = Button(tela, text='Logout', font=fonte,command=lougout, image=ft_logout, compound= TOP, width=150, height=150)
btn_salvar.grid(row=7, column=1, pady=5, padx=5)

tela.mainloop()