import re
import requests
from bs4 import BeautifulSoup
import csv


def get_animals_count():
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = {}

    while base_url:
        response = requests.get(base_url)
        if response.status_code != 200:
            raise Exception(f"Ошибка загрузки страницы: {base_url}")

        soup = BeautifulSoup(response.text, "html.parser")

        # Найти все ссылки на животных
        animals = soup.select(".mw-category-group ul li a")
        for animal in animals:
            if animal.text.strip():
                text = animal.text.strip()
                if re.match(r"^[А-Яа-яЁё]", text):
                    first_letter = text[0].upper()
                    letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

        next_page = soup.select_one("a:-soup-contains('Следующая страница')")
        base_url = "https://ru.wikipedia.org" + next_page["href"] if next_page else None

    return letter_counts


def save_to_csv(letter_counts, filename="beasts.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for letter, count in sorted(letter_counts.items()):
            writer.writerow([letter, count])


if __name__ == "__main__":
    print("Начинаем сбор данных...")
    letter_counts = get_animals_count()
    print("Спарсили. Сохраняем CSV...")
    save_to_csv(letter_counts)
    print("Done!")
