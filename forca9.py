
"""
" algumas palvras,principalmente de CEP podem estar com maisculas no inicio. ex: Campos do Jordao, Inglaterra,
Created on Wed Mar 25 15:50:10 2015

@author: marcos
"""
import random
a = arquivo = open("entrada.txt", encoding = "UTF-8")

lista=arquivo.readlines()
listalimpa=[]
for i in range(len(lista)-1):
    listalimpa.append(lista[i].strip())
print(listalimpa)
x= random.choice(listalimpa)
from unicodedata import normalize
def formatar(txt):
    return normalize("NFKD",txt).encode("ASCII","ignore").decode("ASCII")
if __name__=="__main__":
        from doctest import testmod
        testmod()
y= formatar(x)    
print(x)


    
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Poligonos")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(50,0)
tartaruga.pendown()
tartaruga.color("white")

tartaruga2  = turtle.Turtle()
tartaruga2.speed(5)  # define a velocidade
tartaruga2.penup()       # Remova e veja o que acontece
tartaruga2.setpos(0,0)
tartaruga2.pendown()
tartaruga2.color("green")
#window.textinput("caixa de texto", 'digite a letra')


def boneco(erros):
    if erros == 1:
        head()
    if erros == 2:
        body()
    if erros == 3:
        arm1()
    if erros == 4:
        arm2()
    if erros == 5:
        leg1()
    if erros == 6:
        leg2()
    

for i in range(1):
    
    tartaruga.forward(100)
    tartaruga.backward(50)
    tartaruga.left(90)
    tartaruga.forward(300)
    tartaruga.right(90)
    tartaruga.forward(100)
    tartaruga.backward(25)
    tartaruga.right(90)
    tartaruga.forward(50)
def head():
    tartaruga.penup()
    tartaruga.setpos(150,225)
    tartaruga.pendown()
    tartaruga.circle(25)
    tartaruga.penup()
    tartaruga.setpos(175,200)
def body():
    tartaruga.pendown()
    tartaruga.forward(100)
    tartaruga.backward(60)
def arm1():
    tartaruga.left(45)
    tartaruga.forward(50)
    tartaruga.backward(50)
def arm2():    
    tartaruga.left(275)
    tartaruga.forward(50)
    tartaruga.backward(50)
def leg1():
    tartaruga.left(40)
    tartaruga.forward(60)
    tartaruga.left(45)
    tartaruga.forward(75)
    tartaruga.backward(75)
def leg2():  
    tartaruga.left(275)
    tartaruga.forward(75)
    tartaruga.backward(75)
    tartaruga.penup()
    tartaruga.setpos
    
guess=0
while guess==0:
    pergunta1 = str(window.textinput("caixa de texto", 'digite a letra'))
    if pergunta1 in x:
        tartaruga2.penup()
        tartaruga2.setpos(-150,-25)
        tartaruga2.pendown()
        tartaruga2.write(pergunta1,move=True,align="left",font=("Arial",20,"normal"))
    else:
        head()
        guess+=1
        
while guess==1:
    pergunta2 = str(window.textinput("caixa de texto", 'digite a letra'))
    if pergunta2 in x:
        tartaruga2.penup()
        tartaruga2.setpos(-120,-25)
        tartaruga2.pendown()
        tartaruga2.write(pergunta2,move=True,align="left",font=("Arial",20,"normal")) 
    else:
        body()
        guess+=1        
while guess==2: 
     pergunta3 = str(window.textinput("caixa de texto", 'digite a letra'))
     if pergunta3 in x:
         tartaruga2.penup()
         tartaruga2.setpos(-90,-25)
         tartaruga2.pendown()
         tartaruga2.write(pergunta3,move=True,align="left",font=("Arial",20,"normal"))
     else:
        arm1()
        guess+=1
      
while guess==3:
    pergunta4 = str(window.textinput("caixa de texto", 'digite a letra'))
    if pergunta4 in x:
        tartaruga2.penup()
        tartaruga2.setpos(-60,-25)
        tartaruga2.pendown()
        tartaruga2.write(pergunta4,move=True,align="left",font=("Arial",20,"normal"))
    else:
        arm2()
        guess+=1
       
while guess==4:
    pergunta5 = str(window.textinput("caixa de texto", 'digite a letra'))
    if pergunta5 in x:
        tartaruga2.penup()
        tartaruga2.setpos(-30,-25)
        tartaruga2.pendown()
        tartaruga2.write(pergunta5,move=True,align="left",font=("Arial",20,"normal"))
    else:
        leg1()
        guess+=1
       
while guess==5:
    pergunta6 = str(window.textinput("caixa de texto", 'digite a letra'))
    if pergunta6 in x:
        tartaruga2.penup()
        tartaruga2.setpos(0,-25)
        tartaruga2.pendown()
        tartaruga2.write(pergunta6,move=True,align="left",font=("Arial",20,"normal"))
    else:
        leg2()
        guess+=1
     
window.exitonclick()
        
        
        
            
        
        
        
    