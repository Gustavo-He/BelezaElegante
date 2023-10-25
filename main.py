# Tela 1: Tela de Agendamento de Serviços
# Esta é a tela inicial do aplicativo.
# Deve permitir que os clientes escolham a data e a hora desejadas para agendar serviços de beleza.
# Deve listar os serviços disponíveis, como corte de cabelo, manicure, pedicure, etc.
# Os clientes devem poder selecionar os serviços desejados.
# Deve mostrar a disponibilidade de horários para cada serviço.
# Deve haver um botão "Agendar" para confirmar o agendamento.

# Tela 2: Tela de Visualização de Serviços
# Esta tela permite que os clientes visualizem os serviços oferecidos pelo salão de beleza.
# Deve listar todos os serviços disponíveis, incluindo nome, descrição e preço.
# Deve permitir que os clientes escolham serviços para agendar na Tela 1.
# Deve haver um botão "Agendar" ao lado de cada serviço para adicionar à reserva.

# Tela 3: Tela de Confirmação de Agendamento
# Esta tela é exibida após o cliente confirmar um agendamento na Tela 1.
# Deve mostrar os detalhes do agendamento, incluindo a data, hora e serviços selecionados.
# Deve solicitar ao cliente informações de contato, como nome, número de telefone e e-mail.
# Deve incluir um botão "Confirmar Agendamento" para finalizar o agendamento.


import customtkinter as ctk
import Modulos


