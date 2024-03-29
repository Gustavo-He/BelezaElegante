import customtkinter as Tk
from PIL import Image
from tkcalendar import *
primeiro = True


#---------------Janela---------------
def CriarJanela(Titulo,Tamanho,Tipo,Cor=0,Redimensionar=False):
    if Tipo == 1:
        Janela = Tk.CTk()
    elif Tipo==2:
        Janela = Tk.CTkToplevel()
    elif Tipo == 3:
        Janela = Tk.CTkInputDialog()
    Janela.title(Titulo)
    if Cor !=0:
     Janela.configure(fg_color=Cor)
    if Redimensionar==True:
     Janela.resizable(width=True, height=True)
    else:
     Janela.resizable(width=False, height=False)
    Colunas = list(range(13))
    Linhas = list(range(13))
    Janela.grid_columnconfigure(Colunas, weight=1)
    Janela.grid_rowconfigure(Linhas, weight=1)
    Janela.geometry(Tamanho)
    return Janela


#---------------Botão---------------
def CriarBotão(Local,Texto,Comando,Linha,Coluna,Largura,Altura,Cor=0,CorHover=0,Imagem="Nada"):
    if Imagem!="Nada":
        imagem_pillow = Image.open(Imagem)
        imageTk = Tk.CTkImage(imagem_pillow, size=[15, 15])
        botao = Tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura, image=imageTk)
        botao.grid(row=Linha, column=Coluna)
    else:
        botao = Tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura)
        botao.grid(row=Linha, column=Coluna)
    if Cor != 0:
            botao.configure(fg_color=Cor)
    if CorHover != 0:
            botao.configure(hover_color=CorHover)

    return botao


#---------------Caixa de Texto---------------
def CriarCaixaDeTexto(Local,Largura,Altura,Linha,Coluna,Texto=0,Modo="Padrão"):
    Caixa = Tk.CTkEntry(Local,width=Largura,height=Altura)
    Caixa.grid(row=Linha,column=Coluna)
    if Texto!=0:
     Caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        Caixa.configure(show="*")
        def SenhaMostra():
            global primeiro
            if primeiro:
                imagem_pillow = Image.open("Imagens/eye.ico")
                imageTk = Tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="")
                primeiro = False
            else:
                imagem_pillow = Image.open("Imagens/eye2.ico")
                imageTk = Tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="*")
                primeiro = True
        MostraSenha = CriarBotão(Caixa, "", SenhaMostra, 0, 0, 10, 10, Imagem="Imagens/eye2.ico")
        MostraSenha.grid(sticky="e", padx=2)
        MostraSenha.configure(fg_color=Caixa.cget("fg_color"), hover_color=Caixa.cget("fg_color"), corner_radius=0)
    elif Modo == "Hora":
        def format_hora(event=None):
            text = Caixa.get().replace(":", "")[:4]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 1:
                    new_text += text[index] + ":"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_hora)
    elif Modo == "Moeda":
        def format_moeda(event=None):
            text = Caixa.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_moeda)
    elif Modo == "CPF":
        def format_cpf(event=None):
            text = Caixa.get().replace(".", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):

                if not text[index] in "0123456789": continue
                if index in [2, 5]:
                    new_text += text[index] + "."
                elif index == 8:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_cpf)
    elif Modo == "CNPJ":
        def format_CNPJ(event=None):
            text = Caixa.get().replace(".", "").replace("/", "").replace("-", "")[:14]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 7:
                    new_text += text[index] + "/"
                elif index == 11:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_CNPJ)
    elif Modo == "Telefone":
        def format_tel(event=None):
            text = Caixa.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_tel)
    elif Modo == "Data":
        def format_data(event=None):
            text = Caixa.get().replace("/", "")[:8]
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
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_data)
    elif Modo == "CEP":
        def format_cep(event=None):
            text = Caixa.get().replace("-", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index == 5:
                    new_text += "-" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_cep)
    elif Modo == "Nome":
        def format_nome(event=None):
            text = Caixa.get()
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index].lower() in "abcdefghijklmnopqrstuvwxyz ":
                    continue
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_nome)
    return Caixa

# ---------------Label---------------


def CriarLabel(Local,Texto,Linha,Coluna,Cor="black", padx=1, pady=1):
    Label = Tk.CTkLabel(Local,text=Texto)
    Label.grid(row=Linha,column=Coluna)
    if Cor!="black":
        Label.configure(text_color=Cor)
    Label.configure(padx=padx, pady=pady)
    return Label


# ---------------CheckBox---------------
def CriarCheckBox(Local,Texto,Linha,Coluna,Comando=0):
    check = Tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha,column=Coluna)
    if Comando!=0:
        check.configure(command=Comando)
    return check


def CriarCheckBox2(Local,Texto,Linha,Coluna,Comando=0):
    check = Tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha, column = Coluna)
    if Comando!=0:
        check.configure(command=Comando)
    return check


