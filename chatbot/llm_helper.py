import os

from dotenv import load_dotenv


load_dotenv()


class LLMHelper:
    def __init__(self):
        self.enabled = bool(os.getenv("OPENAI_API_KEY"))
        self.client = None

        if self.enabled:
            from openai import OpenAI

            self.client = OpenAI()

    def generate_response(self, message, entities=None):
        if not self.enabled or self.client is None:
            return None

        entity_text = entities or {}
        system_prompt = (
            "You are an AI internship project chatbot. Answer clearly and briefly. "
            "Help with FAQs, simple conversation, AI, NLP, deep learning, Flask, "
            "project explanation, viva questions, resume guidance, and chatbot architecture. "
            "If the user asks outside the project scope, politely guide them back to the project."
        )

        completion = self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"User message: {message}\nExtracted entities: {entity_text}",
                },
            ],
            temperature=0.4,
            max_tokens=180,
        )

        return completion.choices[0].message.content.strip()
