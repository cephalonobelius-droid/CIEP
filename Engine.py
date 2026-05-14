from ollama import chat


class LLMEngine:
    def __init__(
        self,
        model_name="llama3.2:3B",
        temperature=0.4,
        top_p=0.9,
        repetition_penalty=1.5,
        max_tokens=128,
    ):
        self.model_name = model_name
        self.options = {
            "temperature": temperature,
            "top_p": top_p,
            "repeat_penalty": repetition_penalty,
            "num_predict": max_tokens,
        }

    def generate(self, messages):
        response = chat(
            model=self.model_name,
            messages=messages,
            options=self.options,
        )

        return response["message"]["content"]



