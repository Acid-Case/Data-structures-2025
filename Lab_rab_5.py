from collections import Counter
from time import perf_counter
from re import findall


def load_data(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = findall(r'\b[а-яё]+\b', text)
        return words


def main():

    print("======================================")
    print("Выполнил: Борисов Данила Александрович")
    print("Группа:   090304-РПИа-o24")
    print("======================================")

    WORD = "мир".lower()
    PATH = "Война и мир.txt"

    try:
        start_load = perf_counter()
        data = load_data(PATH)
        print(f"Данные загружены за {perf_counter() - start_load}\n")
    except FileNotFoundError:
        print("Файл не найден")
        return

    start = perf_counter()
    data = Counter((w for w in data if w.startswith(WORD)))

    for w, n in data.most_common(20):
        print(w, n)
    print(f"\nПоиск и вывод завершен за {perf_counter() - start}")


if __name__ == "__main__":
    main()
