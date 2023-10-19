import customtkinter as ctk


def criar_entrada(local, largura, altura, linha, coluna, placeholder="", modo="normal"):
    entrada = ctk.CTkEntry(local, width=largura, height=altura, placeholder_text=placeholder)
    entrada.grid(row=linha, column=coluna)

    if modo == "hora":
        def format_hora(event=None):
            text = entrada.get().replace(":", "")[:4]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return

            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue

                if index == 1:
                    new_text += text[index] + ":"
                else:
                    new_text += text[index]

            entrada.delete(0, "end")
            entrada.insert(0, new_text)

        entrada.bind("<KeyRelease>", format_hora)

    elif modo == "data":
        def format_data(event=None):
            text = entrada.get().replace("/", "")[:8]
            new_text = ""

            if event.keysym.lower() == "backspace":
                return

            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue

                if index in [1, 3]:
                    new_text += text[index] + "/"

                elif index == 9:
                    new_text += text[index]

                else:
                    new_text += text[index]

            entrada.delete(0, "end")
            entrada.insert(0, new_text)

        entrada.bind("<KeyRelease>", format_data)

    elif modo == "telefone":
        def format_tel(event=None):
            text = entrada.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return

            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue

                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            entrada.delete(0, "end")
            entrada.insert(0, new_text)

        entrada.bind("<KeyRelease>", format_tel)

    return entrada


def criar_servico(local, titulo, descricao, preco, horario_disponivel, linha, evento):
    servicoFrame = ctk.CTkFrame(local)

    labelServicoTitulo = ctk.CTkLabel(servicoFrame, text=titulo)
    labelServicoTitulo.grid(row=0, column=0)

    labelServicoDescricao = ctk.CTkLabel(servicoFrame, text=descricao)
    labelServicoDescricao.grid(row=1, column=0)

    labelServicoPreco = ctk.CTkLabel(servicoFrame, text=preco, padx=10)
    labelServicoPreco.grid(row=0, column=1)

    labelServicoHorario = ctk.CTkLabel(servicoFrame, text=horario_disponivel, padx=10)
    labelServicoHorario.grid(row=1, column=1)

    btnServicoAgender = ctk.CTkButton(servicoFrame, text="Agendar", command=evento)
    btnServicoAgender.grid(row=0, column=2)

    servicoFrame.grid(row=linha, column=0, pady=10)
