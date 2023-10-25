import Modulos
import customtkinter as ctk


class Tela4:
    def __init__(self, App):
        self.App = App
        self.frame = Modulos.CriarFrame(App.screen, 0, 3, 450, 700)

    def entrar(self):
        Modulos.CriarLabel(self.frame, "Serviço agendado", 0, 6)

        Modulos.CriarLabel(self.frame, "Data: " + self.App.tela1.agendamentoHora.get(), 1, 6)
        Modulos.CriarLabel(self.frame, "Hora: " + self.App.tela1.agendamentoHora.get(), 2, 6)

        agendamentos_frame = ctk.CTkFrame(self.frame)
        agendamentos_frame.grid(row=3, column=6)

        Modulos.CriarLabel(agendamentos_frame, "Serviços:", 0, 6)

        for index, nome in enumerate(self.App.agendamentos):
            Modulos.CriarLabel(agendamentos_frame, nome, (index + 1), 6)

        Modulos.CriarLabel(self.frame, "Nome: " + self.App.tela3.nomeEntry.get(), 4, 6)
        Modulos.CriarLabel(self.frame, "Telefone: " + self.App.tela3.telEntry.get(), 5, 6)
        Modulos.CriarLabel(self.frame, "E-mail: " + self.App.tela3.emailEntry.get(), 6, 6)

        self.App.tela3.frame.grid_remove()
        self.frame.grid(row=0, column=0)
