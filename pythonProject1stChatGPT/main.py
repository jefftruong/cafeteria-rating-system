# This is a sample Python script.
import os
import openai

openai.api_key = "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"
messages = [{"role": "system", "content": "You are a intelligent assistant."}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
