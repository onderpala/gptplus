# Import the Chat class from the ai module
from ai import Chat

# Define a multiline string containing information about the chat application
INITIAL_INFORMATION = """
This application is a wrapper of OpenAI's GPT-4.
Encodes all inputs and responses in Base64.
You can ask anything you want.

Commands:
- /new -> Create a new chat
- /history -> Get history of current chat
- /exit -> Exit the chat
- /help -> Get help
- /edit MESSAGE_ID -> Edit a message
** MESSAGE_ID is index of the massage that are represented on the go.
"""


if __name__ == '__main__':

    # Print the initial information to the console
    print(INITIAL_INFORMATION)

    # Create an instance of the Chat class to manage the chat session
    chat = Chat()

    # Enter an infinite loop to continuously read user input
    while True:
        # Read a line of input from the user
        entry = input("> ")

        # Handle different commands
        if entry == '/exit':
            # Exit the program
            exit()

        elif entry == '/help':
            # Print the initial information again
            print(INITIAL_INFORMATION)

        elif entry.startswith('/edit'):

            try:
                # Extract the message ID from the input string
                message_id = int(entry.split()[1])

                # Remove the messages after the specified message ID
                i = len(chat.messages)-1
                while i+1 != message_id:
                    chat.messages.pop(i)
                    i -= 1

            except Exception as e:
                # Handle any exceptions that occur during message editing
                print(e)

        elif entry == "/new":
            # Create a new instance of the Chat class
            chat = Chat()

        elif entry == "/history":
            # Print the history of the current chat
            for i, message in enumerate(chat.messages):
                print("[" + message['role'] + "][" + str(i) + "]")
                try:
                    content = chat.decode(str(message['content']))
                except Exception as e:
                    content = message['content']
                print(content)
                
        else:
            # Send the user input to the chat
            print("[user][" + str(len(chat.messages)) + "]\n" + entry)
            print("[assistant]\n" + chat.send(entry) + "\n")
        

