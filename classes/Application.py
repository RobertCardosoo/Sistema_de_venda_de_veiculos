from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes.Consultor import Consultor
from classes.Fipe_Dados import Fipe
import mysql.connector


class Funcs():
#Funções de Banco de Dados
    #busca de usuários para login
    def checkUser(self):
        self.conecta_bd()
        loginCPF = self.login_input.get()
        loginPass = self.senha_login_input.get()
        self.cursor.execute(f'SELECT id,nome,cpf,senha_consultor from consultores where cpf="{loginCPF}" and senha_consultor="{loginPass}";')
        res = self.cursor.fetchall()
        self.desconectar
        
        return res
        
    def monta_tabela(self):
        self.conecta_bd
        self.cursor.execute('CREATE TABLE IF NOT EXISTS consultores(id int primary key auto_increment,nome varchar(60) not null,cpf char(14) not null, data_nascimento date, genero varchar(10) not null, senha_consultor varchar(10) not null);')
        self.conn.commit()
        self.desconectar
        
    def checkCPF(self,cpf):
        
            self.conecta_bd()
            cpfc = cpf
            self.cursor.execute(f'select cpf from consultores where cpf="{cpfc}"')
            res = self.cursor.fetchall()
            self.desconectar()
            return len(res)
        
    def limpa_tela(self):
        
        self.codigo_input.delete(0,END)
        self.nome_input.delete(0,END)
        self.cpf_input.delete(0,END)
        self.senha_input.delete(0,END)
    
    def conecta_bd(self):
        
        self.conn = mysql.connector.connect(host="localhost",user="root",password="root",database="sys_v_veiculos")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados")
        self.monta_tabela()  
        
    def desconectar(self):
        
        self.conn.close(); print("Desconectando ao Banco de Dados")    
    
    def variaveis(self):
        self.codigoc = self.codigo_input.get()
        self.nomec = self.nome_input.get()
        self.cpfc = self.cpf_input.get()
        self.gen = self.cb.get()
        self.password = self.senha_input.get()    
    
    def criar_usuario(self):
        self.variaveis()
        
        check = self.checkCPF(self.cpfc)
        
        if(self.nomec == "" or self.cpfc =="" or self.gen=="" or self.password==""):
            
            messagebox.showwarning(title="Opa!", message="Não é possível criar usuário com campos vazios")
            
        elif(check > 0 ):
            
            messagebox.showwarning(title="Opa!", message="CPF já cadastrado")
            
        elif(check == 0 and self.cpfc!=""):
            
            self.conecta_bd()
            
            self.cursor.execute(f'INSERT INTO consultores (nome,cpf,genero,senha_consultor) VALUES ("{self.nomec}","{self.cpfc}","{self.gen}","{self.password}")')
            self.conn.commit()
            self.desconectar()
            self.limpa_tela()
            messagebox.showinfo(title="Novo Consultor na área!", message="Consultor Criado com Sucesso!")    
            self.select_lista()
            
    def select_lista(self):
        self.lista_usu.delete(*self.lista_usu.get_children())
        self.conecta_bd()
        self.cursor.execute('SELECT id,nome,cpf,data_nascimento,genero FROM consultores ORDER BY id ASC;')
        lista = self.cursor.fetchall()
        for i in lista:
            self.lista_usu.insert("","end",values=i)
        self.desconectar()
    
    #formatação e validação de CPF 
    
    def format_cpf(self,event = None):
    
        text = self.cpf_input.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]

        self.cpf_input.delete(0, "end")
        self.cpf_input.insert(0, new_text)
        
    def format_cpf_login(self,event = None):
    
        text = self.login_input.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]

        self.login_input.delete(0, "end")
        self.login_input.insert(0, new_text)
        
    def onDoubleClick(self, event = True):
        self.limpa_tela()
        self.lista_usu.selection()
        
        for i in self.lista_usu.selection():
            col1,col2,col3,col4,col5 = self.lista_usu.item(i,'values')
            self.codigo_input.insert(END,col1)
            self.nome_input.insert(END,col2)
            self.cpf_input.insert(END,col3)
            self.cb.set(col5)
            
    def deleta_usu(self):
        self.variaveis()
        
        self.conecta_bd()
        
        self.cursor.execute(f'DELETE FROM consultores where id = {self.codigoc}')
        self.conn.commit()
        
        self.desconectar()
        self.limpa_tela()
        self.select_lista()
    
    def altera_usu(self):
        self.variaveis()
        if(self.nomec == "" or self.gen == "" or self.cpfc == ""):
            messagebox.showwarning(title="Não foi possível alterar os dados atuais",message="Você está tentando inserir dados nulos")   
            
        elif(self.nomec != "" and self.cpfc != ""):
            self.conecta_bd()
            self.cursor.execute(f'UPDATE consultores set nome = "{self.nomec}", cpf = "{self.cpfc}", genero = "{self.gen}" WHERE id = {self.codigoc} ;')
            self.conn.commit()
            self.desconectar()
            self.select_lista()
