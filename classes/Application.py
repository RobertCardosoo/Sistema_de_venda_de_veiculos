from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar



class App:
    
    
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='#2A2A2A')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.minsize(width=600,height=600)
        
        
        
        
        
    def Iniciar(self):
        #Configurando a  tela da home e chamando a função frames
        
        self.root.title("System Car")
        self.frames_home()
        
        #Criando menu
        
        self.menu = Menu(self.root,bg='#3E3E3E')
        self.root.config(menu=self.menu)
        
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(label="Usuários",menu=self.fileMenu)
        self.fileMenu.add_command(label="Cadastro", command=self.Cadastro)
        
        self.root.mainloop()
        
    def Cadastro(self):
        #Configurando a tela de  cadastro e chamando a função frames
        self.root.title("Cadastro")
        self.frames_cadastro()
        self.widgets_frame1()
        self.root.mainloop()
        
        
        
    def frames_cadastro(self):
        self.frame_1 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_1.place(relx = 0.02 , rely = 0.02,relwidth = 0.96, relheight = 0.46)
        
        self.frame_2 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_2.place(relx = 0.02 , rely = 0.5,relwidth = 0.96, relheight = 0.46)
        
    def frames_home(self):
        
           
        self.frame_1 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_1.place(relx = 0.02 , rely = 0.02,relwidth = 0.6, relheight = 0.95)
        
        self.frame_2 = Frame(self.root,bd=4,bg='#3E3E3E',
                             highlightbackground='black',highlightthickness=2)
        self.frame_2.place(relx = 0.68 , rely = 0.02,relwidth = 0.3, relheight = 0.65)
        
        
    #Elementos do primeiro frame
        
    def widgets_frame1(self):
        #Criando botão limpar    
        self.btlimpar = Button(self.frame_1,text="Limpar")
        self.btlimpar.place(relx = 0.2,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Buscar  
        self.btlimpar = Button(self.frame_1,text="Buscar")
        self.btlimpar.place(relx = 0.31,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Novo
        self.btlimpar = Button(self.frame_1,text="Novo")
        self.btlimpar.place(relx = 0.62,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Alterar
        self.btlimpar = Button(self.frame_1,text="Alterar")
        self.btlimpar.place(relx = 0.73,rely=0.15,relwidth=0.1,relheight=0.1)
        #Criando botão Apagar
        self.btlimpar = Button(self.frame_1,text="Novo")
        self.btlimpar.place(relx = 0.84,rely=0.15,relwidth=0.1,relheight=0.1)
        
        #Criando label e input do codigo
        
        self.lb_codigo = Label(self.frame_1,text="Código:",bg='#3E3E3E',foreground='white')
        self.lb_codigo.place(relx=0.01, rely=0.05)
        
        self.codigo_input = Entry(self.frame_1)
        self.codigo_input.place(relx=0.01, rely=0.15,relwidth=0.08,relheight=0.09)
        
        #Criando label e input do Nome
        
        self.lb_nome = Label(self.frame_1,text="Nome:",bg='#3E3E3E',foreground='white')
        self.lb_nome.place(relx=0.01, rely=0.35)
        
        self.nome_input = Entry(self.frame_1)
        self.nome_input.place(relx=0.01, rely=0.45,relwidth=0.5,relheight=0.09)
        
        #Criando label e input do cpf
        
        self.lb_cpf = Label(self.frame_1,text="C.P.F:",bg='#3E3E3E',foreground='white')
        self.lb_cpf.place(relx=0.53, rely=0.35)
        
        self.cpf_input = Entry(self.frame_1)
        self.cpf_input.place(relx=0.53, rely=0.45,relwidth=0.2,relheight=0.09)
        
        #Criando input para sexo
        self.lb_sexo = Label(self.frame_1,text="Sexo:",bg='#3E3E3E',foreground='white')
        self.lb_sexo.place(relx=0.34, rely=0)
        
        self.sx = ["Masculino","Feminino"]
        self.cb = ttk.Combobox(self.frame_1,values=self.sx,state="readonly")
        self.cb.place(x=63,y=1,relwidth=0.6)
        self.cb.set("Masculino")
        self.cb.pack()
        
        #Criando datepicker
        
        def escolhedata():
            self.tela_escolhe_data = Tk()
            self.tela_escolhe_data.title("Escolha a data do seu nascimento")
            self.tela_escolhe_data.geometry("210x250")
            self.dt = Calendar(self.tela_escolhe_data,selectmode='day')
            self.btset_date = Button(self.tela_escolhe_data,text="Data de Nascimento")
            self.btset_date.place(rely=1,relx=5)
            self.dt.pack()
            
            
            
        self.date_picker = Button(self.frame_1,text="Data de Nascimento",command=escolhedata)
        self.date_picker.place(relx = 0.75,rely=0.45,relwidth=0.17,relheight=0.1)
        
        
        
        
        
        