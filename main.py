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
import modulos


class App:
    def __init__(self):
        self.reserva = {}
        self.agendamentos = []

        self.screen = ctk.CTk()
        self.screen.geometry("450x700")
        self.screen.title("Beleza Elegante")
        self.screen.resizable(False, False)

        self.tela1 = ctk.CTkFrame(self.screen, width=450, height=700)
        self.tela2 = ctk.CTkFrame(self.screen, width=450, height=700)
        self.tela3 = ctk.CTkFrame(self.screen, width=450, height=700)
        self.telaConfirmada = ctk.CTkFrame(self.screen, width=450, height=700)

    def start(self):
        labelData = ctk.CTkLabel(self.tela1, text="Data")
        labelData.grid(row=0, column=0, padx=10, sticky="e")

        self.agendamentoData = modulos.criar_entrada(self.tela1, 100, 20, 0, 1, modo="data")

        labelHora = ctk.CTkLabel(self.tela1, text="Hora")
        labelHora.grid(row=1, column=0, padx=10, sticky="e")

        self.agendamentoHora = modulos.criar_entrada(self.tela1, 100, 20, 1, 1, modo="hora")

        btnServicos = ctk.CTkButton(self.tela1, text="Serviços", command=self.entrar_tela2)
        btnServicos.grid(row=2, pady=10, padx=10)

        self.btnAgendar = ctk.CTkButton(self.tela1, text="Agendar", command=self.agendar)
        self.btnAgendar.grid(row=4, pady=10, padx=10)

        self.tela1.grid(row=0, column=0)

    def agendar(self):
        if len(self.agendamentos) == 0:
            self.btnAgendar.configure(fg_color="red")
        else:
            self.entrar_tela3()

    def confirmar_agendamento(self):
        labelData = ctk.CTkLabel(self.telaConfirmada, text="Data: "+self.agendamentoData.get())
        labelData.grid(row=0)

        labelHora = ctk.CTkLabel(self.telaConfirmada, text="Hora: "+self.agendamentoHora.get())
        labelHora.grid(row=1)

        agendamentosFrame = ctk.CTkFrame(self.telaConfirmada)
        servicoTitle = ctk.CTkLabel(agendamentosFrame, text="Serviços:")
        servicoTitle.grid(row=0)

        for index, nome in enumerate(self.agendamentos):
            servicoLabel = ctk.CTkLabel(agendamentosFrame, text=nome)
            servicoLabel.grid(row=(index + 1), padx=10)

        agendamentosFrame.grid(row=2)

        nomeLabel = ctk.CTkLabel(self.telaConfirmada, text="Nome: "+self.nomeEntry.get())
        nomeLabel.grid(row=3, column=0)

        telLabel = ctk.CTkLabel(self.telaConfirmada, text="Telefone: "+self.telEntry.get())
        telLabel.grid(row=4, column=0)

        emailLabel = ctk.CTkLabel(self.telaConfirmada, text="E-mail: "+self.emailEntry.get())
        emailLabel.grid(row=5, column=0)

        self.tela3.grid_remove()
        self.telaConfirmada.grid()

    def entrar_tela3(self):
        labelData = ctk.CTkLabel(self.tela3, text="Data: "+self.agendamentoData.get())
        labelData.grid(row=0)

        labelHora = ctk.CTkLabel(self.tela3, text="Hora: "+self.agendamentoHora.get())
        labelHora.grid(row=1)

        agendamentosFrame = ctk.CTkFrame(self.tela3)
        servicoTitle = ctk.CTkLabel(agendamentosFrame, text="Serviços:")
        servicoTitle.grid(row=0)

        for index, nome in enumerate(self.agendamentos):
            servicoLabel = ctk.CTkLabel(agendamentosFrame, text=nome)
            servicoLabel.grid(row=(index + 1), padx=10)

        agendamentosFrame.grid(row=2)

        nomeLabel = ctk.CTkLabel(self.tela3, text="Nome:")
        nomeLabel.grid(row=3, column=0)

        self.nomeEntry = modulos.criar_entrada(self.tela3, 150, 20, 3, 1)

        telLabel = ctk.CTkLabel(self.tela3, text="Telefone:")
        telLabel.grid(row=4, column=0)

        self.telEntry = modulos.criar_entrada(self.tela3, 150, 20, 4, 1, modo="telefone")

        emailLabel = ctk.CTkLabel(self.tela3, text="E-mail:")
        emailLabel.grid(row=5, column=0)

        self.emailEntry = modulos.criar_entrada(self.tela3, 150, 20, 5, 1)

        btnConfirmar = ctk.CTkButton(self.tela3, text="Confirmar agendamento", command=self.confirmar_agendamento)
        btnConfirmar.grid(row=6, column=0)

        self.tela1.grid_remove()
        self.tela3.grid()

    def entrar_tela2(self):
        modulos.criar_servico(self.tela2, "Corte de cabelo", "Faz um corte daora no cabelo", "R$20", "16:00 - 19:00", 0, lambda: self.adicionar_a_reserva("Corte de cabelo"))
        modulos.criar_servico(self.tela2, "Manicure", "Deixa a mão bonita", "R$70", "8:00 - 18:00", 1, lambda: self.adicionar_a_reserva("Manicure"))
        modulos.criar_servico(self.tela2, "Pedicure", "Deixa o pé legal", "R$50", "5:00 - 14:00", 2, lambda: self.adicionar_a_reserva("Pedicure"))
        modulos.criar_servico(self.tela2, "Maquiagem", "Faz maquiagem bonita", "R$200", "9:00 - 12:00", 3, lambda: self.adicionar_a_reserva("Maquiagem"))

        btnVoltarTela = ctk.CTkButton(self.tela2, text="Voltar", command=self.entrar_tela1)
        btnVoltarTela.grid(row=4)

        self.tela2.grid(row=0, column=0)
        self.tela1.grid_remove()

    def entrar_tela1(self):
        agendamentosFrame = ctk.CTkFrame(self.tela1)

        servicoTitle = ctk.CTkLabel(agendamentosFrame, text="Serviços:")
        servicoTitle.grid(row=0)

        for index, nome in enumerate(self.agendamentos):
            servicoLabel = ctk.CTkLabel(agendamentosFrame, text=nome)
            servicoLabel.grid(row=(index + 1), padx=10)

        agendamentosFrame.grid(row=3)

        self.tela1.grid(row=0, column=0)
        self.tela2.grid_remove()

    def adicionar_a_reserva(self, nomeReserva):
        for nome in self.agendamentos:
            if nome == nomeReserva:
                break
        else:
            self.agendamentos.append(nomeReserva)


app = App()
app.start()
app.screen.mainloop()
