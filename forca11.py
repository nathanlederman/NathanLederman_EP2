
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

acertos=0        
erros=0    
z= len(y)
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
    
while z != len(y):    
    tartaruga2.penup()
    tartaruga2.setpos(-150+20*z,-35)
    tartaruga2.pendown()
    tartaruga2.write("__ ", font=("Arial",25))
    z+=1
    
while erros<6 and acertos != len(y):
    t = str(window.textinput("caixa de texto", 'digite a letra'))
    for i in range(0,len(y)):
        if t == y[i]:
            
            tartaruga2.penup()
            tartaruga2.setpos(-150+30*i,-25)
            tartaruga2.pendown()
            tartaruga2.write(t,move=True,align="left",font=("Arial",20,"normal"))
            
        
    if t not in y:
        erros+=1
        
        boneco(erros)  
        print(erros)
        
            

     
window.exitonclick()
        
        
        
            
        
        
        
    