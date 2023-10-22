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
        self.screen.geometry("450x700")
        self.screen.title("Beleza Elegante")
        self.screen.resizable(False, False)

        self.tela1 = Modulos.CriarFrame(self.screen, 0, 0, 450, 700)
        self.tela2 = Modulos.CriarFrame(self.screen, 0, 1, 450, 700)
        self.tela3 = Modulos.CriarFrame(self.screen, 0, 2, 450, 700)
        self.telaConfirmada = Modulos.CriarFrame(self.screen, 0, 3, 450, 700)

        # Tela 1
        self.agendamentoData = Modulos.CriarCaixaDeTexto(self.tela1, 100, 20, 0, 1, Modo="Data")
        self.agendamentoHora = Modulos.CriarCaixaDeTexto(self.tela1, 100, 20, 1, 1, Modo="Hora")
        self.btnAgendar = Modulos.CriarBotão(self.tela1, "Agendar", self.agendar, 4, 0, 100, 50)


        # Tela 2

    def start(self):
        Modulos.CriarLabel(self.tela1, "Data", 0, 0)

        Modulos.CriarLabel(self.tela1, "Hora", 1, 0)

        Modulos.CriarBotão(self.tela1, "Serviços", self.entrar_tela2, 2, 0, 100, 50)

        self.tela1.grid(row=0, column=0)

    def agendar(self):
        if len(self.agendamentos) == 0:
            self.btnAgendar.configure(fg_color="red")
        else:
            self.entrar_tela3()

    def confirmar_agendamento(self):
        Modulos.CriarLabel(self.telaConfirmada, "Data: "+self.agendamentoHora.get(), 0, 0)
        Modulos.CriarLabel(self.telaConfirmada, "Hora: "+self.agendamentoHora.get(), 1, 0)

        agendamentos_frame = ctk.CTkFrame(self.telaConfirmada)
        agendamentos_frame.grid(row=2, column=0)

        Modulos.CriarLabel(agendamentos_frame, "Serviços:", 0, 0)

        for index, nome in enumerate(self.agendamentos):
            Modulos.CriarLabel(agendamentos_frame, nome, (index+1), 0)

        Modulos.CriarLabel(self.telaConfirmada, "Nome: "+self.nomeEntry.get(), 3, 0)
        Modulos.CriarLabel(self.telaConfirmada, "Telefone: "+self.telEntry.get(), 4, 0)
        Modulos.CriarLabel(self.telaConfirmada, "E-mail: "+self.emailEntry.get(), 5, 0)

        self.tela3.grid_remove()
        self.telaConfirmada.grid(row=0, column=0)

    def entrar_tela3(self):
        Modulos.CriarLabel(self.tela3, "Data: "+self.agendamentoData.get(), 0, 0)
        Modulos.CriarLabel(self.tela3, "Hora: "+self.agendamentoHora.get(), 1, 0)

        agendamentosFrame = ctk.CTkFrame(self.tela3)
        agendamentosFrame.grid(row=2, column=0)

        Modulos.CriarLabel(agendamentosFrame, "Serviços:", 0, 0)

        for index, nome in enumerate(self.agendamentos):
            Modulos.CriarLabel(agendamentosFrame, nome, index+1, 0)

        Modulos.CriarLabel(self.tela3, "Nome:", 3, 0)
        self.nomeEntry = Modulos.CriarCaixaDeTexto(self.tela3, 150, 20, 3, 1)

        Modulos.CriarLabel(self.tela3, "Telefone:", 4, 0)
        self.telEntry = Modulos.CriarCaixaDeTexto(self.tela3, 150, 20, 4, 1, Modo="Telefone")

        Modulos.CriarLabel(self.tela3, "E-mail:", 5, 0)
        self.emailEntry = Modulos.CriarCaixaDeTexto(self.tela3, 150, 20, 5, 1)

        Modulos.CriarBotão(self.tela3, "Confirmar agendamento", self.confirmar_agendamento, 6, 0, 80, 15)

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
        agendamentosFrame = ctk.CTkFrame(self.tela1)
        agendamentosFrame.grid(row=3)

        Modulos.CriarLabel(agendamentosFrame, "Serviços:", 0, 0)

        for index, nome in enumerate(self.agendamentos):
            Modulos.CriarLabel(agendamentosFrame, nome, index+1, 0)

        self.tela2.grid_remove()
        self.tela1.grid(row=0, column=0)

    def adicionar_a_reserva(self, nomeReserva):
        for nome in self.agendamentos:
            if nome == nomeReserva:
                break
        else:
            self.agendamentos.append(nomeReserva)


app = App()
app.start()
app.screen.mainloop()
