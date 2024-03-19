import tkinter as tk
from tkinter import ttk
from db import get_all_alunos


class IndexPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Sua lógica de UI aqui, por exemplo, um botão para ir para NewPage
        ttk.Button(self, text="Adicionar Novo Aluno",
                   command=lambda: controller.show_frame("NewPage")).pack()
        # Adicionar a tabela aqui diretamente ou chamar create_table
        self.tree = self.create_table()
        self.tree.pack(pady=20)


    def create_table(self):
        # Cria o Treeview widget como uma tabela
        tree = ttk.Treeview(self)

        # Define as colunas
        tree['columns'] = ('ID', 'Nome','Matricula','CPF', 'Curso')


        # Formata as colunas
        tree.column("#0", width=0, stretch=tk.NO)  # Coluna fantasma
        tree.column("ID", anchor=tk.W, width=100)
        tree.column("Nome", anchor=tk.W, width=200)
        tree.column("Matricula", anchor=tk.W, width=200)
        tree.column("CPF", anchor=tk.W, width=200)
        tree.column("Curso", anchor=tk.W, width=300)

        # Cria os cabeçalhos das colunas
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("ID", text="ID", anchor=tk.W)
        tree.heading("Nome", text="Nome", anchor=tk.W)
        tree.heading("Matricula", text="Matricula", anchor=tk.W)
        tree.heading("CPF", text="CPF", anchor=tk.W)
        tree.heading("Curso", text="Curso", anchor=tk.W)

        # Chama a função para obter dados do banco de dados
        alunos = get_all_alunos()

        # Insere os dados na Treeview
        if alunos:
            for aluno in alunos:
                tree.insert('', 'end', values=aluno)  # Adiciona cada aluno como uma nova linha

        return tree

    def update_table(self):
        # Primeiro, limpa a tabela
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Então, recarrega os dados
        alunos = get_all_alunos()
        for aluno in alunos:
            self.tree.insert('', 'end', values=aluno)