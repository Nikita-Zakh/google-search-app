import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Загружаем переменные из .env
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

if not api_key:
    print("Ошибка: ключ SerpAPI не найден!")
    exit()

print("Ключ найден:", api_key[:5] + "...")

# Параметры запроса
params = {
    "q": "электрокар 2026",  # ключевое слово
    "engine": "google",
    "api_key": api_key,
    "num": 5,       # количество результатов
    "hl": "cs",     # язык поиска (можно "ru")
    "gl": "cz"      # регион поиска
}

# Выполняем поиск
search = GoogleSearch(params)
results = search.get_dict()

# Выводим результаты
organic = results.get("organic_results")
if organic:
    print("Найдено результатов:", len(organic))
    for i, r in enumerate(organic, 1):
        print(f"{i}. {r.get('title')} — {r.get('link')}")
else:
    print("Что-то пошло не так, результатов нет")
    print("Полный ответ API:", results)