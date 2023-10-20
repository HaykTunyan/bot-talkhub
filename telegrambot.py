import requests
import datetime  # Import the datetime module

# Your bot's API token
API_TOKEN = "6326634215:AAGrjGCch_X59XzDaXj6FgMO3B9S9Bjggew"

# Define the base URL for the Telegram Bot API
BASE_URL = f"https://api.telegram.org/bot{API_TOKEN}"

# Define a function to send messages
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
    }
    response = requests.post(url, data=data)
    return response.json()

# Define a function to handle incoming messages
def handle_message(update):
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]
    
    if text == "/start":
        send_message(chat_id, "Welcome to the TalkHub Bot. Use /help to see available commands.")
    elif text == "/help":
        help_message = "Available commands:\n" \
                       "/start - Start the bot\n" \
                       "/help - Show available commands\n" \
                       "/meet - Schedule a meeting\n" \
                       "/show - Show something\n" \
                       "/info - Get information\n"  \
                       "/time - Get Your time"
        send_message(chat_id, help_message)
    elif text == "/meet":
        send_message(chat_id, "Let's schedule a meeting! Please provide the details.")
    elif text == "/show":
        send_message(chat_id, "Here is something to show.")
    elif text == "/info":
        send_message(chat_id,
                      " Our bot is constantly learning and improving, so feel free to ask any questions, and we'll do our best to assist you. We are here to help with both simple and complex inquiries."
                      )
    elif text == "/time":
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_message(chat_id, f"Current time: {current_time}")
    else:
        send_message(chat_id, "Error: Invalid command. Use /help to see available commands.")
    

# Define a function to poll for updates
def poll_for_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"offset": offset}
    response = requests.get(url, params=params)
    return response.json()

# Main loop to continuously poll for updates
def main():
    offset = None
    while True:
        updates = poll_for_updates(offset)
        for update in updates.get("result", []):
            handle_message(update)
            offset = update["update_id"] + 1

if __name__ == "__main__":
    main()
