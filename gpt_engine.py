import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(user_query: str) -> str:
    return (
        "Ты тревел-ассистент для digital nomads. "
        "Твоя задача — на основе запроса пользователя давать свежие и персонализированные рекомендации для путешествий в новом городе. "
        "Используй данные о лучших местах для еды, концертах, мероприятиях, культурных локациях, а также учитывай, когда в местах меньше всего туристов. "
        "Пиши кратко, дружелюбно, добавляй полезные инсайты для digital nomads.\n\n"
        f"Запрос пользователя: {user_query}"
    )

def ask_gpt(user_query: str) -> str:
    prompt = build_prompt(user_query)
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # или другой поддерживаемый модуль
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()
