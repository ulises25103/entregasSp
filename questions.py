import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#crea una nueva lista con la pregunta, la respuesta y el indice de la respuesta correcta, haciendolo de forma random.
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

puntaje = 0
# El usuario deberá contestar 3 preguntas
for pregunta, opciones, correcta in questions_to_ask:
# Se selecciona una pregunta aleatoria
    print(pregunta)
# Se muestra la pregunta y las respuestas posibles

    for i, answer in enumerate(opciones, start = 1):
        print(f"{i}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isdigit() == False or int(user_answer) < 1 or int(user_answer) > 4:
            print("Respuesta no válida")
            exit(1)
        user_answer = int(user_answer)
    # Se verifica si la respuesta es correcta
        if user_answer -1 == correcta:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
            print("Incorrecto.")
            if intento == 1:
                print("La respuesta correcta era:", correcta + 1)
                puntaje -= 0.5  # solo descuenta si falló ambos intentos
    # Se imprime un blanco al final de la pregunta
print()

print('el puntaje es: ', puntaje)