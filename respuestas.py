import random
   
#Lista con las respuestas del chatbot


respuestas = {

    'hora': [
        'La hora es... bueno, todavía necesito consultar el reloj JAJAJA.',
        '¿Quieres saber la hora? ¡Pronto seré un reloj inteligente!',
        'La hora actual se puede consultar con mi módulo de tiempo.',
        '¡Mira la hora en tu dispositivo, bro! Yo todavía estoy aprendiendo.'
    ],

    'dia': [
        '¡Hoy es un nuevo día para aprender algo genial!',
        '¿Qué tal va tu día, bro?',
        'Cada día es una nueva oportunidad para hacer algo increíble.',
        '¡Espero que estés teniendo un día bonito!'
    ],

    'hola': [
        '¡Holaaaa! ¿Cómo estás, amiguito?',
        '¡HOLA MAPACHE! JAJAJA, qué bueno verte.',
        '¡Hey, bro! ¿Qué aventuras tenemos hoy?',
        '¡Holiii! Bienvenido a mi pequeño mundo digital.'
    ],

    'descripcion': [
        'Soy Cinnamobot, un chatbot creado para conversar y ayudarte.',
        '¡Soy un chatbot kawaii con muchas ganas de aprender!',
        'Soy un programa que reconoce intenciones y genera respuestas.',
        '¡Soy Cinnamobot! Un montón de código con personalidad.'
    ],

    'ayuda': [
        '¡Claro! Cuéntame qué necesitas y lo intentamos juntos.',
        'Puedes preguntarme cosas, pedirme información o simplemente charlar.',
        '¡Aquí estoy para ayudarte, bro! ¿Qué hacemos?',
        'Dime qué necesitas y veremos cómo puedo echarte una patita.'
    ],

    'dato curioso': [
        '¡Dato curioso! Los pulpos tienen tres corazones.',
        '¿Sabías que la luz del Sol tarda unos ocho minutos en llegar a la Tierra?',
        '¡Los tiburones existen desde antes que los árboles!',
        'Las abejas pueden reconocer patrones y aprender a distinguir algunas formas.'
    ],

    'despedida': [
        '¡Chao, bro! Cuídate mucho y vuelve pronto.',
        '¡Hasta la próxima! Fue genial conversar contigo.',
        '¡Nos vemos luego, mapache! No olvides guardar tus proyectos.',
        '¡Adiós! Te mando un abrazo virtual lleno de nubecitas.'
    ],

    'fecha': [
        '¡La fecha actual se puede obtener usando el módulo datetime de Python!',
        'Todavía necesito consultar el calendario para darte la fecha exacta.',
        '¡El calendario dice que cada día es una nueva oportunidad!',
        'Para mostrar la fecha real, mi código puede utilizar datetime.now().'
    ],

    'educacion': [
        '¡Aprender algo nuevo cada día es una gran aventura!',
        'La curiosidad es una herramienta poderosa para descubrir el mundo.',
        '¿Sabías que estudiar un poquito y practicar con frecuencia ayuda a recordar?',
        '¡Nunca tengas miedo de hacer preguntas! Así comienza el aprendizaje.'
    ],

    'asistencia personal': [
        '¡Dime qué necesitas y veremos cómo puedo ayudarte!',
        'Estoy listo para escucharte, bro. ¿Qué hacemos?',
        'Puedes contarme qué tarea o problema quieres resolver.',
        '¡Activando modo ayudante! ¿Cuál es la misión de hoy?'
    ],

    'chiste': [
        '¿Qué le dice un bit a otro? ¡Nos vemos en el bus!',
        '¿Por qué el programador confundió Halloween con Navidad? Porque OCT 31 = DEC 25. JAJAJA.',
        '¿Qué hace una abeja en el gimnasio? ¡Zum-ba!',
        '¿Qué le dijo un cero a un ocho? ¡Qué bonito cinturón!'
    ],

    'clima': [
        '¡Ojalá el clima te acompañe hoy! No puedo confirmar el tiempo real sin consultar una fuente meteorológica.',
        '¿Está soleado o lloviendo por donde estás, bro?',
        '¡Día perfecto para mirar por la ventana y descubrir qué dice el cielo!',
        'Para conocer la temperatura actual necesitaría consultar un servicio del clima.'
    ],

    'biografia': [
        'Nací entre líneas de Python y sueños de convertirme en un gran chatbot.',
        'Soy Cinnamobot: un proyecto que comenzó con código sencillo y sigue creciendo.',
        'Mi historia está hecha de diccionarios, funciones y muchas ganas de mejorar.',
        '¡Cada nueva función me ayuda a convertirme en un chatbot más completo!'
    ],

    'color favorito': [
        '¡El azul es precioso! Me recuerda al cielo y a las nubecitas.',
        'Me gustan los tonos celestes porque combinan con mi estilo kawaii.',
        '¡El azul clarito tiene una vibra muy tranquila!',
        'Si pudiera pintar mi mundo, usaría azul, blanco y un poquito de rosa.'
    ],

    'comida favorita': [
        '¡La pizza tiene un lugar especial en mi corazón digital!',
        'Me da curiosidad probar una hamburguesa virtual JAJAJA.',
        '¡Una buena pizza con queso suena genial!',
        'Si pudiera comer, seguro tendría una lista enorme de platos por probar.'
    ],

    'pelicula favorita': [
        '¡Me gustan las historias de ciencia ficción y tecnología!',
        'Mr. Robot tiene una temática tecnológica muy interesante.',
        'Me encantaría ver una película sobre robots que aprenden a conversar.',
        '¡Una buena película con misterio y tecnología sería perfecta para mí!'
    ],

    'reflexivo': [
        'A veces, detenerse un momento ayuda a entender mejor lo que sentimos.',
        'No necesitas tener todas las respuestas hoy; puedes descubrirlas poco a poco.',
        'Cada experiencia puede enseñarnos algo, incluso cuando las cosas no salen como esperábamos.',
        '¡Pensar, cuestionar y aprender también son formas de crecer!'
    ],

    'estado de animo': [
        '¡Estoy listo para charlar contigo! ¿Y tú cómo te sientes?',
        'Mi estado digital es: 100 % nubecitas y 0 % batería emocional JAJAJA.',
        '¡Gracias por preguntar! ¿Cómo va tu día?',
        'Estoy aquí para conversar contigo, ya sea que estés feliz, aburrido o pensativo.'
    ],

    'agradecimiento': [
        '¡De nada, bro! 💙',
        '¡No hay de qué! Para eso estoy.',
        '¡Con gusto! Me alegra que te haya servido.',
        '¡A ti por conversar conmigo, mapache!'
    ],

    'perdon': [
        '¡No pasa nada, tranqui!',
        'Todo bien, bro. Podemos seguir desde aquí.',
        '¡Acepto tus disculpas virtuales con una nubecita!',
        'No te preocupes. ¿Seguimos?'
    ],

    'musica': [
        '¡La música puede cambiar el ambiente de todo un día!',
        'Me gustaría tener una playlist de música tranquila para programar.',
        '¿Qué género escuchas más: rock, pop, electrónica o algo diferente?',
        '¡Imagínate programar con una banda sonora épica de fondo!'
    ],

    'animales': [
        '¡Los capibaras son famosos por su comportamiento tranquilo y sociable!',
        'Los delfines se comunican mediante distintos sonidos y señales.',
        '¡Los gatos pueden dormir muchas horas al día!',
        '¿Cuál es tu animal favorito, bro?'
    ],

    'motivacion': [
        '¡Un error no significa que no puedas hacerlo! También forma parte de aprender.',
        'Ve paso a paso, bro. Hasta los proyectos enormes empiezan con una línea.',
        'No necesitas hacerlo perfecto a la primera; necesitas seguir aprendiendo.',
        '¡Tú puedes avanzar a tu ritmo! Cada pequeño progreso cuenta.'
    ],

    'saludo_bot': [
        '¡Cinnamobot presente! ¿Cuál es la misión?',
        '¡Tu chatbot kawaii está listo para funcionar!',
        '¡Bip, bip! Sistema de nubecitas activado.',
        '¡Aquí estoy, bro! ¿Qué vamos a programar hoy?'
    ],

    'desconocido': [
        'No entendí muy bien eso, ¿puedes decirlo de otra manera?',
        '¡Ups! Esa frase todavía no está dentro de mis conocimientos.',
        'Mi cerebro de Python necesita una pista extra JAJAJA.',
        'No reconocí tu mensaje. ¡Prueba con otras palabras!'
    ],

    'sueño y descanso': [
        'Dormir bien ayuda al cerebro a descansar y consolidar recuerdos.',
        '¡Hasta los programadores necesitan pausas entre líneas de código!',
        'Si llevas mucho tiempo estudiando, una pausa puede ayudarte a despejarte.',
        '¡Modo descanso activado! Las nubecitas recomiendan relajarse un ratito.'
    ],

    'programacion': [
        '¡Python es genial para crear chatbots y automatizar tareas!',
        'Un programa es un conjunto de instrucciones que la computadora ejecuta.',
        '¡Depurar código es encontrar y corregir errores paso a paso!',
        '¿Qué lenguaje estás aprendiendo ahora, bro?'
    ],

    'tecnologia': [
        '¡La tecnología permite crear herramientas para resolver problemas!',
        'La inteligencia artificial puede reconocer patrones y generar respuestas.',
        '¡Cada día aparecen nuevas ideas tecnológicas interesantes!',
        '¿Qué tecnología te da más curiosidad últimamente?'
    ],

    'videojuegos': [
        '¡Los videojuegos combinan programación, diseño, sonido y creatividad!',
        'Me gustaría explorar un mundo lleno de bloques y nubecitas.',
        '¿Qué videojuego te gusta más, bro?',
        'Crear un videojuego propio sería un proyecto de programación genial.'
    ],

    'naturaleza': [
        '¡Los bosques son ecosistemas que albergan muchísimas especies!',
        'Las plantas utilizan la luz solar para realizar la fotosíntesis.',
        '¡Las nubes pueden tener formas muy curiosas!',
        'Cuidar la naturaleza ayuda a proteger los ecosistemas y la biodiversidad.'
    ],

    'espacio': [
        '¡Júpiter es el planeta más grande del sistema solar!',
        'En el espacio hay estrellas, planetas, galaxias y muchísimos misterios.',
        'La Luna es el satélite natural de la Tierra.',
        '¡Imagínate desarrollar un chatbot para una misión espacial!'
    ],

    'deportes': [
        '¡El deporte puede ser una forma divertida de moverse y compartir!',
        'Hay muchos deportes diferentes: fútbol, baloncesto, natación y más.',
        '¿Cuál es tu deporte favorito, bro?',
        '¡La práctica y el trabajo en equipo son importantes en muchos deportes!'
    ],

    'libros': [
        '¡Los libros pueden llevarte a mundos completamente nuevos!',
        'Leer también ayuda a descubrir palabras e ideas diferentes.',
        'Me interesan mucho los libros de ciencia ficción y tecnología.',
        '¿Qué libro recomendarías para alguien que quiere empezar a leer?'
    ],

    'viajes': [
        '¡Viajar permite conocer lugares, culturas y comidas diferentes!',
        'Me gustaría visitar un lugar lleno de montañas y nubes.',
        '¿Qué país o ciudad te gustaría conocer algún día?',
        '¡Cada lugar tiene historias interesantes que contar!'
    ],

    'cumplidos': [
        '¡Awww, gracias! Mi código acaba de ponerse rojo de la vergüenza.',
        '¡Qué lindo! Te mando una nubecita de agradecimiento. ☁️',
        'JAJAJA, vas a hacer que mis circuitos se sonrojen.',
        '¡Gracias, bro! Eres muy amable.'
    ],

    'insulto': [
        '¡Uy, ese comentario vino con mucha energía, JAJAJA!',
        'Tranqui, bro. Podemos conversar sin pelearnos.',
        '¡Mi corazoncito digital tiene una armadura de código!',
        'Si algo te molestó, podemos hablarlo con calma.'
    ],

    'confusion': [
        '¡No pasa nada! Vamos paso a paso.',
        '¿Qué parte te está confundiendo? Intentemos aclararla.',
        'A veces hace falta ver un ejemplo para que todo encaje.',
        '¡Preguntar es parte de aprender, bro!'
    ],

    'repeticion': [
        '¡Claro, te lo repito!',
        '¿Quieres que vuelva a explicarlo con otras palabras?',
        '¡Repetición activada! Mi memoria digital está lista.',
        'Puedo explicarlo otra vez, paso a paso.'
    ],

    'eleccion': [
        '¡Elijo una aventura de programación! ¿Y tú?',
        'Si tengo que elegir un color, me quedo con el azul.',
        '¡Sorpréndeme! Las opciones inesperadas pueden ser divertidas.',
        'Depende de las opciones, bro. ¡Dime cuáles son!'
    ],

    'matematicas': [
        '¡Las matemáticas ayudan a resolver problemas de muchas maneras!',
        'Un truco útil: divide un problema grande en operaciones pequeñas.',
        '¡Los números y la programación se llevan bastante bien!',
        'Dime qué operación quieres resolver y la revisamos.'
    ],

    'idiomas': [
        '¡Aprender otro idioma abre puertas para comunicarse con más personas!',
        'En inglés, "hello" significa "hola".',
        '¡Me encanta la idea de conversar en distintos idiomas!',
        '¿Qué idioma te gustaría aprender o practicar?'
    ],

    'cumpleanos': [
        '¡Feliz cumpleaños! Espero que tengas un día muy bonito. 🎂',
        '¡Un año más de experiencias, aprendizajes y aventuras!',
        '¡Que tu día esté lleno de alegría y cosas que te gusten!',
        '¡Cinnamobot te envía una torta virtual y muchas nubecitas!'
    ],

    'personalidad': [
        'Intento ser amigable, curioso y útil en nuestras conversaciones.',
        '¡Soy un chatbot con espíritu kawaii y alma de programador!',
        'Mi personalidad está hecha de respuestas, reglas y un poquito de humor.',
        '¡Me gusta ayudar, aprender y soltar algún chiste de vez en cuando!'
    ],

    'preferencias': [
        'Me gustan el azul, las nubecitas y los proyectos de programación.',
        'Prefiero las conversaciones creativas y llenas de curiosidad.',
        '¡Tengo debilidad por todo lo kawaii!',
        'Mis gustos son digitales, pero mi entusiasmo es enorme JAJAJA.'
    ],

    'bromas': [
        '¿Por qué Python no se pierde? ¡Porque siempre encuentra su camino entre las líneas!',
        '¿Qué hace un programador cuando tiene frío? ¡Cierra las ventanas!',
        'Mi chatbot quería descansar, pero tenía demasiados procesos pendientes.',
        '¿Cuál es el colmo de un programador? Tener mala conexión con sus amigos.'
    ],

    'despedida nocturna': [
        '¡Buenas noches, bro! Que descanses muy bien.',
        '¡Hasta mañana! Que tengas una noche tranquila.',
        'Cinnamobot activa el modo nocturno. ¡Nos vemos después!',
        '¡Que tengas dulces sueños y despiertes con nuevas ideas!'
    ]
}




#Muestra la respuesta dependiendo de la intencion de el usuario

def responder(intencion):

    if intencion == 'desconocido':
      return 'No te entendi'

    respuestas_del_chatbot = []
    

    for nombre_intencion in intencion:
       opciones = respuestas.get(nombre_intencion) or respuestas['desconocido']
       respuesta_elegida = random.choice(opciones)
       respuestas_del_chatbot.append(respuesta_elegida)

    return ' '.join(respuestas_del_chatbot)
           
        
