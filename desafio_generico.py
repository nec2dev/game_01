#Lección 13. Pygame avanzado
"""
El objetivo de la lección.
En esta lección, presentaremos características avanzadas del módulo pygame y crearemos una aplicación gráfica.
"""

"""
aplicación gráfica.
    1. Preguntas iniciales
    2. Ejercicios de calentamiento
    3. Continuación de nuestro primer proyecto de juego.
    4. Resumen

Información para el profesor
El guión se divide en una parte básica y una avanzada/extra. Nuestra tarea es terminar la parte básica del juego: mover al jugador en la pantalla. Podemos empezar la parte del bono si hay tiempo suficiente para hacerlo; tenga en cuenta cuánto logró hacer en su grupo
"""

# 1. Preguntas iniciales
"""
    • ¿Qué es el módulo pygame?
    • Aparte de la instalación, ¿qué es necesario para que funcione el módulo pygame? Respuesta: Inicialización - pygame.init()
    • ¿Qué pasará si el programador se olvida de leer los eventos o de actualizar?¿la ventana? Respuesta: El programa se congelará.
    • ¿Al hacer clic en el botón X se cerrará el programa de forma predeterminada? Respuesta: No, el evento está registrado, pero si se lee y maneja correctamente es trabajo de los programadores. El programador debe asegurarse de leer este evento y en En este caso, rompa el ciclo y salga de la aplicación con elegancia.
    • ¿Qué significa RGB?
    • ¿Cuál es el rango que cada variable R - G - B puede contener como valor? Respuesta: 0-255
"""


# 2. Ejercicio de calentamiento
"""
Creando tus propios gráficos de reproductor, por ejemplo en MS Paint. Tamaño: 40 x 40 píxeles.
Coloque el archivo de imagen en la carpeta de su proyecto y asegúrese de que este nombre de archivo se use en un Versión del proyecto de la lección 12:
"""

