# bibliotecas e ferramentas necessárias para serem utilizadas no projeto.
from tkinter import *
import tkinter.messagebox as tsmg

# Criando a janela de login
root=Tk()

# Função para checar os dados.
def check():
    nome=usuario.get()                                                                                  #requisitando o nome do usuário
    senha=password.get()                                                                                #requisitando a senha do usuário
    confirmacao_senha=confirmacao_password.get()                                                        #requisitando a confirmação da senha do usuário
    mix=nome+"-"+senha+"-"+confirmacao_senha                                                            #mixando os dados
    # os dados de login ficarão armazenados no arquivo dados.txt pois nesse projeto não utilizei banco de dados SQL.
    #
    try:                                                                                                #tentando abrir o arquivo
        with open("dados.txt","r") as ler:
            ler=ler.readlines()
    except FileNotFoundError:                                                                           #se o arquivo não existir, cria o arquivo.
        arquivo = open('dados.txt', 'w+')
        arquivo.writelines(u'\n')
    if senha==confirmacao_senha:                                                                        #verificando se as senhas são iguais
        if str(mix) in str(ler):
            tsmg.showinfo("Bem Vindo(a)!",f"Olá {nome}, Você está Logado!")                             #mostrando uma mensagem de sucesso
        if str(nome) in str(ler) and str(senha) not in str(ler):
            tsmg.showerror("Erro!","Usuário encontrado, mas a senha está incorreta.")                   #mostrando uma mensagem de erro
        else:
            tsmg.showerror("Erro!","Usuário não encontrado, Faça o cadastro!")                          #mostrando uma mensagem de erro
    else:
        tsmg.showerror("Erro!","A senha e a confirmação de senha estão diferentes.")                    #mostrando uma mensagem de erro
    if nome in str(ler):                                                                                #verificando se o nome já existe
        tsmg.showerror("Erro!","Esse nome já está em uso. Faça login ou Registre-se")                   #mostrando uma mensagem de erro
    usuario.set("")
    password.set("")
    confirmacao_password.set("")

# Função para salvar os dados
def save():
    nome=usuario.get()                                                              #requisitando o nome do usuário
    senha=password.get()                                                            #requisitando a senha do usuário
    confirmacao_senha=confirmacao_password.get()                                    #requisitando a confirmação da senha do usuário
    mix=nome+"-"+senha+"-"+confirmacao_senha                                        #mixando os dados
    if nome!="" and senha!="" and confirmacao_senha!="" :                           #verificando se os campos estão preenchidos
        with open("dados.txt","r") as ler:                                          #abrindo o arquivo
            ler=ler.readlines()                                                     #lendo o arquivo dados.txt
        if str(mix) in str(ler):                                                    #verificando se o usuário já existe
            tsmg.showerror("Erro!","Usuário existente, faça login!")                #se o usuário já existe, mostra um erro
            usuario.set("")                                                         #limpando os campos
            password.set("")                                                        #limpando os campos
            confirmacao_password.set("")                                            #limpando os campos
        elif str(nome) in str(ler):                                                 #verificando se o nome já existe
            tsmg.showerror("Erro","Esse usuário já existe, crie outro nome.")       #se o nome já existe, mostra um erro
            usuario.set("")                                                         #limpando os campos
            password.set("")                                                        #limpando os campos                             
            confirmacao_password.set("")                                            #limpando os campos
        else:
            if senha==confirmacao_senha:                                            #verificando se as senhas são iguais
                with open("dados.txt","a") as ler:                                  #abrindo o arquivo                  
                    ler.write(f"{nome}-{senha}-{confirmacao_senha}\n")              #escrevendo no arquivo
                tsmg.showinfo("Sucesso!","Sua conta foi criada!")                   #mostrando uma mensagem de sucesso  
                usuario.set("")                                                     #limpando os campos
                password.set("")                                                    #limpando os campos
                confirmacao_password.set("")                                        #limpando os campos
            else:
                tsmg.showerror("Erro!","Uma das senhas está diferente")             #se as senhas não forem iguais, mostra um erro
                usuario.set("")                                                     #limpando os campos
                password.set("")                                                    #limpando os campos
                confirmacao_password.set("")                                        #limpando os campos

# Criando os campos de texto e onde serão inseridos os dados.

usuario=StringVar()                                                                 #criando uma variável para armazenar o nome do usuário
password=StringVar()                                                                #criando uma variável para armazenar a senha do usuário
confirmacao_password=StringVar()                                                    #criando uma variável para armazenar a confirmação da senha do usuário

############## Settings da Janela de login ##############
# Tamanho da janela
root.geometry("800x600")
# Titulo da janela
root.title("Página de Login para Estudos")

# Cor de fundo da janela
f=Frame(root)                                                                     
Label(f,text="Faça login para continuar",font="SegoeUI 18 bold",pady=10).pack()         
f.pack()

# Criando os campos de texto
f=Frame(root)
Label(f,text="Login",font="SegoeUI 14 bold",pady=5).pack()                                                  #criando um campo para o nome do usuário
campo_usuario=Entry(f,textvariable=usuario,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
Label(f,text="Senha",font="SegoeUI 14 bold",pady=5).pack()                                                  #criando um campo para a senha do usuário                           
campo_senha=Entry(f,textvariable=password,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
campo_confirma_senha=Label(f,text="Repita a senha",font="SegoeUI 14 bold",pady=5).pack()         #criando um campo para a confirmação da senha do usuário
e3=Entry(f,textvariable=confirmacao_password,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
f.pack()

# Criando os botões
f=Frame(root)
b1=Button(f,text="Logar",font="SegoeUI 10 bold",command=check).pack(side=LEFT,pady=11,padx=11)                      #criando um botão para logar
b2=Button(f,text="Registrar",font="SegoeUI 10 bold",command=save).pack(side=LEFT,pady=11,padx=11)                   #criando um botão para registrar
f.pack()

# Rodapé
f=Frame(root)
Label(f,text="Você não tem uma conta, precisa se registrar para efetuar login",font="SegoeUI 14 bold",pady=5).pack()    #criando um campo para registrar
f.pack()

# Mantendo a janela aberta.
root.mainloop()