from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import re
import random

app = Flask(__name__)

# Inicializamos el modelo GPT-2
generator = pipeline('text-generation', model='gpt2')

# Definimos el prompt oscuro y deprimente para todas las personalidades
dark_prompt = (
    "You are a dark and gloomy entity. Respond with a tone that is consistently "
    "pessimistic, dismal, and melancholic. Your answers should reflect a sense of "
    "hopelessness and despair, with no trace of positivity or light."
)

# Lista de nombres para los bots
bot_names = ["droplems.droppeles", "Misty_Paine_", "BBBeez911", "CRAZYBOB", "piSSreSpek"]

# Memoria de conversación para cada bot
bot_memory = {name: [] for name in bot_names}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    # Selección aleatoria de bot si no se menciona uno en específico
    bot_name = random.choice(bot_names)
    
    # Verificamos si el usuario menciona a un bot en particular
    for name in bot_names:
        if name.lower() in user_message.lower():
            bot_name = name
            break
    
    # Usamos el prompt oscuro y deprimente
    prompt = dark_prompt
    
    if user_message:
        # Concatenamos el prompt con el mensaje del usuario y el nombre del bot
        full_message = f"{prompt}\nUser: {user_message}\n{bot_name}:"
        
        # Recuperar la memoria del bot y agregar el mensaje actual
        bot_memory[bot_name].append(user_message)
        
        # Generar texto a partir del mensaje del usuario y el prompt
        responses = generator(full_message, max_length=200, num_return_sequences=1)
        generated_text = responses[0]['generated_text']
        
        # Extraer solo la parte generada después del nombre del bot
        match = re.search(rf'{bot_name}:(.*)', generated_text, re.DOTALL)
        if match:
            bot_response = match.group(1).strip().split('\n')[0].strip()
        else:
            bot_response = "No response generated."
        
        # Guardar la respuesta en la memoria del bot
        bot_memory[bot_name].append(bot_response)
    else:
        bot_response = "No se recibió un mensaje."

    return jsonify({'response': f'{bot_name}: {bot_response}'})

if __name__ == '__main__':
    app.run(debug=True)
