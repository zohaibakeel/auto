import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API credentials from environment variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# Define the services message to be sent
services_message = (
    "Hello! Thank you for reaching out. Here are the services we offer:\n\n"
    "1. Service 1\n"
    "2. Service 2\n"
    "3. Service 3\n\n"
    "Feel free to ask if you have any questions!"
)

# Create a client instance
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

# Dictionary to store users that have received the message
user_message_sent = {}

@app.on_message(filters.private & filters.text)
def auto_reply(client: Client, message: Message):
    """Send a services message to new users only once."""
    user_id = message.chat.id

    if user_id not in user_message_sent:
        try:
            # Send the services message
            client.send_message(chat_id=user_id, text=services_message)
            
            # Mark the user as having received the message
            user_message_sent[user_id] = True
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")

# Start the client
app.run()
