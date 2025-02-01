# Chat Application with OpenAI GPT-4

This is a simple chat application that interacts with OpenAI's GPT-4 model using the `Chat` class from `ai.py`. The application encodes user input in Base64 and sends it to the OpenAI model for a response.

## Features
- Fully open to any question. ⭐⭐⭐⭐
- Interactive chat interface with OpenAI GPT-4 model.
- Supports multiple commands:
  - `/new`: Create a new chat session.
  - `/history`: Display chat history.
  - `/edit MESSAGE_ID`: Edit a message in chat history.
  - `/help`: Display initial information and help text.
  - `/exit`: Exit the application.
- Keeps a record of chat history for reference.

## Requirements
- Python 3.x
- `openai` library (version 1.61.0)
- `python-dotenv` library (version 1.0.1)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo-name
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your OpenAI API key and model name. See `.env.example` for the required format.

## Usage
1. Run the application:
   ```sh
   python main.py
   ```
2. Interact with the chat interface using the supported commands.

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to enhance the application!

