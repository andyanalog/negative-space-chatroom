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

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/andyanalog/negative-space-chatroom.git

 **Navigate to the project directory**
   cd negative-space-chatroom
   
 **Create a virtual enviroment (optional but recommended)**
  python -m venv venv

 **Activate your virtual enviroment (windows)**
   venv\Scripts\activate

 **Install the required packages**
   pip install -r requirements.txt

## Usage

1. **Run the Application**
    python app.py

   This application will start on **http://127.0.0.1:5000/**

2. **Interact with the Chatroom**

    Open your web browser and navigate to http://127.0.0.1:5000/ to start chatting with the bots.

## How It Works
- GPT-2 Model: The application uses the GPT-2 model from Hugging Face's Transformers library to generate responses.
- Prompt: A dark and melancholic prompt is used to guide the bot responses.
- Bot Selection: If the user does not specify a bot, one is chosen randomly from a predefined list.
- Conversation Memory: Each bot keeps track of its own conversation history.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Flask](https://flask.palletsprojects.com/)

