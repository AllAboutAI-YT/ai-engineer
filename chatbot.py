import openai

# Initialize the OpenAI API
openai.api_key = "YOUR API KEY"

# Initialize the conversation list
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]

# Function to interact with GPT-3
def chat_with_gpt3(prompt, conversation):
    model_engine = "gpt-3.5-turbo"
    
    # Add the new user message to the conversation list
    conversation.append({"role": "user", "content": prompt})
    
    # Generate a message from the model
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=conversation
    )
    
    message_output = response['choices'][0]['message']['content']
    
    # Add the model's message to the conversation list
    conversation.append({"role": "assistant", "content": message_output})
    
    return message_output

# Main chat loop
if __name__ == "__main__":
    print("Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            bot_response = chat_with_gpt3(user_input, conversation)
            print(f"Chatbot: {bot_response}")
