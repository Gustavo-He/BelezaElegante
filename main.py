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
import tela1
import tela2
import tela3
import telaConfirmada


class App:
    def __init__(self):
        self.reserva = {}
        self.agendamentos = []

        self.screen = ctk.CTk()
        self.screen.geometry("450x550")
        self.screen.title("Beleza Elegante")
        self.screen.resizable(False, False)

        self.telaConfirmada = telaConfirmada.Tela4(self)
        self.tela3 = tela3.Tela3(self)
        self.tela2 = tela2.Tela2(self)
        self.tela1 = tela1.Tela1(self)


app = App()
app.tela1.criar_tela()
app.screen.mainloop()
