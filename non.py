from Engine import LLMEngine

if __name__ == "__main__":
    llm = LLMEngine()

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")

        messages.append({"role": "user", "content": user_input})

        reply = llm.generate(messages)

        print("Bot:", reply)

        messages.append({"role": "assistant", "content": reply})