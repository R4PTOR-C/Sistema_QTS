import tkinter as tk
from tkinter import ttk, messagebox
from db import insert_aluno, get_all_alunos


class NewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Botão para voltar para a tela de lista de alunos
        ttk.Button(self, text="Voltar para a lista de alunos",
                   command=lambda: controller.show_frame("IndexPage")).pack()

        # Chama a função para criar a UI de inserção de alunos dentro deste frame
        self.create_insert_ui()

    def create_insert_ui(self):
        # Frame para inserção de dados
        insert_frame = ttk.Frame(self)
        insert_frame.pack(pady=20, padx=20, fill="x", expand=True)

        # Cria e organiza os campos de entrada e o botão de inserção
        nome_entry = self.create_entry(insert_frame, "Nome:", 0)
        matricula_entry = self.create_entry(insert_frame, "Matricula:", 1)
        cpf_entry = self.create_entry(insert_frame, "CPF:", 2)
        cursos_entry = self.create_entry(insert_frame, "Curso:", 3)

        # Botão para inserir os dados no banco
        insert_button = ttk.Button(insert_frame, text="Inserir Aluno",
                                   command=lambda: self.insert_aluno_and_clear(nome_entry, matricula_entry, cpf_entry,
                                                                               cursos_entry))
        insert_button.pack(side="left", padx=(10, 0))

    def create_entry(self, frame, label, row):
        ttk.Label(frame, text=label).pack(side="top", fill="x", expand=True)
        entry = ttk.Entry(frame)
        entry.pack(side="top", fill="x", expand=True, padx=5, pady=5)
        return entry

    def insert_aluno_and_clear(self, nome_entry, matricula_entry, cpf_entry, cursos_entry):
        # Extrai os dados das entradas
        nome = nome_entry.get()
        matricula = matricula_entry.get()
        cpf = cpf_entry.get()
        cursos = cursos_entry.get()

        # Verifica se os campos não estão vazios
        if nome and cursos:
            # Insere no banco de dados
            try:
                insert_aluno(nome, matricula, cpf, cursos)
                messagebox.showinfo("Sucesso", "Aluno inserido com sucesso.")
                # Limpa os campos após a inserção
                nome_entry.delete(0, 'end')
                cursos_entry.delete(0, 'end')
                matricula_entry.delete(0, 'end')
                cpf_entry.delete(0, 'end')
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir aluno: {e}")
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
