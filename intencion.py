#Lista con las intenciones que puede detectar el bot

intenciones = {
         'hora'        : ['hora',],
         
         'dia'         : ['dia'],
         
         'hola'        : ['hola'],
         
         'descripcion' : ['descripcion'],
       
         'ayuda'       : ['ayuda'],

         'dato curioso' : ['dato curioso'],
        
         'despedida'    : ['adios','chao'],

         'fecha'        : ['fecha'],

         'educacion'    : ['educame'],

         'asistencia personal'   :['asistencia personal'],

         'chiste'  : ['puedes contarme un chiste'],

         'clima'   : ['como esta el clima hoy'],

         'biografia' : ['cuentame sobre ti'],

         'color favorito' : ['cual es tu color favorito'],

         'comida favorita' : ['cual es tu comida favorita'],

         'pelicula favorita' : ['cual es tu pelicula favorita'],

         'reflexivo'  : ['cual es el sentido de la vida']


    
    }

'''
Esta funcion Detecta si el mensaje de el usuario esta en la lista de intenciones del chatbot 
Para asi mismo devolver un resultado.
'''

def deteccion_intenciones(usuario):
    
     #Esto vuelve el mensaje del usuario a minusculas
        usuario = usuario.lower()

        #vuelve las palabras del usuario en cadenas
        palabras_usuario = usuario.split()

        #Esta variable almacena las intenciones encontradas en el mensaje del usuario
        lista_intenciones = []
        
    
        #el for busca si la intencion y las frases estan en la lista de intenciones del bot
        for intencion, frases in intenciones.items():
            for frase in frases:
                
             #Lee la cantidad de palabras en la frase convertida en una lista
             cantidad_palabras_frase = len(frase.split())
             #Lee la cantidad de palabras de el usuario
             cantidad_palabras_usuario = len(palabras_usuario)
                                           
             for i in range(cantidad_palabras_usuario - cantidad_palabras_frase + 1):
                 grupo_palabras = palabras_usuario[i:i + cantidad_palabras_frase]
            
                 '''
                 Se hace una condicion para evitar la repeticion de palabras como por ejemplo hola hola
                 Si la intencion no esta en la lista se agrega la intencion si ya esta lo contrario
                 Esto no afecta si las intenciones son diferentes
                 '''

                 if grupo_palabras == frase.split():
                  if intencion not in lista_intenciones:
                    lista_intenciones.append(intencion)
  
                              
        #Se hace una condicion para saber si la lista esta llena y devuelve la lista de intenciones
        
        if lista_intenciones != [] :
            return lista_intenciones 
        
        #Este valor se ejecuta cuando no encuentra ninguna coincidencia en el mensaje del usuario

        else:
            return "desconocido"