class App:
    def __init__(self):
        self.reserva = {}
        self.agendamentos = []

        self.screen = ctk.CTk()
        self.screen.geometry("450x550")
        self.screen.title("Beleza Elegante")
        self.screen.resizable(False, False)

        self.tela1 = Modulos.CriarFrame(self.screen, 0, 0, 450, 700)
        self.tela1ErrorLabel = Modulos.CriarLabel(self.tela1, "", 3, 0)

        self.tela2 = Modulos.CriarFrame(self.screen, 0, 1, 450, 700)
        self.tela3 = Modulos.CriarFrame(self.screen, 0, 2, 450, 700)
        self.tela3ErrorLabel = Modulos.CriarLabel(self.tela3, "", 6, 0)

        self.telaConfirmada = Modulos.CriarFrame(self.screen, 0, 3, 450, 700)

        self.agendamentosFrame = ctk.CTkFrame(self.tela1)

    def start(self):
        Modulos.CriarLabel(self.tela1, "Beleza Elegante", 0, 0)

        frameInputs = Modulos.CriarFrame(self.tela1, 1, 0, 120, 60)

        frameData = Modulos.CriarFrame(frameInputs, 0, 0, 120, 30)
        Modulos.CriarLabel(frameData, "Data", 0, 0, padx=10)
        self.agendamentoData = Modulos.CriarCaixaDeTexto(frameData, 100, 20, 0, 1, Modo="Data")

        frameHora = Modulos.CriarFrame(frameInputs, 1, 0, 120, 30)
        Modulos.CriarLabel(frameHora, "Hora", 0, 0, padx=10)
        self.agendamentoHora = Modulos.CriarCaixaDeTexto(frameHora, 100, 20, 0, 1, Modo="Hora")

        Modulos.CriarBotão(self.tela1, "Serviços", self.entrar_tela2, 1, 1, 100, 50)
        self.btnAgendar = Modulos.CriarBotão(self.tela1, "Agendar", self.agendar, 2, 0, 100, 50)

    def tela1_raise_error(self, error_list):
        texto = "Erro:\n"
        for error in error_list:
            texto += error+"\n"

        self.tela1ErrorLabel.configure(text=texto)

    def agendar(self):
        error_list = []
        length_bool = len(self.agendamentos) > 0
        data_bool = Modulos.checar_data(self.agendamentoData.get())
        hora_bool = Modulos.checar_hora(self.agendamentoHora.get(), self.agendamentos)

        if length_bool and data_bool and hora_bool:
            self.entrar_tela3()
        else:
            if not length_bool:
                error_list.append("Não há agendamentos")

            if not data_bool:
                error_list.append("Essa data não é permitida")

            if not hora_bool:
                error_list.append("Essa hora não é permitida")

            self.tela1_raise_error(error_list)
            self.btnAgendar.configure(fg_color="darkred")

    def confirmar_agendamento(self):
        nome_bool = len(self.nomeEntry.get()) > 0
        tel_bool = len(self.telEntry.get()) == 14
        email_bool = Modulos.checar_email(self.emailEntry.get())

        if nome_bool and tel_bool and email_bool:
            Modulos.CriarLabel(self.telaConfirmada, "Serviço agendado", 0, 6)

            Modulos.CriarLabel(self.telaConfirmada, "Data: "+self.agendamentoHora.get(), 1, 6)
            Modulos.CriarLabel(self.telaConfirmada, "Hora: "+self.agendamentoHora.get(), 2, 6)

            agendamentos_frame = ctk.CTkFrame(self.telaConfirmada)
            agendamentos_frame.grid(row=3, column=6)

            Modulos.CriarLabel(agendamentos_frame, "Serviços:", 0, 6)

            for index, nome in enumerate(self.agendamentos):
                Modulos.CriarLabel(agendamentos_frame, nome, (index+1), 6)

            Modulos.CriarLabel(self.telaConfirmada, "Nome: "+self.nomeEntry.get(), 4, 6)
            Modulos.CriarLabel(self.telaConfirmada, "Telefone: "+self.telEntry.get(), 5, 6)
            Modulos.CriarLabel(self.telaConfirmada, "E-mail: "+self.emailEntry.get(), 6, 6)

            self.tela3.grid_remove()
            self.telaConfirmada.grid(row=0, column=0)
        else:
            error_list = []

            if not nome_bool:
                error_list.append("O nome não é válido")

            if not tel_bool:
                error_list.append("O telefone não é válido")

            if not email_bool:
                error_list.append("O email não é válido")

            self.tela3_raise_error(error_list)

            self.confirmarAgendamentoBtn.configure(fg_color="darkred")

    def entrar_tela3(self):
        frameDataHora = Modulos.CriarFrame(self.tela3, 0, 0, 100, 50)

        Modulos.CriarLabel(frameDataHora, "Data: "+self.agendamentoData.get(), 0, 0)
        Modulos.CriarLabel(frameDataHora, "Hora: "+self.agendamentoHora.get(), 1, 0)

        agendamentosFrame = ctk.CTkFrame(self.tela3)
        agendamentosFrame.grid(row=0, column=1)

        Modulos.CriarLabel(agendamentosFrame, "Serviços:", 0, 0)

        for index, nome in enumerate(self.agendamentos):
            Modulos.CriarLabel(agendamentosFrame, "- "+nome, index+1, 0)

        nomeFrame = Modulos.CriarFrame(self.tela3, 2, 0, 200, 20)
        Modulos.CriarLabel(nomeFrame, "Nome  ", 0, 0)
        self.nomeEntry = Modulos.CriarCaixaDeTexto(nomeFrame, 150, 20, 0, 1, Modo="Nome")
        self.nomeEntry.configure()

        telFrame = Modulos.CriarFrame(self.tela3, 3, 0, 200, 20)
        Modulos.CriarLabel(telFrame, "Telefone  ", 0, 0)
        self.telEntry = Modulos.CriarCaixaDeTexto(telFrame, 150, 20, 0, 1, Modo="Telefone")

        emailFrame = Modulos.CriarFrame(self.tela3, 4, 0, 200, 20)
        Modulos.CriarLabel(emailFrame, "E-mail  ", 0, 0)
        self.emailEntry = Modulos.CriarCaixaDeTexto(emailFrame, 150, 20, 0, 1)

        self.confirmarAgendamentoBtn = Modulos.CriarBotão(self.tela3, "Confirmar agendamento", self.confirmar_agendamento, 5, 0, 80, 15)

        self.tela1.grid_remove()
        self.tela3.grid(row=0, column=0)

    def entrar_tela2(self):
        Modulos.criar_servico(self.tela2, "Corte de cabelo", "Faz um corte daora no cabelo", "R$20", "16:00 - 19:00", 0, lambda: self.adicionar_a_reserva("Corte de cabelo"))
        Modulos.criar_servico(self.tela2, "Manicure", "Deixa a mão bonita", "R$70", "8:00 - 18:00", 1, lambda: self.adicionar_a_reserva("Manicure"))
        Modulos.criar_servico(self.tela2, "Pedicure", "Deixa o pé legal", "R$50", "5:00 - 14:00", 2, lambda: self.adicionar_a_reserva("Pedicure"))
        Modulos.criar_servico(self.tela2, "Maquiagem", "Faz maquiagem bonita", "R$200", "9:00 - 12:00", 3, lambda: self.adicionar_a_reserva("Maquiagem"))

        Modulos.CriarBotão(self.tela2, "Voltar", self.entrar_tela1, 4, 0, 80, 15)

        self.tela1.grid_remove()
        self.tela2.grid(row=0, column=0)

    def entrar_tela1(self):
        self.agendamentosFrame.destroy()

        self.agendamentosFrame = ctk.CTkFrame(self.tela1)
        self.agendamentosFrame.grid(row=2, column=1)

        servicosTitle = Modulos.CriarLabel(self.agendamentosFrame, "Serviços:", 0, 0)
        servicosTitle.configure(width=120, anchor="w", padx=5)

        for index, nome in enumerate(self.agendamentos):
            tempLabel = Modulos.CriarLabel(self.agendamentosFrame, "- "+nome, index+1, 0)
            tempLabel.configure(width=100, anchor="w")

        self.tela2.grid_remove()
        self.tela1.grid(row=0, column=0)

    def adicionar_a_reserva(self, nomeReserva):
        for index in range(len(self.agendamentos)):
            if self.agendamentos[index] == nomeReserva:
                self.agendamentos.pop(index)
                break
        else:
            self.agendamentos.append(nomeReserva)

    def tela3_raise_error(self, error_list):
        text = ""
        for error in error_list:
            text += error+"\n"

        self.tela3ErrorLabel.configure(text=text)



app = App()
app.start()
app.screen.mainloop()