# 3. Continuación del primer proyecto de juego.
"""
Movimiento de jugadores : nuestro plan
Nos gustaría controlar el jugador que pudimos mostrar. Para poder hacer eso nosotros necesitamos planificar las siguientes funciones:
    • función responsable del movimiento del jugador
    • función responsable de interpretar el evento de teclas presionadas del teclado
Moviendo nuestros gráficos en la pantalla Al agregarlos a nuestro programa, le informamos al script cuál debería ser la posición inicial de esta imagen en la pantalla. Esta posición se puede cambiar. Crear un set_position_image tomando dos parámetros: img_list y position:
    • img_list es una lista de la función load_image
    • La posición contiene nuevas coordenadas de un objeto
Creemos un elemento rect y devolvamos una lista de 3 elementos.
        def set_position_image(img_list, position):
            image, surface, rect = img_list
            rect = surface.get_rect(center=position)
            return [image, surface, rect]

Eventos de teclas presionadas del teclado
Dentro de un bucle while tenemos que leer qué teclas del teclado se presionan en un momento determinado momento. Para cada tecla obtendremos Verdadero (presionada) o Falso (no presionada).
        pressed_keys = pygame.key.get_pressed()
        # Display player
        print_image(player)

Tenemos que crear una función que verifique si las teclas que nos interesan están presionadas y ejecute una acción adecuada para una tecla determinada. Llamaremos a esta función calculate_player_movement.
Usaremos variables constantes del módulo pygame para verificar si una clave determinada fue presionado. Esas variables se denominan: K_x, donde x es una clave que nos interesa. Variables: delta_x y delta_y contienen información sobre el cambio de posición: ¿cuántos píxeles si el jugador se mueve a lo largo de los ejes x e y.?
        def calculate_player_movement(keys):
            # Moving the player
            speed = 10
            delta_x = 0
            delta_y = 0
            if keys[pygame.K_w]:
                delta_y -= speed
            if keys[pygame.K_s]:
                delta_y += speed
            if keys[pygame.K_d]:
                delta_x += speed
            if keys[pygame.K_a]:
                delta_x -= speed
            return [delta_x, delta_y]

Para grupos ambiciosos
Agregue un aumento de velocidad si se presiona la tecla Mayús.
        delta_y = 0
        if keys[pygame.K_LSHIFT]:
            speed *= 2
        if keys[pygame.K_w]:

Volviendo a todos los grupos
Devolvemos los delta_x y delta_y calculados como una lista. Volvamos a nuestro mientras bucle para usar nuestra función y obtener los valores delta_x y delta_y .
        pressed_keys = pygame.key.get_pressed()
        # # # # # # # # # # # # # # # # # # #
        delta_x, delta_y = calculate_player_movement(pressed_keys)
        # Change coordinates
        player_pos[0] += delta_x
        player_pos[1] += delta_y
        # Move image to new coordinates
        player = set_position_image(player, player_pos)
        # # # # # # # # # # # # # # # # # # #
        # Fill the background

Explicación del código anterior • 
    • Tomar nuevas coordenadas del jugador
        # Change coordinates
        player_pos[0] += delta_x
        player_pos[1] += delta_y

    • Modificar la posición de la imagen.
        # Zmiana współrzędnych obrazu
        player = set_position_image(player, player_pos)

También hay otro problema.
Mover nuestro reproductor crea una mancha en la pantalla. Los gráficos mostrados anteriormente todavía son visibles. Para resolver este problema necesitamos actualizar no sólo los gráficos del reproductor sino también el fondo. Hoy configuraremos el fondo en un color liso, pero es También es posible crear gráficos separados para ello.
Agregar variable para mantener el color de fondo en formato RGB:
        player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        player = load_image('player.png', player_pos)
        background_color = [9, 42, 121]

Dentro del bucle while necesitamos agregar relleno de fondo.
        # Fill the background
        screen_surface.fill(background_color)
        # Display the player
        print_image(player)

Atención al estropear el orden en el que coloreamos el fondo y mostramos el player puede resultar en que nuestro reproductor quede oculto. Cuando ejecutamos el programa podemos ver que es posible mover nuestro reproductor fuera de la pantalla.

Limitar el movimiento del jugador para que no pueda pasar el borde de la pantalla.
Creemos una función limit_position tomando coordenadas como parámetros y verifiquemos si son válidos. Si están fuera de un rango adecuado, debería modificarlos para que encajen.
dentro de la pantalla del programa. Si hay mucho tiempo podemos pedir a los estudiantes que hagan esto por ellos mismos. Démosles pistas y mostrémosles la plantilla de funciones.
        def limit_position(position):
        x, y = position
        # # # # # # # # # # # #
        # Your solution here #
        # # # # # # # # # # # #
        return [x, y]
Una de las posibles soluciones:
        def limit_position(position):
            x, y = position
            x = max(0, min(x, SCREEN_WIDTH))
            y = max(0, min(y, SCREEN_HEIGHT))
            return [x, y]
Agreguemos la función limit_position :
        player_pos[1] += delta_y
        # # # # # # # # # # # # # # # # # # # # #
        #     Check the coordinates limits      #
        player_pos = limit_position(player_pos) #
        # # # # # # # # # # # # # # # # # # # # #
        # Change the image coordinates

StandarGame.py
Parte Extra
Continuación del proyecto: la parte avanzada
Antes de comenzar esta parte de la lección tenemos que crear la parte básica del juego. Este parte es sólo para grupos ambiciosos que fueron rápidos en conseguir todo el trabajo anterior hecho. En esta parte del proyecto agregaremos nuevos objetos que el jugador recopilará para puntos
Enlace a gráficos:
https://drive.google.com/drive/folders/1i1tFyICDx9JAf1uU0nlbQkcoPhN4FM44
Al comienzo de nuestro script (después de crear la variable de reloj ) agregamos una lista en la que mantendremos los nombres de nuestros gráficos. Así es como debería verse:
        bonus_images = [
            'bonus_1.png',
            'bonus_2.png',
            'bonus_3.png'
        ]
Necesitamos almacenar los objetos creados en la memoria del programa. Usemos una nueva lista que llamaremos bonus_objects. Todos los objetos creados se agregarán a esta lista. Cuando un El objeto ya no será necesario, lo eliminaremos de la lista.
        # Lista of bonus objects
        # Each object is a 3-element list returned by the load_image function
        bonus_objects = []

Creando un nuevo objeto de bonificación
Los objetos de bonificación deberían aparecer en la pantalla de vez en cuando, pero primero escribamos el código responsable de crear un objeto: elige uno de los gráficos disponibles para un objeto de bonificación y lo guarda en la lista de objetos_bonificaciones .
Comencemos importando dos funciones del módulo aleatorio . La función de elección devuelve un elemento aleatorio de una lista determinada. La función randint devuelve un número entero de un rango determinado (cerrado a la izquierda, abierto a la derecha).
Dentro de la función seleccionamos un nombre de gráfico aleatorio. Luego seleccionamos al azar coordinar dentro de nuestra pantalla donde debe aparecer el objeto. Guardamos tanto x como y coordenadas de una variable: una lista. Usamos una función creada en la lección anterior para cargue los gráficos, debe tomar el nombre del archivo y las coordenadas iniciales como parámetros. Agregamos el objeto recién creado a la lista bouns_objects .
        from random import choice, randint
        def generate_bonus_object():
            # Select random name from bonus_images
            image_name = choice(bonus_images)
            # Select random coordinates for an object
            x = randint(0, SCREEN_WIDTH)
            y = randint(0, SCREEN_HEIGHT)
            # The position variable is a 2-element list
            position = [x, y]
            # Create the graphics using the load_image function
            new_obj = load_image(image_name, position)
            # Add new object to the list of all bonus objects
            bonus_objects.append(new_obj)
            pass
            
Función que muestra objetos extra
Mantener todos los objetos de bonificación en una lista facilita la escritura de una función utilizada para mostrarlos todos. Usemos la función print_image creada anteriormente .
        def print_bonus_objects():
            # Iterate over bonus_objects
            for obj in bonus_objects:
                # Display object on the screen,
                # using previously created function
                print_image(obj)
                pass
            pass

Llamar a la función que genera objetos y función que los muestra en pantalla. Dentro del bucle while después de la instrucción print_image(player) :
        # Adding bonus - First time generation without limiting condition ;)
        generate_bonus_object()
        print_bonus_objects()

¿Cuál es el problema aquí? Deje que los estudiantes descubran cómo resolver un error con nuevos elementos de desove.

Limitar el número de objetos de bonificación
Podemos utilizar un mecanismo simple para generar nuevos objetos después de un tiempo Usemos el número de fps para saber la hora.
    • al comienzo del script, creemos una variable FRAMES_PER_SECOND donde mantendremos el FPS esperado: 30 o 60.
    • Usemos esta variable en la función clock.tick(FRAMES_PER_SECOND) .
    • Creemos una función frames_cnt que será el contador de los archivos mostrados marcos. Su valor inicial debe establecerse en 0.
    • Agreguemos la instrucción frames_cnt += 1 después de: pygame.display.update()
    • Convirtamos la función generate_bonus_object() en una declaración condicional que decidirá si los objetos deben generarse en función de frames_cnt valor. Hará que los objetos aparezcan con menos frecuencia.

Si todavía queda algo de tiempo, entreguemos esto a nuestros estudiantes como tarea.

Usando frames_cnt y FRAMES_PER_SECOND preparemos el condicional declaración que se ejecutará solo una vez por segundo Sugerencia: use el operador de módulo. Solución:
        if frames_cnt % (FRAMES_PER_SECOND * 1) == 0:
            generate_bonus_object()
            pass
            
El número en la instrucción FRAMES_PER_SECOND * 1 representa el número de segundos (en nuestro caso 1)

Eliminar objeto de bonificación cuando el jugador lo toca
Ahora tenemos un juego donde aparecen objetos de bonificación en la pantalla pero no hay nada sucede cuando el jugador los toca. Creemos una función responsable de verificar si el jugador tocó un objeto. Si es así debería eliminarse.
        def check_collisions():
            rect_player = player[2]
            # Two ways to iterate over objects
            # for i in range(len(bonus_objects)):
            # index = len(bonus_objects) - 1 - i
            for index in range(len(bonus_objects) - 1, -1, -1):
                obj = bonus_objects[index]
                rect = obj[2]
                if rect.colliderect(rect_player):
                    bonus_objects.pop(index)
                    pass
                pass
            pass
            
Información para el profesor 
Hay dos formas de iterar sobre objetos: ya sea complicada rango o una variable adicional. Para detectar colisiones utilizamos una función relacionada con los gráficos de pygame. Gráficos rect es un rectángulo y podemos comprobar si está chocando con un rectángulo de otro gráficos. Para hacer esto, guardemos el rectángulo del reproductor en una variable rect_player (por leyendo el segundo elemento de la lista de jugadores . A continuación queremos iterar a través de todos objetos de bonificación para comprobar cuál debe eliminarse.

Importante Empezamos desde el final porque cuando eliminamos elementos de la lista podemos cambiar índices en la lista. Cuando eliminamos elementos al final de la lista, no tener algún impacto negativo.

Detección de colisiones
Antes de print_bonus_objects() agregamos la llamada a la función check_collisions() .

Ejercicio adicional
Si no queda mucho tiempo, puede mostrarles a los estudiantes cómo funcionaría el programa si se aplicara el bono. Los objetos aparecen con cada nuevo fotograma: comente la declaración condicional utilizada.para limitar el número de objetos de bonificación.

Puntos de jugador
Al comienzo del script, agreguemos una variable player_points establecida en 0. Para cada elemento eliminado de la lista bonus_objects agregamos 1 punto - incrementamos la variable. Importante: Tenemos que agregar una palabra clave global si queremos modificar player_points variable dentro de una función.
        # Number of points gathered by player
        player_points = 0
        def check_collisions():
            global player_points
            rect_player = player[2]
            # for i in range(len(bonus_objects)):
            # index = len(bonus_objects) - 1 - i
            for index in range(len(bonus_objects) - 1, -1, -1):
                obj = bonus_objects[index]
                rect = obj[2]
                if rect.colliderect(rect_player):
                    bonus_objects.pop(index)
                    player_points += 1
                    pass
                pass
            pass

Mostrar puntos en la terminal.  
        print(f"\rPoints: {player_points}", end='')

Mostrar puntos en la pantalla del juego.
    • Al comienzo del script, creemos un objeto de fuente (lo hacemos una vez, no en cada llamada de función). Podemos utilizar una fuente y tamaño diferente.
    • Dentro de la función, creemos variables para los parámetros de texto mostrados.
    • Utilizando la fuente creada anteriormente creamos un mensaje de visualización.
    • Mostrar el mensaje mostrado en la pantalla.
    • La función debe llamarse en el bucle del juego. - Recuerda el orden. Cada vez muestra algo en la pantalla, puede sobrescribir algún otro objeto. El mensaje debería aparecer al final justo después de actualizar la pantalla.
        POINTS_FONT = pygame.font.SysFont("verdana", 20)
        def print_points(points: int) -> None:
            text = f"Points: {points}"
            color = [255, 255, 255]
            position = [0, 0]
            label = POINTS_FONT.render(text, False, color)
            screen_surface.blit(label, position)
            pass            
        print_points(player_points)

CompleteGame.py    
"""

# 4. Resumen
"""
    • ¿Qué es el módulo pygame?
    • Aparte de la instalación, ¿qué es necesario para que funcione el módulo pygame? Respuesta: Inicialización - pygame.init()
    • ¿Qué pasará si el programador se olvida de leer los eventos o de actualizar? ¿la ventana? Respuesta: El programa se congelará.
    • ¿Cómo almacenamos muchos elementos gráficos de manera que podamos rastrearlos fácilmente? Respuesta: use una lista
    • ¿Cómo limitamos la cantidad de objetos que aparecen en la pantalla? Respuesta: Ejecutamos la función una vez por cada X cantidad de fotogramas.
    • ¿Podemos leer todas las teclas presionadas a la vez en lugar de usar eventos? Respuesta: Sí, utilizamos un método pygame donde obtenemos un valor bool para cada uno.
    Tecla: verdadero significado presionado.
"""