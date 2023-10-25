import Modulos
import customtkinter as ctk


class Tela1:
    def __init__(self, App):
        self.App = App
        self.frame = Modulos.CriarFrame(App.screen, 0, 0, 450, 700)

        self.ErrorLabel = Modulos.CriarLabel(self.frame, "", 3, 0)
        self.FrameAgendamentos = ctk.CTkFrame(self.frame)

        self.tela2_entrar = App.tela2.entrar

    def criar_tela(self):
        Modulos.CriarLabel(self.frame, "Beleza Elegante", 0, 0)

        frameInputs = Modulos.CriarFrame(self.frame, 1, 0, 120, 60)

        frameData = Modulos.CriarFrame(frameInputs, 0, 0, 120, 30)
        Modulos.CriarLabel(frameData, "Data", 0, 0, padx=10)
        self.agendamentoData = Modulos.CriarCaixaDeTexto(frameData, 100, 20, 0, 1, Modo="Data")

        frameHora = Modulos.CriarFrame(frameInputs, 1, 0, 120, 30)
        Modulos.CriarLabel(frameHora, "Hora", 0, 0, padx=10)
        self.agendamentoHora = Modulos.CriarCaixaDeTexto(frameHora, 100, 20, 0, 1, Modo="Hora")

        Modulos.CriarBotão(self.frame, "Serviços", self.tela2_entrar, 1, 1, 100, 50)
        self.btnAgendar = Modulos.CriarBotão(self.frame, "Agendar", self.agendar_servico, 2, 0, 100, 50)

    def entrar(self):
        self.FrameAgendamentos.destroy()

        self.FrameAgendamentos = ctk.CTkFrame(self.frame)
        self.FrameAgendamentos.grid(row=2, column=1)

        servicosTitle = Modulos.CriarLabel(self.FrameAgendamentos, "Serviços:", 0, 0)
        servicosTitle.configure(width=120, anchor="w", padx=5)

        for index, nome in enumerate(self.App.agendamentos):
            tempLabel = Modulos.CriarLabel(self.FrameAgendamentos, "- " + nome, index + 1, 0)
            tempLabel.configure(width=100, anchor="w")

        self.App.tela2.frame.grid_remove()
        self.frame.grid(row=0, column=0)

    def agendar_servico(self):
        error_list = []
        length_bool = len(self.App.agendamentos) > 0
        data_bool = Modulos.checar_data(self.agendamentoData.get())
        hora_bool = Modulos.checar_hora(self.agendamentoHora.get(), self.App.agendamentos)

        if length_bool and data_bool and hora_bool:
            self.App.tela3.entrar()
        else:
            if not length_bool:
                error_list.append("Não há agendamentos")

            if not data_bool:
                error_list.append("Essa data não é permitida")

            if not hora_bool:
                error_list.append("Essa hora não é permitida")

            self.raise_error(error_list)
            self.btnAgendar.configure(fg_color="darkred")

    def raise_error(self, error_list):
        texto = "Erro:\n"
        for error in error_list:
            texto += error+"\n"

        self.ErrorLabel.configure(text=texto)
