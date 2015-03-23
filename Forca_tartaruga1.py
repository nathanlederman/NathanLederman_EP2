
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(50,0)
tartaruga.pendown()
tartaruga.color("orange")

dist = 100


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
    tartaruga.penup()
    tartaruga.setpos(150,225)
    tartaruga.pendown()
    tartaruga.circle(25)
    tartaruga.penup()
    tartaruga.setpos(175,200)
    tartaruga.pendown()
    tartaruga.forward(100)
    tartaruga.backward(60)
    tartaruga.left(45)
    tartaruga.forward(50)
    tartaruga.backward(50)
    tartaruga.left(275)
    tartaruga.forward(50)
    tartaruga.backward(50)
    tartaruga.left(40)
    tartaruga.forward(60)
    tartaruga.left(45)
    tartaruga.forward(75)
    tartaruga.backward(75)
    tartaruga.left(275)
    tartaruga.forward(75)
    tartaruga.backward(75)
    tartaruga.write("tartaruga",align = "center", font=("Arial",14, "normal"))
    

window.exitonclick()


