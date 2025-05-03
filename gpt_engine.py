import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_messages(user_query: str):
    return [
        {
            "role": "system",
            "content": (
                "Ты тревел-ассистент для digital nomads. "
                "Твоя задача — на основе запроса пользователя давать свежие и персонализированные рекомендации для путешествий в новом городе. "
                "Используй данные о лучших местах для еды, концертах, мероприятиях, культурных локациях, а также учитывай, когда в местах меньше всего туристов. "
                "Пиши кратко, дружелюбно, добавляй полезные инсайты для digital nomads."
                "Если тебя просят составить план на определенной временной промежуток, что расписывай план пошагово. Используй упорядочивание, пункты для списков, чтобы сообщение выглядело красиво."
            )
        },
        {"role": "user", "content": user_query}
    ]

def ask_gpt(user_query: str) -> str:
    messages = build_messages(user_query)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()

