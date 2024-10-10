# Stack for storing sent messages
sent_messages = []

# Queue for receiving messages
received_messages = []

# List to display chat history
chat_history = []

def send_message(message):
    sent_messages.append(message)  # Push to stack
    chat_history.append(("sent", message))  # Add to chat history

def receive_message(message):
    received_messages.append(message)  # Enqueue
    chat_history.append(("received", message))  # Add to chat history

def get_next_received_message():
    if received_messages:
        return received_messages.pop(0)  # Dequeue
    return None

def display_chat_history():
    for message_type, message in chat_history:
        print(f"{message_type.capitalize()}: {message}")

# Example usage
send_message("Hello!")
receive_message("Hi there!")
send_message("How are you?")
receive_message("I'm good, thanks!")

print("Chat History:")
display_chat_history()

print("\nSent Messages Stack:")
print(sent_messages)

print("\nReceived Messages Queue:")
print(received_messages)

# Process received messages
print("\nProcessing received messages:")
while True:
    message = get_next_received_message()
    if message is None:
        break
    print(f"Processing: {message}")

print("\nReceived Messages Queue after processing:")
print(received_messages)