# Define a function that responds to a user's message:
def respond(message):
  # If the message is a greeting, respond with a greeting:
  if message in ['hi', 'hello', 'hey', 'hola']:
    return 'Hello there!'
  # If the message is a question, respond with a question:
  elif message.endswith('?'):
    return 'That is a good question. I am not sure.'
  # Otherwise, respond with a default message:
  else:
    return 'I am a simple chat bot. I do not have much to say.'

# Define a function that prints the conversation between the user and the bot:
def have_a_conversation():
  # Print a welcome message:
  print('Hi, I am a simple chat bot. What is your name?')
  
  # Ask the user for their name:
  user_name = input()
  
  # Respond to the user's name:
  print('Nice to meet you, ' + user_name + '. What can I do for you?')
  
  # Keep track of the conversation:
  conversation = []
  
  # Start the conversation loop:
  while True:
    # Ask the user for a message:
    message = input()
    
    # If the user enters a blank message, end the conversation:
    if message == '':
      break
    
    # Add the user's message to the conversation:
    conversation.append(user_name + ': ' + message)
    
    # Get the bot's response to the user's message:
    response = respond(message)
    
    # Add the bot's response to the conversation:
    conversation.append('Bot: ' + response)
    
  # Print the entire conversation:
  print('\nConversation:\n')
  for message in conversation:
    print(message)

# Start the conversation:
have_a_conversation()