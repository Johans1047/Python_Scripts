import turtle

# crea una pantalla para dibujar
screen = turtle.Screen()

# crea una tortuga
t = turtle.Turtle()

# dibuja el cuadro
#for i in range(12):
t.pencolor("red")
t.forward(50)
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.right(180)
t.left(90)
t.forward(1)
t.right(90)
t.forward(50)

t.left(90)
t.forward(1)
t.left(90)
t.forward(50)

t.right(90)
t.forward(1)
t.right(90)
t.forward(50)

t.left(90)
t.forward(1)
t.left(90)
t.forward(50)

t.right(90)
t.forward(1)
t.right(90)
t.forward(50)

t.left(90)
t.forward(1)
t.left(90)
t.forward(50)

t.right(90)
t.forward(1)
t.right(90)
t.forward(50)

t.left(90)
t.forward(1)
t.left(90)
t.forward(50)

t.right(90)
t.forward(1)
t.right(90)
t.forward(50)

# espera a que el usuario cierre la ventana
turtle.done()