class App(Funcs):
    
    
    
        
    #tela de inicial de login    
    def Login(self):
        self.tela_login = Tk()
        self.tela_login.title("Login")
        self.tela_login.configure(background='#2A2A2A')
        self.tela_login.geometry("700x300")
        self.tela_login.minsize(width=700,height=300)
        self.tela_login.maxsize(width=700,height=300)
        self.frames_login()
        self.widgets_frame_login()
        self.tela_login.mainloop()
    
    #Função de verificação de login   
    def fazerlogin(self):
        #Recebendo lista com a busca de usuário
        resp = self.checkUser()
        conf = len(resp)
        #Recebendo os valores dos inputs
        login = self.login_input.get()
        senha = self.senha_login_input.get()
        
        #Mensagem de erro se os valores dos inputs de login forem nulos
        if(login == "" or senha == ""):
            messagebox.showwarning(title="Opa!", message="Por favor preencher os campos necessários!")
        elif(conf != 0):
        #Entrando no sistema se os dados de login forem inseridos corretamente   
            self.tela_login.destroy()
            self.currentuser = Consultor(resp[0][1],NONE,resp[0][2],NONE,resp[0][0]) 
            self.Iniciar()
        #Se não for encontrado usuário
        elif(conf == 0):
             messagebox.showwarning(title="Opa!", message="Usuário não encontrado")
             
            
    #Tela Home             
    def Iniciar(self):
        
        self.root = Tk()
        self.root.configure(background='#2A2A2A')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.minsize(width=600,height=600)
        self.root.title("System Car")
        self.frames_home()
        
        
        #Menu da Home
        self.menu = Menu(self.root,bg='#3E3E3E')
        self.root.config(menu=self.menu)
        
        self.fileMenu = Menu(self.menu)
        self.menu.add_command(label="Home", command=self.home)
        self.menu.add_cascade(label="Cadastro",menu=self.fileMenu)
        self.fileMenu.add_command(label="Usuários", command=self.Cadastro)
        self.widgets_frame1_home()
        
        
        self.root.mainloop()
        
    def Cadastro(self):
        #Tela de Cadastro de Consultores
        self.root.title("Cadastro")
        self.fechar_home()
        self.frames_cadastro()
        self.widgets_frame1_cadastro()
        self.widgets_frame2_cadastro()
        self.select_lista()
        self.root.mainloop()
        
        
    #Frames da Tela de Cadastro    
    def frames_cadastro(self):
        self.frame_11= Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_11.place(relx = 0.02 , rely = 0.02,relwidth = 0.96, relheight = 0.46)
        
        self.frame_22 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_22.place(relx = 0.02 , rely = 0.5,relwidth = 0.96, relheight = 0.46)
    #Frames da tela de login    
    def frames_login(self):
        self.frame_l = Frame(self.tela_login,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_l.place(relx = 0.39 , rely = 0.02,relwidth = 0.6, relheight = 0.95)
        
    #Frames da tela home
    def frames_home(self):
        
        self.frame_1 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_1.place(relx = 0.02 , rely = 0.02,relwidth = 0.6, relheight = 0.95)
        
        self.frame_2 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_2.place(relx = 0.68 , rely = 0.02,relwidth = 0.3, relheight = 0.65)
        
        
    #Função que fecha os frames da home    
    def fechar_home(self):
        self.frame_1.destroy()
        self.frame_2.destroy()
    #Função que fecha a tela de Cadastro
    def fechar_cadastro(self):
        self.frame_11.destroy()
        self.frame_22.destroy()
    def home(self):
        self.fechar_cadastro()
        self.frames_home()
        self.widgets_frame1_home()
        
        
    #Elementos do primeiro frame Cadastro
        
    def widgets_frame1_cadastro(self):
        #Criando botão limpar    
        self.btlimpar = Button(self.frame_11,text="Limpar",command=self.limpa_tela)
        self.btlimpar.place(relx = 0.2,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Buscar  
        self.btbuscar = Button(self.frame_11,text="Buscar")
        self.btbuscar.place(relx = 0.31,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Novo
        self.btnovo = Button(self.frame_11,text="Novo",command=self.criar_usuario)
        self.btnovo.place(relx = 0.62,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Alterar
        self.btalterar = Button(self.frame_11,text="Alterar",command=self.altera_usu)
        self.btalterar.place(relx = 0.73,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Apagar
        self.btexcluir = Button(self.frame_11,text="Excluir",command=self.deleta_usu)
        self.btexcluir.place(relx = 0.84,rely=0.15,relwidth=0.1,relheight=0.1)
        
        #Criando label e input do codigo
        
        self.lb_codigo = Label(self.frame_11,text="Código:",bg='#3E3E3E',foreground='white')
        self.lb_codigo.place(relx=0.01, rely=0.05)
        
        self.codigo_input = Entry(self.frame_11)
        self.codigo_input.place(relx=0.01, rely=0.15,relwidth=0.08,relheight=0.09)
        
        #Criando label e input do Nome
        
        self.lb_nome = Label(self.frame_11,text="Nome:",bg='#3E3E3E',foreground='white')
        self.lb_nome.place(relx=0.01, rely=0.35)
        
        self.nome_input = Entry(self.frame_11)
        self.nome_input.place(relx=0.01, rely=0.45,relwidth=0.5,relheight=0.09)
        
        #Criando label e input do cpf
        
        self.lb_cpf = Label(self.frame_11,text="C.P.F:",bg='#3E3E3E',foreground='white')
        self.lb_cpf.place(relx=0.53, rely=0.35)
        
        self.cpf_input = Entry(self.frame_11)
        self.cpf_input.place(relx=0.53, rely=0.45,relwidth=0.2,relheight=0.09)
        self.cpf_input.bind("<KeyRelease>",self.format_cpf)
        
        #Criando input para sexo
        self.lb_sexo = Label(self.frame_11,text="Sexo:",bg='#3E3E3E',foreground='white')
        self.lb_sexo.place(relx=0.34, rely=0)
        
        self.sx = ["Masculino","Feminino","Outro"]
        self.cb = ttk.Combobox(self.frame_11,values=self.sx,state="readonly")
        self.cb.place(x=63,y=1,relwidth=0.6)
        self.cb.set("Masculino")
        self.cb.pack()
        
        #Criando input para senha
        self.lb_senha = Label(self.frame_11,text="Senha:",bg='#3E3E3E',foreground='white')
        self.lb_senha.place(relx=0.01, rely=0.56)
        self.senha_input = Entry(self.frame_11,show="*")
        self.senha_input.place(relx=0.01, rely=0.65,relwidth=0.3,relheight=0.09)
    
        
    
    def widgets_frame2_cadastro(self):
        #Criando Lista de Usuários
        self.lista_usu = ttk.Treeview(self.frame_22, height = 3,columns=('col1','col2','col3','col4','col5'))

        self.lista_usu.heading("#1",text="Código")
        self.lista_usu.heading("#2",text="Nome")
        self.lista_usu.heading("#3",text="CPF")
        self.lista_usu.heading("#4",text="Idade")
        self.lista_usu.heading("#5",text="Gênero")
        
        self.lista_usu.column("#0",width=0)
        self.lista_usu.column("#1",width=50)
        self.lista_usu.column("#2",width=200)
        self.lista_usu.column("#3",width=125)
        self.lista_usu.column("#4",width=125)
        self.lista_usu.column("#5",width=125)
        
        self.lista_usu.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.99)
        self.scroll_Lista = Scrollbar(self.frame_22, orient='vertical')
        self.lista_usu.configure(yscroll=self.scroll_Lista.set)
        self.scroll_Lista.place(relx=0.96,rely=0.01,relwidth=0.02, relheight=0.99)
        
        self.lista_usu.bind("<Double-1>",self.onDoubleClick)
        
        
    def widgets_frame1_home(self):
        
        self.tabela = Listbox(self.frame_1)    
        self.tabela.configure(width=1024,height=768)
        self.tabela.config(background="#3E3E3E",border=0,foreground="white")
        self.tabela.insert(1,"Python1")
        self.tabela.pack()
        
        self.info_nome_usuario = Label(self.frame_2,foreground='white',text=f"Usuário:{self.currentuser.getNome()}",bg="#3E3E3E",font=("Arial",12))
        self.info_nome_usuario.place(relx=0.05, rely=0.05)
        self.info_mat_usuario = Label(self.frame_2,foreground='white',text=f"Matrícula:{self.currentuser.getMat()}",bg="#3E3E3E",font=("Arial",12))
        self.info_mat_usuario.place(relx=0.05, rely=0.1)
    
    def widgets_frame_login(self):
        #Inputs de Login e Senha
        self.login_input = Entry(self.frame_l)
        self.login_input.place(relx=0.3, rely=0.20,relwidth=0.5,relheight=0.09)
        self.login_input.bind("<KeyRelease>",self.format_cpf_login)
        self.senha_login_input = Entry(self.frame_l)
        self.senha_login_input.config(show="*")
        self.senha_login_input.place(relx=0.3, rely=0.35,relwidth=0.5,relheight=0.09)
        
        #Labels de Login e Senha
        self.lb_login = Label(self.frame_l,text="Login:",bg='#3E3E3E',foreground='white')
        self.lb_login.place(relx = 0.15 ,rely = 0.20)
        self.lb_senha = Label(self.frame_l,text="Senha:",bg='#3E3E3E',foreground='white')
        self.lb_senha.place(relx = 0.15 ,rely = 0.35)
        
        #Botão para login
        
        self.bt_login = Button(self.frame_l,text="Entrar",command=self.fazerlogin)
        self.bt_login.place(relx=0.40,rely=0.60,relwidth=0.25,relheight=0.08)
        
        #Nome do Sistema
        
        self.name_sytstem = Label(self.tela_login,text="System Car",bg='#2A2A2A',foreground='white',font=("Arial",25))
        self.name_sytstem.place(relx=0.05,rely=0.35)
        
        
        
        