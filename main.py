import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def submit_form():
    # Substitua isso pelo seu código real que lida com a submissão do formulário
    print("Formulário enviado")

root = ThemedTk()
root.title("Formulário de Inscrição")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.minsize(500, 300)

# Configura a janela para ser responsiva
for i in range(30):  # Corrigido para 4 linhas de widgets reais
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style(root)
style.theme_use('breeze')

# Corrige a sobreposição colocando cada widget em sua própria linha
label_name = ttk.Label(root, text="Nome:")
label_name.grid(row=0, column=0, sticky="ew", padx=10, pady=(0, 10))
entry_name = ttk.Entry(root)
entry_name.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))

label_matricula = ttk.Label(root, text="Matricula:")
label_matricula.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
entry_matricula = ttk.Entry(root)
entry_matricula.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))

label_cpf = ttk.Label(root, text="CPF:")
label_cpf.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 10))
entry_cpf = ttk.Entry(root)
entry_cpf.grid(row=5, column=0, sticky="ew", padx=10, pady=(0, 10))

submit_btn = ttk.Button(root, text="Enviar", command=submit_form)
submit_btn.grid(row=20, column=0, columnspan=2, sticky="ew", padx=10, pady=20)

root.mainloop()
