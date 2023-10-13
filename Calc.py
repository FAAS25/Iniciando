from tkinter import *
from tkinter import ttk

#CORES
cor1 = "#ffffff" #branco
cor2 = "#363333" #cinza-escuro
cor3 = "#294066" #azul-escuro
cor4 = "#7a9acf" #azul-claro
cor5 = "#0a0a0a" #PRETO
cor6 = "#f2eded" #cinza-claro

janela = Tk()
janela.title("Calc")
janela.geometry("236x260")
janela.config(background=cor1)

#CRIANDO FRAMES
frame_tela = Frame(janela, width=235,height=40, bg=cor5)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela, width=235,height=268, bg=cor2)
frame_corpo.grid(row=1,column=0)

#variavel todos os valores 
todos_valores = ""

#CRIANDO LABEL
valor_texto = StringVar()

#criando função
def entrar_valores(event):

  global todos_valores
  todos_valores = todos_valores + str(event)
  
  #passando valor para tela
  valor_texto.set(todos_valores)

# função pp/ calcular
def calcular():
  global todos_valores
  resultado = eval(todos_valores)
  valor_texto.set(str(resultado))

# função p/ limpar tela
def limpar_tela():
  global todos_valores
  todos_valores = ""
  valor_texto.set("")


label_tela = Label(frame_tela, textvariable=valor_texto, width=19, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 14"), bg=cor3, fg=cor1)
label_tela.place(x=0, y=0)

#CRIANDO BOTÔES
b_1 = Button(frame_corpo, command = limpar_tela, text="C",width=11,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=1, y=0)

b_2 = Button(frame_corpo,  command = lambda: entrar_valores("%"), text="%",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=117, y=0)

b_3 = Button(frame_corpo,  command = lambda: entrar_valores("/"), text="/",width=4,height=2, bg=cor4, fg=cor1,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo,  command = lambda: entrar_valores("7"), text="7",width=4,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=1, y=44)

b_5 = Button(frame_corpo,  command = lambda: entrar_valores("8"), text="8",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=44)

b_6 = Button(frame_corpo,  command = lambda: entrar_valores("9"), text="9",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=117, y=44)

b_7 = Button(frame_corpo,  command = lambda: entrar_valores("*"), text="*",width=4,height=2, bg=cor4, fg=cor1, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=44)

b_8 = Button(frame_corpo, command = lambda: entrar_valores("4"),  text="4",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=1, y=88)

b_3 = Button(frame_corpo,  command = lambda: entrar_valores("5"), text="5",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=59, y=88)

b_1 = Button(frame_corpo,  command = lambda: entrar_valores("6"), text="6",width=4,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=117, y=88)

b_2 = Button(frame_corpo,  command = lambda: entrar_valores("-"), text="-",width=4,height=2, bg=cor4, fg=cor1, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=177, y=88)

b_3 = Button(frame_corpo,  command = lambda: entrar_valores("1"), text="1",width=4,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=1, y=132)

b_1 = Button(frame_corpo,  command = lambda: entrar_valores("2"), text="2",width=4,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=59, y=132)

b_2 = Button(frame_corpo,  command = lambda: entrar_valores("3"), text="3",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=117, y=132)

b_3 = Button(frame_corpo,  command = lambda: entrar_valores("+"), text="+",width=4,height=2, bg=cor4, fg=cor1,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=132)

b_1 = Button(frame_corpo,  command = lambda: entrar_valores("0"), text="0",width=11,height=2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=1, y=176)

b_2 = Button(frame_corpo,  command = lambda: entrar_valores("."), text=".",width=4,height=2,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=117, y=176)

b_3 = Button(frame_corpo, command = calcular, text="=",width=4,height=2, bg=cor4, fg=cor1,  font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=176)


janela.mainloop()



