# Negative Space Chatroom

This project is a Flask-based web application that simulates a chatroom inspired by the novel *Negative Space* by B. R. Yeager. The chatroom features bots that respond in a dark and melancholic tone using GPT-2.

## Features

- **Dark and Melancholic Responses**: Bots respond with a consistently pessimistic and gloomy tone.
- **Random Bot Selection**: A bot is randomly selected to respond if none is specifically mentioned.
- **Memory**: Each bot retains conversation history for more context-aware responses.

## Requirements

- Python
- Flask
- Transformers library (Hugging Face)


## How It Works
- GPT-2 Model: The application uses the GPT-2 model from Hugging Face's Transformers library to generate responses.
- Prompt: A dark and melancholic prompt is used to guide the bot responses.
- Bot Selection: If the user does not specify a bot, one is chosen randomly from a predefined list.
- Conversation Memory: Each bot keeps track of its own conversation history.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
