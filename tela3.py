import Modulos
import customtkinter as ctk


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
