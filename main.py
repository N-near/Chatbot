
import turtle
from intencion import deteccion_intenciones
from respuestas import responder
#Haciendo la pantalla de turtle

pantalla = turtle.Screen()
pantalla.title("CHATBOT")
pantalla.setup(width=640,height=640)
pantalla.bgpic("cinnamoroll-gif-11.gif")

#Haciendo las letras de turtle

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0,120)
t.color("pink")
t.write("CHATBOT",align=("center"),font=("Comic Sans MS",40,"normal"))


    

t_respuesta = turtle.Turtle()

t_respuesta.hideturtle()
t_respuesta.penup()

usuario = turtle.textinput("usuario:","Bienvenido :3")



#Respuesta del chatbot
intencion = deteccion_intenciones(usuario)
respuesta = responder(intencion)
t_respuesta.goto(0,-45)
t_respuesta.color('blue')
t_respuesta.write(respuesta,align=("center"),font=("Comic Sans MS",25,"normal"))

#Bucle para que las respuestas puedan ser mas de una
while True:
    usuario = turtle.textinput("usuario:","Bienvenido :3")
    t_respuesta.clear()
    intencion = deteccion_intenciones(usuario)
    respuesta = responder(intencion)
    t_respuesta.write(respuesta,align=("center"),font=("Comic Sans MS",25,"normal"))
    
    #Detiene el programa
    if usuario == "salir":
      break