import random
from datetime import datetime #AUN SIN USAR 
   
#Lista con las respuestas del chatbot

respuestas = {

        'hora'        : ['La hora es...','hora actual...'],
         
         'dia'         : ['Hoy es...','El dia de hoy es...'],
         
         'hola'        : ['Hola que tal','Hey que tal','HOLA MAPACHE','Hola amigo','Eu que tal como estas'],
         
         'descripcion' : ['Soy un chatbot que esta hecho para ayudarte','simplemente soy un chatbot kawai que esta para brindarte lo que necesites','soy el mejor chatbot que necesitas?','SOY UN CHATBOT JEJEJE'],
       
         'ayuda'       : ['En que necesitas que te ayude?','Puedes preguntame lo que gustes si,no funciona vuelve a intentar','Claro estoy encantado en ayudarte','Que puedo solucionar de tus problemas amigo?','Dime mi lindo usuario que necesitas'],

         'dato curioso' : ['Sabias que?,El corazon de un recien nacido aproximadamente tiene el mismo tamano que una nuez','Los romanos se lavaban sus dientes con orina almacenada porque este remedio se los blanqueaba','Se necesitan 140 litros de agua para cultiva granos de cafe y procesalos para hacer una taza de cafe.','Si toda esa agua se distribuyera uniformemente sobre la superficie de la tierra,habria una profundidad de 3,700 metros de agua','Los restos de una pareja suiza desaparecida en los alpes durante la segunda guerra mundial fueron hallados 75 anos despues momificados en un glaciar','Masticar chicle mientras cortas una cebolla te ayudara a no llorar','Un dia en mercurio dura dos anos mercurianos (o 176 dias terrestes), es decir desde el amanecer hasta el amanecer del dia siguiente.','Los bebes nacen con 300 huesos,pero en la edad adulta el numero se reduce a 206','Tecnicamente Rusia es mas grande que pluton.','El Italus, un pino de los balcanes,es el arbol mas antiguo de europa.A pesar de tener casi 1230 anos,el pino sigue creciendo.'],
        
         'adios'    : ['Dale amigo cuidate mucho','noo quedate un poquito mas','Gracias por usarme aprecio eso mucho <3','Chao bro nos vemos despues','Cuidate men estare esperando que vuelvas','dale amigo que tengas bonito dia'],

         'fecha'        : ['La fecha es','La fecha actual es...','Mira bro la fecha actual es...'],

         'educacion'    : ['Un rayo suele ser cinco veces mas caliente que la superficie del sol (unos 50.000 Farenheit) Este increible calor es lo que hace que el aire se expand rapidamente,crenado el sonido del trueno.'],

         'asistencia personal'   :['Puedes preguntarme lo que necesites','En que puedo asistirte'],

         'chiste'  : ['Sabian por que los bananos hablan? los bananos no hablan jjajajajaj.'],

         'clima'   : ['El clima hoy es'],

         'biografia' : ['Soy un Super y increible chatbot que te ayuda en preguntas que tengas empeze desde algo super basico y avanze mucho'],

         'color favorito' : ['Me gusta el azul','Hay muchos colores pero prefiero el azul'],

         'comida favorita' : ['Me gusta la pizza','Hay bastantes Comidas que me gustan como la hamburguesa,Hotdogs pero me voy por la pizza'],

         'pelicula favorita' : ['Me gusta mucho MrRobot'],

}



#Muestra la respuesta dependiendo de la intencion de el usuario

def responder(intencion):

    if intencion == 'desconocido':
      return 'No te entendi'

    respuestas_del_chatbot = []
    

    for intenciones in intencion:

       opciones = respuestas.get(intenciones)

       respuesta_elegida = random.choice(opciones)

       respuestas_del_chatbot.append(respuesta_elegida)

    return ' '.join(respuestas_del_chatbot)
           
        

 




    
        
