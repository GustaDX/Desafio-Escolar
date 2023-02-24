from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox

#Funções
def conecta():
    global conexao, Cursor
    conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='')
    print('conectado')
    Cursor = conexao.cursor()

def desconecta():
    conexao.close()

def verificacao():
    global emailx
    usuario = login.get()#mecher na v2.0 ----------------------------------------------------------------------------------------------------------
    password = senha.get()
    print('chegou')
    conecta()
    Cursor.execute('USE BANCO;')
    Cursor.execute(f"SELECT * FROM clientes_cadastrados WHERE Email = '{usuario}';")
    desconecta()
    print(Cursor)
    if Cursor.rowcount == 1:
        dados = Cursor.fetchone()
        print(dados)
        if dados[0] == usuario:
            if dados[4] == password:
                emailx = usuario
                home()
            else:
                messagebox.showinfo('Erro de usuario', \
                'Senha incorreta')

    else:
        messagebox.showinfo('Erro de usuario', \
        'Email não encontrado')

def home():
    global selecao, quantidade, texto_compra, texto_quantidade, R1, R2, quantidade, gerar, comprar
    texto_login.destroy()
    texto_senha.destroy()
    login.destroy()
    senha.destroy()
    logar.destroy()
    cadastro.destroy()
    imagem.destroy()
    selecao = IntVar()

    texto_compra = Label(text= 'Selecione o produto:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_compra.place(x=lado / 2.3, y = c1)
    texto_quantidade = Label(text= 'Quantos KG:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_quantidade.place(x=lado / 2.2, y = cima/ 5)
    R1 = Radiobutton(tela, text="Milho", fg= '#FFFF00', bg= '#363636', font= 'arial', variable=selecao, value=1)
    R1.place(x= lado / 2.13, y = cima / 8)

    R2 = Radiobutton(tela, text="Soja", fg= '#FFFF00', bg= '#363636', font= 'arial', variable=selecao, value=2)
    R2.place(x= lado / 2.13, y = cima / 6.5)

    quantidade = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    quantidade.place(x=lado / 2.37, y= cima / 4)

    gerar= Button(text='Gerar Valor', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= gerarv)
    gerar.place(x = lado / 2.3, y = cima/ 2.5)

    comprar= Button(text='Comprar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= compra)
    comprar.place(x = lado / 2.3, y = cima/ 2)

def cadastrar():
    global email, nome, telefone, localizacao, senhac, texto_email, texto_nome, texto_localizacao, texto_senhac, texto_telefone, cadastrado
    texto_login.destroy()
    texto_senha.destroy()
    login.destroy()
    senha.destroy()
    logar.destroy()
    cadastro.destroy()
    imagem.destroy()
    texto_nome = Label(text= 'Insira o seu nome:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_nome.place(x=lado / 2.3, y = c1)
    texto_email = Label(text= 'Insira o email', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_email.place(x=lado / 2.24, y = c2)
    texto_telefone = Label(text= 'Insira o telefone:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_telefone.place(x=lado / 2.27, y = cima / 3.29)
    texto_localizacao = Label(text= 'Insira seu endereço:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_localizacao.place(x=lado / 2.30, y = cima / 2.4)
    texto_senhac = Label(text= 'Insira sua senha:', fg= '#FFFF00', bg= '#363636', font= 'arial')
    texto_senhac.place(x=lado / 2.25, y = cima / 1.95)
    nome = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    nome.place(x=lado / 2.4, y= c3)
    email = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    email.place(x=lado / 2.4, y= c4)
    telefone = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    telefone.place(x=lado / 2.4, y= cima / 2.8)
    localizacao = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    localizacao.place(x=lado / 2.4, y= cima / 2.15)
    senhac = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
    senhac.place(x=lado / 2.4, y= cima / 1.75)
    cadastrado= Button(text='cadastrar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= verificacao_cadastro)
    cadastrado.place(x = lado / 2.26, y = cima / 1.5)

def verificacao_cadastro():
    emails = email.get()#mecher na v2.0 ----------------------------------------------------------------------------------------------------------
    nomes = nome.get()
    telefones = telefone.get()
    localizacaoz = localizacao.get()
    senhas = senhac.get()

    print('chegou')
    conecta()
    Cursor.execute('USE BANCO;')
    conexao.commit()
    Cursor.execute(f"SELECT * FROM clientes_cadastrados WHERE Email = '{emails}';")
    dados = Cursor.fetchone
    desconecta()
    if Cursor.rowcount == 0:
        try:
            conecta()
            Cursor.execute('USE BANCO;')
            conexao.commit()
            Cursor.execute(f'INSERT INTO clientes_cadastrados(Nome, Email, localizacao, senha, telefone) VALUES ("{nomes}", "{emails}", "{localizacaoz}", "{senhas}","{telefones}");')
            conexao.commit()
            desconecta()
            login2()
        except:
            messagebox.showinfo('Erro', \
            'Erro')
    else:
        messagebox.showinfo('Erro de Cadastro', \
        'email ja cadastrado')
    
def login2():
    global senha, login, logar, cadastro, texto_login, texto_senha, imagem 
    try:
        texto_nome.destroy()
        texto_email.destroy()
        texto_telefone.destroy()
        texto_localizacao.destroy()
        texto_senhac.destroy()
        nome.destroy()
        email.destroy()
        telefone.destroy()
        localizacao.destroy()
        senhac.destroy()
        cadastrado.destroy()
    finally:
        imagem = Label(tela, image = foto, border=0)
        imagem.place(x= 350, y= 0)
        texto_login = Label(text= 'Insira o email:', fg= '#FFFF00', bg= '#363636', font= 'arial')
        texto_login.place(x=l, y = c1)
        texto_senha = Label(text= 'Insira a senha:', fg= '#FFFF00', bg= '#363636', font= 'arial')
        texto_senha.place(x=l, y = c2)
        login = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
        login.place(x=l, y= c3)
        senha = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
        senha.place(x=l, y= c4)
        logar= Button(text='Logar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= verificacao)
        logar.place(x = l2, y = c5)
        cadastro= Button(text='cadastrar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= cadastrar)
        cadastro.place(x = l2, y = 350)

def gerarv():
    global texto_total
    k = selecao.get()
    kvalor = quantidade.get()
    if k == 1:
        kvalor = float(kvalor)
        total = kvalor * 1.5
        texto_total = Label(text= f'Total de R$:{total}', fg= '#FFFF00', bg= '#363636', font= 'arial')
        texto_total.place(x=lado / 2.2, y = cima/ 3)
    elif k == 2:
        kvalor = float(kvalor)
        total = kvalor * 2.7
        texto_total = Label(text= f'Total de R$:{total}', fg= '#FFFF00', bg= '#363636', font= 'arial')
        texto_total.place(x=lado / 2.2, y = cima/ 3)

    else:
        messagebox.showinfo('Erro de Compra', \
        'Não foi selecionado um produto')

def compra():
    k = selecao.get()
    kvalor = quantidade.get()
    if k == 1:
        kvalor = float(kvalor)
        total = kvalor * 1.5
        conecta()
        Cursor.execute('USE BANCO;')
        conexao.commit()
        Cursor.execute(f'INSERT INTO compras(Email, produto, Valor) VALUES ("{emailx}", "Milho", "{total}");')
        conexao.commit()
        desconecta()
        messagebox.showinfo('Nota de Retirada', \
        f'''
        Produto : Milho
        Quantidade: {kvalor}Kg
        Valor por Kg: R$: 1,50
        Valor total: R$:{total}

        Pagamento no local e Retirada no Local
        ''')
    elif k == 2:
        kvalor = float(kvalor)
        total = kvalor * 2.7
        conecta()
        Cursor.execute('USE BANCO;')
        conexao.commit()
        Cursor.execute(f'INSERT INTO compras(Email, produto, Valor) VALUES ("{emailx}", "Milho", "{total}");')
        conexao.commit()
        desconecta()
        messagebox.showinfo('Nota de Retirada', \
        f'''
        Produto : Soja
        Quantidade: {kvalor}Kg
        Valor por Kg: R$: 2,70
        Valor total: R$:{total}

        Pagamento no local e Retirada no Local
        ''')
    else:
        messagebox.showinfo('Erro de Compra', \
        'Realize a compra Novamete')

    R1.destroy()
    R2.destroy()
    quantidade.destroy() 
    texto_compra.destroy()
    texto_quantidade.destroy()
    quantidade.destroy()
    gerar.destroy()
    comprar.destroy()
    texto_total.destroy()
    login2()

#definicoes de tela

tela = Tk()
lado, cima = (tela.winfo_screenwidth()), (tela.winfo_screenheight())
tela.geometry('%dx%d+0+0' % (lado,cima))
tela.config(background='#363636', )
tela.title('Corns LTA')
image = Image.open("milhao.png")
ldivisao = lado/1.2
ldivisao = int(ldivisao)
resize_image = image.resize((ldivisao, cima))
foto = ImageTk.PhotoImage(resize_image)

#Posicionamento de botoes

imagem = Label(tela, image = foto, border=0)
imagem.place(x= 350, y= 0)
l =lado/25
l = int(l)
c1 = cima/12
c2 = cima/5
c3 = cima/7
c4 = cima/4
texto_login = Label(text= 'Insira o email:', fg= '#FFFF00', bg= '#363636', font= 'arial')
texto_login.place(x=l, y = c1)
texto_senha = Label(text= 'Insira a senha:', fg= '#FFFF00', bg= '#363636', font= 'arial')
texto_senha.place(x=l, y = c2)
login = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
login.place(x=l, y= c3)
senha = Entry(bg= '#FFFF00', border=0, fg= 'white', font='arial')
senha.place(x=l, y= c4)
l2 = lado/16
c5 = cima/3
c6 = cima / 2.5
logar= Button(text='Logar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= verificacao)
logar.place(x = l2, y = c5)
cadastro= Button(text='cadastrar', bg= '#363636', border=2, fg= '#FFFF00', activebackground='#363636', width= 20, height= 3, command= cadastrar)
cadastro.place(x = l2, y = 350)

#banco
conecta()
Cursor.execute('CREATE DATABASE IF NOT EXISTS BANCO;')
conexao.commit()
print('foi')
Cursor.execute('USE BANCO;')
conexao.commit()
Cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes_cadastrados(
    Email varchar(40) PRIMARY KEY,
    Nome varchar(30),
    telefone varchar(30),
    localizacao varchar(50),
    senha varchar(15));''')
conexao.commit()
Cursor.execute('''CREATE TABLE IF NOT EXISTS Compras(
    ID_Compra int PRIMARY KEY AUTO_INCREMENT,
    Email varchar(30),
    Valor varchar(50),
    produto varchar(15));''')
conexao.commit()
print('foi 2')
desconecta()

tela.mainloop()
