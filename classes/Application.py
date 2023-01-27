from tkinter import *



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
        
        self.codigp_input = Entry(self.frame_1)
        self.codigp_input.place(relx=0.01, rely=0.15,relwidth=0.08,relheight=0.09)
        
        #Criando label e input do Nome
        
        self.lb_codigo = Label(self.frame_1,text="Nome:",bg='#3E3E3E',foreground='white')
        self.lb_codigo.place(relx=0.05, rely=0.35)
        
        self.codigp_input = Entry(self.frame_1)
        self.codigp_input.place(relx=0.05, rely=0.45,relwidth=0.7,relheight=0.09)
        
        
        