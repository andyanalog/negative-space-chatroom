# Negative Space Chatroom

This project is a Flask-based web application that simulates a chatroom inspired by the novel *Negative Space* by B. R. Yeager. The chatroom features bots that respond in a dark and melancholic tone using GPT-2.

***Disclaimer***

*Please be aware that interactions with the bots in this chatroom may not always be precise. The model may occasionally provide unclear, ambiguous, or even aggressive and offensive responses. We recommend using discretion when engaging with the bots and being mindful of the nature of the responses you might receive.*

https://github.com/user-attachments/assets/04bb7bf9-760f-4202-be2b-84afbca09ba1

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

2. **Navigate to the project directory**
   ```bash
   cd negative-space-chatroom
   
3. **Create a virtual enviroment (optional but recommended)**
   ```bash
   python -m venv venv

4. **Activate your virtual enviroment (windows)**
   ```bash
   venv\Scripts\activate

5. **Install the required packages**
   ```bash
   pip install -r requirements.txt

## Usage

1. **Run the Application**
    ```bash
    python app.py

3. **Interact with the Chatroom**

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
