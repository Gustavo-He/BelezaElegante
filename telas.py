import customtkinter as ctk
import Modulos


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


class Tela2:
    def __init__(self, App):
        self.App = App
        self.frame = Modulos.CriarFrame(App.screen, 0, 1, 450, 700)

    def entrar(self):
        Modulos.criar_servico(self.frame, "Corte de cabelo", "Faz um corte daora no cabelo", "R$20", "16:00 - 19:00", 0, lambda: self.adicionar_a_reserva("Corte de cabelo"))
        Modulos.criar_servico(self.frame, "Manicure", "Deixa a mão bonita", "R$70", "8:00 - 18:00", 1, lambda: self.adicionar_a_reserva("Manicure"))
        Modulos.criar_servico(self.frame, "Pedicure", "Deixa o pé legal", "R$50", "5:00 - 14:00", 2, lambda: self.adicionar_a_reserva("Pedicure"))
        Modulos.criar_servico(self.frame, "Maquiagem", "Faz maquiagem bonita", "R$200", "9:00 - 12:00", 3, lambda: self.adicionar_a_reserva("Maquiagem"))

        Modulos.CriarBotão(self.frame, "Voltar", self.App.tela1.entrar, 4, 0, 80, 15)

        self.App.tela1.frame.grid_remove()
        self.frame.grid(row=0, column=0)

    def adicionar_a_reserva(self, nomeReserva):
        for index in range(len(self.App.agendamentos)):
            if self.App.agendamentos[index] == nomeReserva:
                self.App.agendamentos.pop(index)
                break
        else:
            self.App.agendamentos.append(nomeReserva)


class Tela3:
    def __init__(self, App):
        self.App = App
        self.frame = Modulos.CriarFrame(App.screen, 0, 2, 450, 700)
        self.ErrorLabel = Modulos.CriarLabel(self.frame, "", 6, 0)

    def entrar(self):
        frameDataHora = Modulos.CriarFrame(self.frame, 0, 0, 100, 50)

        Modulos.CriarLabel(frameDataHora, "Data: "+self.App.tela1.agendamentoData.get(), 0, 0)
        Modulos.CriarLabel(frameDataHora, "Hora: "+self.App.tela1.agendamentoHora.get(), 1, 0)

        agendamentosFrame = ctk.CTkFrame(self.frame)
        agendamentosFrame.grid(row=0, column=1)

        Modulos.CriarLabel(agendamentosFrame, "Serviços:", 0, 0)

        for index, nome in enumerate(self.App.agendamentos):
            Modulos.CriarLabel(agendamentosFrame, "- "+nome, index+1, 0)

        nomeFrame = Modulos.CriarFrame(self.frame, 2, 0, 200, 20)
        Modulos.CriarLabel(nomeFrame, "Nome  ", 0, 0)
        self.nomeEntry = Modulos.CriarCaixaDeTexto(nomeFrame, 150, 20, 0, 1, Modo="Nome")
        self.nomeEntry.configure()

        telFrame = Modulos.CriarFrame(self.frame, 3, 0, 200, 20)
        Modulos.CriarLabel(telFrame, "Telefone  ", 0, 0)
        self.telEntry = Modulos.CriarCaixaDeTexto(telFrame, 150, 20, 0, 1, Modo="Telefone")

        emailFrame = Modulos.CriarFrame(self.frame, 4, 0, 200, 20)
        Modulos.CriarLabel(emailFrame, "E-mail  ", 0, 0)
        self.emailEntry = Modulos.CriarCaixaDeTexto(emailFrame, 150, 20, 0, 1)

        self.confirmarAgendamentoBtn = Modulos.CriarBotão(self.frame, "Confirmar agendamento", self.confirmar_agendamento, 5, 0, 80, 15)

        self.App.tela1.frame.grid_remove()
        self.frame.grid(row=0, column=0)

    def raise_error(self, error_list):
        text = ""
        for error in error_list:
            text += error+"\n"

        self.ErrorLabel.configure(text=text)

    def confirmar_agendamento(self):
        nome_bool = len(self.nomeEntry.get()) > 0
        tel_bool = len(self.telEntry.get()) == 14
        email_bool = Modulos.checar_email(self.emailEntry.get())

        if nome_bool and tel_bool and email_bool:
            self.App.telaConfirmada.entrar()
        else:
            error_list = []

            if not nome_bool:
                error_list.append("O nome não é válido")

            if not tel_bool:
                error_list.append("O telefone não é válido")

            if not email_bool:
                error_list.append("O email não é válido")

            self.raise_error(error_list)

            self.confirmarAgendamentoBtn.configure(fg_color="darkred")


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
