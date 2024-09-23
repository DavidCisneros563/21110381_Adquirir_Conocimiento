#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# chatbot_chivas.py

class ChatbotChivas:
    def __init__(self):
        # Base de datos de preguntas y respuestas sobre las Chivas
        self.database = {
            "hola": "¡Hola! ¿Eres aficionado de las Chivas?",
            "como estas?": "Estoy bien, gracias. ¿Qué te gustaría saber sobre las Chivas?",
            "quien es el jugador mas famoso?": "Uno de los jugadores más famosos es Javier Hernández, conocido como 'Chicharito'.",
            "cuando se fundó el club?": "El Club Deportivo Guadalajara fue fundado el 8 de mayo de 1906.",
            "cuantos campeonatos tiene?": "Las Chivas han ganado 12 títulos de liga hasta la fecha.",
            "cual es el estadio?": "El estadio de las Chivas es el Estadio Akron."
        }

    def get_response(self, user_input):
        # Buscamos una respuesta en la base de datos
        response = self.database.get(user_input.lower())
        
        if response:
            return response
        else:
            # Si no hay match, pedimos nuevo conocimiento
            return self.ask_for_new_knowledge(user_input)

    def ask_for_new_knowledge(self, user_input):
        new_response = input(f"No tengo una respuesta para: '{user_input}'. ¿Cuál debería ser la respuesta? ")
        self.database[user_input.lower()] = new_response
        return f"Gracias, he aprendido algo nuevo: '{user_input}' significa '{new_response}'."

def main():
    print("¡Bienvenido al chatbot de las Chivas!")
    chatbot = ChatbotChivas()
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit"]:
            print("¡Hasta luego!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