# ---------------ComboBox---------------
def CriarComboBox(Local,Largura,Altura,Valores,Linha,Coluna,Comando=0):
    combo= Tk.CTkComboBox(Local, width=Largura, height=Altura,
                          values=Valores, state="readonly")
    combo.grid(row=Linha, column=Coluna)
    combo.set("Selecione")
    if Comando!=0:
        combo.configure(command=Comando)
    return combo


# ---------------ProgressBar---------------
def CriarProgressBar(Local,Largura,Altura,Linha,Coluna):
    progress =Tk.CTkProgressBar(Local,width=Largura,height=Altura)
    progress.grid(row=Linha,column=Coluna)
    progress.set(0)
    return progress


# ---------------Switch---------------
def CriarSwitch(Local,Texto,Linha,Coluna,Comando=0):
    switch = Tk.CTkSwitch(Local,text=Texto)
    switch.grid(row=Linha,column=Coluna)
    if Comando!=0:
     switch.configure(command=Comando)
    return switch


# ---------------Slider---------------
def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider=Tk.CTkSlider(Local,width=Largura,height=Altura)
    slider.grid(row=Linha,column=Coluna)
    slider.set(0)
    return slider


# ---------------Caixa de Texto (rolagem)---------------
def CriarTexto(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
    caixatxt= Tk.CTkTextbox(Local,wrap="word")
    caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
    caixatxt.insert("0.0",Texto,)
    if Largura!=0:
        caixatxt.configure(width=Largura)
    if Altura!=0:
        caixatxt.configure(height=Altura)

    return caixatxt


# ---------------Imagem---------------
def CriarImagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = Tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = Tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem


def CriarData(Local,Linha,Coluna):
    pass


def CriarAbas(Local,Linha,Coluna,Largura,Altura,*Abas):
    aba = Tk.CTkTabview(Local,width=Largura, height=Altura)
    for C in Abas:
        aba.add(C)
        Tamanho = list(range(13))
        aba.tab(C).grid_rowconfigure(Tamanho,weight=1)
        aba.tab(C).grid_columnconfigure(Tamanho, weight=1)
    aba.grid(row=Linha, column=Coluna)
    return aba


def CriarFrame(Local,Linha,Coluna,Largura,Altura):
    frame = Tk.CTkFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_propagate(False)
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame


def CriarFundo(Local,Largura,Altura,Caminho):
    imagem_pillow = Image.open(Caminho)
    imageTk = Tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = Tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.place(x=0,y=0)
    return imagem


def criar_servico(local, titulo, descricao, preco, horario_disponivel, linha, evento):
    servicoFrame = CriarFrame(local, linha, 0, 450, 100)

    CriarLabel(servicoFrame, titulo, 0, 0)
    # labelServicoTitulo = Tk.CTkLabel(servicoFrame, text=titulo)
    # labelServicoTitulo.grid(row=0, column=0)

    CriarLabel(servicoFrame, descricao, 1, 0)
    # labelServicoDescricao = Tk.CTkLabel(servicoFrame, text=descricao)
    # labelServicoDescricao.grid(row=1, column=0)

    CriarLabel(servicoFrame, preco, 0, 1)
    # labelServicoPreco = Tk.CTkLabel(servicoFrame, text=preco, padx=10)
    # labelServicoPreco.grid(row=0, column=1)

    CriarLabel(servicoFrame, horario_disponivel, 1, 1)
    # labelServicoHorario = Tk.CTkLabel(servicoFrame, text=horario_disponivel, padx=10)
    # labelServicoHorario.grid(row=1, column=1)

    CriarBotão(servicoFrame, "Agendar", evento, 0, 2, 90, 20)
    # btnServicoAgender = Tk.CTkButton(servicoFrame, text="Agendar", command=evento)
    # btnServicoAgender.grid(row=0, column=2)


def checar_data(data):
    if len(data) == 10:
        dia, mes, ano = data.split("/")

        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and int(ano) >= 1:
            return True

    return False


def checar_hora(hora, agendamentos):
    if len(hora) == 5:
        hora, minuto = hora.split(":", 1)
        if 0 <= int(hora) < 24 and 0 <= int(minuto) < 60:
            for servico in agendamentos:
                print(servico)
                if "Corte de cabelo" == servico:
                    if not 16 <= int(hora) <= 19:
                        return False

                elif "Manicure" == servico:
                    if not 8 <= int(hora) <= 18:
                        return False

                elif "Maquiagem" == servico:
                    if not 9 <= int(hora) <= 12:
                        return False

                elif "Pedicure" == servico:
                    if not 5 <= int(hora) <= 14:
                        return False

                else:
                    return False

            return True

    return False


def checar_email(email):
    if email.find("@") != -1 and email.find(".") != -1:
        return True

    return False
