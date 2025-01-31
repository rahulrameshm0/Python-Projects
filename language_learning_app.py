import random
word = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "perro", "english": "dog"},
    {"spanish": "gato", "english": "cat"},
    {"spanish": "libro", "english": "book"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "mañana", "english": "morning/tomorrow"},
    {"spanish": "noche", "english": "night"},
    {"spanish": "hoy", "english": "today"},
    {"spanish": "ayer", "english": "yesterday"},
    {"spanish": "tarde", "english": "afternoon"},
    {"spanish": "coche", "english": "car"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "ciudad", "english": "city"},
    {"spanish": "país", "english": "country"},
    {"spanish": "mundo", "english": "world"},
    {"spanish": "mujer", "english": "woman"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "niño", "english": "child"},
    {"spanish": "hermano", "english": "brother"},
    {"spanish": "hermana", "english": "sister"},
    {"spanish": "padre", "english": "father"},
    {"spanish": "madre", "english": "mother"},
    {"spanish": "abuelo", "english": "grandfather"},
    {"spanish": "abuela", "english": "grandmother"},
    {"spanish": "amable", "english": "kind"},
    {"spanish": "feliz", "english": "happy"},
    {"spanish": "triste", "english": "sad"},
    {"spanish": "fuerte", "english": "strong"},
    {"spanish": "débil", "english": "weak"},
    {"spanish": "rápido", "english": "fast"},
    {"spanish": "lento", "english": "slow"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "pequeño", "english": "small"},
    {"spanish": "blanco", "english": "white"},
    {"spanish": "negro", "english": "black"},
    {"spanish": "rojo", "english": "red"},
    {"spanish": "azul", "english": "blue"},
    {"spanish": "verde", "english": "green"},
    {"spanish": "amarillo", "english": "yellow"},
    {"spanish": "nuevo", "english": "new"},
    {"spanish": "viejo", "english": "old"},
    {"spanish": "caliente", "english": "hot"},
    {"spanish": "frío", "english": "cold"},
    {"spanish": "bueno", "english": "good"},
    {"spanish": "malo", "english": "bad"},
    {"spanish": "felicidad", "english": "happiness"},
    {"spanish": "esperanza", "english": "hope"},
    {"spanish": "salud", "english": "health"},
    {"spanish": "dinero", "english": "money"},
    {"spanish": "problema", "english": "problem"},
    {"spanish": "solución", "english": "solution"},
    {"spanish": "día", "english": "day"},
    {"spanish": "mes", "english": "month"},
    {"spanish": "año", "english": "year"},
    {"spanish": "hora", "english": "hour"},
    {"spanish": "minuto", "english": "minute"},
    {"spanish": "segundo", "english": "second"},
    {"spanish": "camino", "english": "path"},
    {"spanish": "puerta", "english": "door"},
    {"spanish": "ventana", "english": "window"},
    {"spanish": "pared", "english": "wall"},
    {"spanish": "mesa", "english": "table"},
    {"spanish": "silla", "english": "chair"},
    {"spanish": "techo", "english": "ceiling"},
    {"spanish": "piso", "english": "floor"},
    {"spanish": "corazón", "english": "heart"},
    {"spanish": "cabeza", "english": "head"},
    {"spanish": "mano", "english": "hand"},
    {"spanish": "ojo", "english": "eye"},
    {"spanish": "pierna", "english": "leg"},
    {"spanish": "oreja", "english": "ear"},
    {"spanish": "nariz", "english": "nose"},
    {"spanish": "boca", "english": "mouth"},
    {"spanish": "cabello", "english": "hair"},
    {"spanish": "piel", "english": "skin"},
    {"spanish": "mar", "english": "sea"},
    {"spanish": "montaña", "english": "mountain"},
    {"spanish": "río", "english": "river"},
    {"spanish": "bosque", "english": "forest"},
    {"spanish": "cielo", "english": "sky"},
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for i in words:
        print(f"what is the english translation of word {i['spanish']}?")
        user_input = input("Enter your answer: ").strip().lower()
        correct_answer = i['english'].lower()

        if user_input == correct_answer:
            print("You are correct!")
            score += 1
        else:
            print("You have entered wrong answer!")
def main():
    print("Welcome to language learning flashcard app!")
    input("Press enter to start the quiz...")
    quiz_user(word)
if __name__ == "__main__":
    main()
