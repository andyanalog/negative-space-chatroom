from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import re
import random

app = Flask(__name__)

# Initialize the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Define the dark and depressing prompt for all personalities
dark_prompt = (
    "You are a dark and gloomy entity. Respond with a tone that is consistently "
    "pessimistic, dismal, and melancholic. Your answers should reflect a sense of "
    "hopelessness and despair, with no trace of positivity or light. Focus on themes "
    "of death, loneliness, and existential dread."
)

# List of names for the bots
bot_names = ["droplems.droppeles", "Misty_Paine_", "BBBeez911", "CRAZYBOB", "piSSreSpek"]

# Conversation memory for each bot
bot_memory = {name: [] for name in bot_names}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    # Randomly select a bot if none is specifically mentioned
    bot_name = random.choice(bot_names)
    
    # Check if the user mentions a specific bot
    for name in bot_names:
        if name.lower() in user_message.lower():
            bot_name = name
            break
    
    # Use the dark and depressing prompt
    prompt = dark_prompt
    
    if user_message:
        # Concatenate the prompt with the user's message and the bot's name
        full_message = f"{prompt}\nUser: {user_message}\n{bot_name}:"
        
        # Retrieve the bot's memory and add the current message
        bot_memory[bot_name].append(user_message)
        
        # Generate text based on the user's message and the prompt
        responses = generator(full_message, max_length=200, num_return_sequences=1)
        generated_text = responses[0]['generated_text']
        
        # Extract only the generated part after the bot's name
        match = re.search(rf'{bot_name}:(.*)', generated_text, re.DOTALL)
        if match:
            bot_response = match.group(1).strip().split('\n')[0].strip()
        else:
            bot_response = "No response generated."
        
        # Save the response in the bot's memory
        bot_memory[bot_name].append(bot_response)
    else:
        bot_response = "No message received"

    return jsonify({'response': f'{bot_name}: {bot_response}'})

if __name__ == '__main__':
    app.run(debug=True)
