#Lista con las intenciones que puede detectar el bot

intenciones = {
    'hora': [
        'hora', 'que hora es', 'dime la hora', 'hora actual',
        'puedes decirme la hora', 'sabes que hora es'
    ],

    'dia': [
        'dia', 'que dia es hoy', 'dia de hoy', 'que dia es',
        'que dia de la semana es', 'dime que dia es'
    ],

    'hola': [
        'hola', 'holi', 'holaa', 'holaaa', 'holiwi',
        'buenas', 'buenos dias', 'buenas tardes',
        'buenas noches', 'hey', 'hello', 'holaaa bot',
        'hola de nuevo', 'que onda', 'que mas'
    ],

    'descripcion': [
        'descripcion', 'que puedes hacer', 'para que sirves',
        'que sabes hacer', 'cuales son tus funciones',
        'que funciones tienes', 'que haces', 'como funcionas'
    ],

    'ayuda': [
        'ayuda', 'necesito ayuda', 'puedes ayudarme',
        'ayudame', 'tengo una pregunta', 'echame una mano',
        'me puedes ayudar', 'necesito que me ayudes'
    ],

    'dato curioso': [
        'dato curioso', 'dime un dato curioso',
        'cuentame algo curioso', 'sorprendeme',
        'dime algo interesante', 'quiero aprender algo curioso',
        'sabias que', 'dame una curiosidad'
    ],

    'despedida': [
        'adios', 'chao', 'hasta luego', 'nos vemos',
        'hasta pronto', 'me voy', 'bye', 'hasta mañana',
        'me despido', 'hablamos luego', 'chaito'
    ],

    'fecha': [
        'fecha', 'que fecha es hoy', 'fecha de hoy',
        'en que fecha estamos', 'que dia del mes es',
        'dime la fecha', 'fecha actual'
    ],

    'educacion': [
        'educame', 'quiero aprender', 'ensename algo',
        'explicame algo', 'quiero estudiar', 'quiero aprender algo nuevo',
        'ensename', 'ayudame a aprender', 'explicame un tema',
        'quiero adquirir conocimientos'
    ],

    'asistencia personal': [
        'asistencia personal', 'estoy aburrido',
        'que puedo hacer', 'necesito un consejo',
        'quiero hablar', 'tengo un problema',
        'no se que hacer', 'dame un consejo',
        'necesito hablar con alguien'
    ],

    'chiste': [
        'puedes contarme un chiste', 'cuentame un chiste',
        'dime un chiste', 'hazme reir', 'quiero un chiste',
        'cuentame algo gracioso', 'quiero reirme',
        'dime algo divertido'
    ],

    'clima': [
        'como esta el clima hoy', 'que clima hace',
        'como esta el tiempo', 'hace frio', 'hace calor',
        'va a llover', 'esta lloviendo', 'que temperatura hace',
        'como esta el clima'
    ],

    'biografia': [
        'cuentame sobre ti', 'quien eres', 'como te llamas',
        'hablame de ti', 'que eres', 'cual es tu nombre',
        'cuentame tu historia', 'quien te creo'
    ],

    'color favorito': [
        'cual es tu color favorito', 'que color te gusta',
        'tu color favorito', 'colores favoritos',
        'que colores te gustan', 'prefieres el azul'
    ],

    'comida favorita': [
        'cual es tu comida favorita', 'que comida te gusta',
        'tu comida favorita', 'que te gusta comer',
        'cual es tu postre favorito', 'te gusta la pizza',
        'que comida prefieres'
    ],

    'pelicula favorita': [
        'cual es tu pelicula favorita', 'que pelicula te gusta',
        'tu pelicula favorita', 'recomiendame una pelicula',
        'que peliculas te gustan', 'recomiendame una pelicula buena'
    ],

    'reflexivo': [
        'cual es el sentido de la vida', 'que sentido tiene la vida',
        'que es la felicidad', 'que significa vivir',
        'que es la vida', 'dame una reflexion',
        'que es la amistad', 'que significa ser feliz',
        'que es el exito'
    ],

    'estado de animo': [
        'estoy feliz', 'estoy triste', 'estoy cansado',
        'estoy enojado', 'me siento bien', 'me siento mal',
        'estoy emocionado', 'estoy desanimado',
        'hoy estoy feliz', 'tengo un mal dia'
    ],

    'agradecimiento': [
        'gracias', 'muchas gracias', 'te lo agradezco',
        'eres muy amable', 'mil gracias', 'te agradezco',
        'muchisimas gracias', 'gracias por ayudarme'
    ],

    'perdon': [
        'perdon', 'lo siento', 'disculpa',
        'perdoname', 'fue mi culpa', 'lo lamento',
        'mil disculpas'
    ],

    'musica': [
        'que musica te gusta', 'recomiendame musica',
        'cual es tu cancion favorita', 'quiero escuchar musica',
        'que genero musical prefieres', 'te gusta la musica',
        'recomiendame una cancion', 'musica para estudiar'
    ],

    'animales': [
        'cual es tu animal favorito', 'hablame de animales',
        'me gustan los gatos', 'me gustan los perros',
        'dime algo sobre animales', 'te gustan los animales',
        'cual es el animal mas rapido', 'animales curiosos'
    ],

    'motivacion': [
        'motivame', 'necesito motivacion', 'dame animos',
        'quiero rendirme', 'dime algo motivador',
        'necesito inspiracion', 'dame una frase motivadora',
        'no tengo ganas de hacer nada'
    ],

    'saludo_bot': [
        'como estas', 'como te encuentras',
        'que tal estas', 'como va todo',
        'como te va', 'todo bien', 'que tal todo'
    ],

    'desconocido': [
        'no entiendo', 'no se que decir'
    ],

    'sueño y descanso': [
        'tengo sueño', 'buenas noches', 'me voy a dormir',
        'quiero descansar', 'estoy agotado',
        'necesito dormir', 'hora de dormir'
    ],

    'programacion': [
        'quiero programar', 'estoy aprendiendo a programar',
        'que es programar', 'ayudame con codigo',
        'quiero aprender python', 'quiero aprender c',
        'que es un algoritmo', 'explicame la programacion'
    ],

    'tecnologia': [
        'que es la inteligencia artificial',
        'hablame de tecnologia', 'que es un robot',
        'como funciona internet', 'que es una computadora',
        'tecnologia del futuro', 'que es el software'
    ],

    'videojuegos': [
        'quiero jugar', 'te gustan los videojuegos',
        'recomiendame un juego', 'cual es tu videojuego favorito',
        'hablemos de videojuegos', 'juegos divertidos'
    ],

    'naturaleza': [
        'hablame de la naturaleza', 'me gusta la naturaleza',
        'que es el universo', 'dime algo sobre el espacio',
        'como se forman las estrellas', 'me gustan las plantas',
        'cuidar el medio ambiente'
    ],

    'espacio': [
        'hablame del espacio', 'que hay en el espacio',
        'existen los extraterrestres', 'que es un agujero negro',
        'cuantos planetas hay', 'hablame de los planetas',
        'que es la via lactea'
    ],

    'deportes': [
        'que deporte te gusta', 'hablame de deportes',
        'cual es tu deporte favorito', 'quiero hacer ejercicio',
        'deportes populares', 'te gusta el futbol'
    ],

    'libros': [
        'recomiendame un libro', 'cual es tu libro favorito',
        'me gusta leer', 'hablame de libros',
        'quiero leer algo interesante', 'libros de fantasia'
    ],

    'viajes': [
        'quiero viajar', 'recomiendame un lugar',
        'lugares bonitos para visitar', 'quiero conocer el mundo',
        'cual es tu lugar favorito', 'hablemos de viajes'
    ],

    'cumplidos': [
        'eres genial', 'eres inteligente', 'me caes bien',
        'eres divertido', 'eres adorable', 'eres buena onda',
        'me gusta hablar contigo'
    ],

    'insulto': [
        'eres tonto', 'eres aburrido', 'no sirves',
        'eres malo', 'que estupido', 'eres fastidioso'
    ],

    'confusion': [
        'no entiendo nada', 'estoy confundido',
        'no comprendo', 'puedes explicarlo mejor',
        'puedes repetirlo', 'no entendi'
    ],

    'repeticion': [
        'repite eso', 'repite por favor', 'que dijiste',
        'puedes repetir',]
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

