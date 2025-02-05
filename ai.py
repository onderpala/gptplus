from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

class Chat:
    """
    Represents a chat session with an OpenAI model, where all messages are encoded and decoded in Base64.

    Attributes:
        client (OpenAI): The OpenAI client used to interact with the model.
        messages (list): A list of messages in the chat session, where each message is a dictionary with 'role' and 'content' keys.

    Methods:
        __init__(messages=False): Initializes the chat session with an OpenAI client and a list of initial messages.
        add_to_chat(role, content): Adds a message to the chat with the specified role and content.
        send(message='hello'): Sends a message to the chat, encodes it in Base64, and returns the response from the OpenAI model.
        encode(message): Encodes a message in Base64.
        decode(message): Decodes a Base64-encoded message.

    Notes:
        This class is designed to work with OpenAI's GPT-4 model, and the send method assumes that the model is configured to respond to Base64-encoded messages.
    """
    def __init__(self, messages=False):

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.messages = []
        initial_messages = [
                {"role": "system", "content": (
                    "You are an assistant that communicates exclusively in Base64. "
                    "All responses should be encoded in Base64 before being returned. "
                    "Do not include plain text in your responses."
                )},
                {
                    "role": "user",
                    "content": "ZnJvbSBub3cgb24sIHJlc3BvbnNlIHdpdGggYmFzZTY0Lg=="
                }
            ]
        if messages:
            messages = initial_messages + messages
            for message in messages:
                self.add_to_chat(message['role'], message['content'])
        else:
            self.messages = initial_messages

    def add_to_chat(self, role, content):
        """
        Adds a message to the chat.

        Parameters
        ----------
        role : str
            The role of the message sender. Should be one of 'system', 'user',
            or 'assistant'.
        content : str
            The content of the message to be added.

        Returns
        -------
        None
        """

        self.messages.append({"role": role, "content": content})

    def send(self, message='hello'):
        """
        Sends a message to the chat and returns the response.

        Parameters
        ----------
        message : str
            The message to be sent to the chat.

        Returns
        -------
        str
            The response from the chat.

        Raises
        ------
        Exception
            If there is an error in the chat API call.
        """
        encoded = self.encode(message)
        self.add_to_chat("user", encoded)

        self.chat = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=self.messages
        )
        try:
            res = self.chat.choices[0].message.content
            decoded = self.decode(res)
        except Exception as e:
            raise Exception(e)

        self.add_to_chat('assistant', res)

        return decoded
    

    def encode(self, message):
        """
        Encodes a message in Base64.

        Parameters
        ----------
        message : str
            The message to be encoded.

        Returns
        -------
        str
            The Base64 encoded message.

        """
        return str(base64.b64encode(message.encode('utf-8')))


    def decode(self, message):
        """
        Decodes a message from Base64.

        Parameters
        ----------
        message : str
            The Base64 encoded message to be decoded.

        Returns
        -------
        str
            The decoded message.

        """
        decoded_bytes = base64.b64decode(message)
        return decoded_bytes.decode('utf-8')

