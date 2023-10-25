import Modulos
import customtkinter as ctk


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
