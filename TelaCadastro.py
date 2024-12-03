from cachorro import Cachorro
from gato import Gato

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

"""Função de criação de objetos"""

lista=[]

def cadastraAnimal():
    nome=entryNome.get()
    idade=entryIdade.get()
    peso=entryPeso.get()
    tipo=varTipo.get()
    porte=entryCporte.get()
    erro=0

    if tipo=="Cachorro":
        if nome=="":
            messagebox.showerror("Erro", "Deve ser preenchido o nome do cachorro!")
            erro=1

        if idade=="":
            messagebox.showerror("Erro", "Deve ser preenchido a idade do cachorro!")
            erro=1

        if peso=="":
            messagebox.showerror("Erro", "Deve ser preenchido o peso do cachorro!")
            erro=1
        
        if porte=="":
            messagebox.showerror("Erro", "Deve ser preenchido o porte do cachorro!")
            erro=1
        
        if erro==0:
            c=Cachorro(nome, idade, peso, porte)
            salvar(c)
            messagebox.showinfo("Cadastro", f"{tipo}: Cadastrado com sucesso!")

    else:
        if tipo=="Gato":
            if nome=="":
                messagebox.showerror("Erro", "Deve ser preencido o nome do gato!")
                erro=1
            
            if idade=="":
                messagebox.showerror("Erro", "Deve ser preenchifo a idade do gato!")
                erro=1
            
            if peso=="":
                messagebox.showerror("Erro", "Deve ser preenchido a peso do gato!")
                erro=1
            
            if porte=="":
                messagebox.showerror("Erro", "Deve ser preenchido a raça do gato!")
                erro=1
            
            else:
                if erro==0:
                    g = Gato(nome, idade, peso, porte)
                    salvar(g)
                    messagebox.showinfo("Cadastro", f"{tipo}: cadastrado com sucesso!")

def salvar(obj):
    lista.append(obj)

def atualizaListabox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

##############################################

janela = tk.Tk()
janela.title("Cadastro de animal")
janela.geometry("500x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_rowconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight= 1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista")

labal1 = tk.Label(tab1, text="Nome:", font=("",15))
labal1.grid(row=0, column=0, sticky="w", padx=10)

entryNome = tk.Entry(tab1, font=("", 15))
entryNome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

labal2 = tk.Label(tab1, text="Idade:", font=("", 15))
labal2.grid(row=1, column=0, sticky="w", pady=10)

entryIdade = tk.Entry(tab1, font=("", 15))
entryIdade.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

labal3 = tk.Label(tab1, text="Peso:", font=("", 15))
labal3.grid(row=2, column=0, sticky="w", padx=10)

entryPeso = tk.Entry(tab1, font=("", 15))
entryPeso.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

labal4 = tk.Label(tab1, text="Porte/Raça", font=("", 15))
labal4.grid(row=3, column=0, sticky="w", padx=10)

entryCporte = tk.Entry(tab1, font=("", 15))
entryCporte.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo",font=("", 15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Cachorro")
tk.Radiobutton(tab1, text="Cachorro", font=("", 15), variable=varTipo, value="Cachorro").grid(row=4, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Gato", font=("", 15), variable=varTipo, value="Gato").grid(row=4, column=1, sticky="e", padx=10)

tk.Button(tab1, text="Cadastrar", font=("", 15), command=cadastraAnimal).grid(row=5, columnspan=2)

###############################################################################

listbox = tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizaListabox).grid(row=1, column=0)

janela.mainloop()
