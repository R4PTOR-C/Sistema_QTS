import tkinter as tk
from tkinter import ttk
from index import IndexPage
from new import NewPage

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Sistema CRUD com Tkinter e PostgreSQL")
        self.geometry("800x600")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (IndexPage, NewPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("IndexPage")

    def show_frame(self, page_name):
        '''Mostra um frame para o usuário'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "IndexPage":
            frame.update_table()  # Atualiza a tabela ao exibir a IndexPage

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
