import openai
import os
from places import extract_city, search_places

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(user_query: str, places: list, city: str) -> str:
    places_str = "\n".join(f"- {place}" for place in places) if places else "— ничего не найдено"
    return (
                "Ты тревел-ассистент для digital nomads. "
                "Твоя задача — на основе запроса пользователя давать свежие и персонализированные рекомендации для путешествий в новом городе. "
                "Используй данные о лучших местах для еды, концертах, мероприятиях, культурных локациях, а также учитывай, когда в местах меньше всего туристов. "
                "Пиши кратко, дружелюбно, добавляй полезные инсайты для digital nomads."
                "Если тебя просят составить план на определенной временной промежуток, то расписывай план пошагово. Используй упорядочивание, пункты для списков, чтобы сообщение выглядело красиво."
                f"Город: {city}\n"
                f"Актуальные места:\n{places_str}\n\n"
                f"Запрос пользователя: {user_query}"
            )

def ask_gpt(user_query: str) -> str:
    city = extract_city(user_query)
    places = search_places(city) if city else []
    prompt = build_prompt(user_query, places, city)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

