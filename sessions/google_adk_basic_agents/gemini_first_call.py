import os
from google import genai

# Gemini Python SDK 

client = genai.Client(
    api_key="<your key>",
)

generation_config = {
    'max_output_tokens': 65536,
    'thinking_level': 'low',
}


history = []

while True:
    user_input = input("Enter your text (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    history.append(f"User: {user_input}")

    interaction = client.interactions.create(
        model='models/gemini-3.5-flash',
        input="\n".join(history),
        system_instruction='You are a helpful assistant.',
        generation_config=generation_config,
    )

    history.append(f"Assistant: {interaction.output_text}")
    print(f"Assistant: {interaction.output_text}")


