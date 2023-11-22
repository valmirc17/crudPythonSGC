# Sistema de Gerenciamento de Celulares

# Importações
from tkinter import *
import tkinter as tk

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
ft_salvar = PhotoImage(file=r"icones\salvar.png")
ft_alterar = PhotoImage(file=r"icones\alterar.png")
ft_excluir = PhotoImage(file=r"icones\excluir.png")
ft_procurar = PhotoImage(file=r"icones\procurar.png")
ft_sair = PhotoImage(file=r"icones\sair.png")

menu = Menu(tela)
janela.config(menu=menu)

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

tela.mainloop()