from collections import defaultdict
from time import perf_counter


def load_data(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file]


def can_assembled(source_word: str, target_word: str) -> bool:
    if len(source_word) < len(target_word):
        return False

    if set(target_word) - set(source_word):
        return False

    letter_count = defaultdict(int)
    for letter in source_word:
        letter_count[letter] += 1

    for char in target_word:
        if letter_count[char] <= 0:
            return False
        letter_count[char] -= 1

    return True


def main():

    PATH = "nouns.txt"
    WORDS = ["обороноспособность", "агат", "метель", "превысокомногорассмотрительствующий"]
    WORDS = list(map(lambda x: x.lower(), WORDS))

    try:
        start_load = perf_counter()
        data = load_data(PATH)
        print(f"Данные загружены за {perf_counter() - start_load}\n")
    except FileNotFoundError:
        print("Файл не найден")
        return

    for WORD in WORDS:
        start = perf_counter()
        match_words = [i for i in data if can_assembled(WORD, i)]
        print("Время поиска:", perf_counter() - start)

        print("Количество слов:", len(match_words))
        print(*sorted(match_words, key=len, reverse=True))
        print(f"Полное время: {perf_counter() - start}\n")


if __name__ == "__main__":
    main()
