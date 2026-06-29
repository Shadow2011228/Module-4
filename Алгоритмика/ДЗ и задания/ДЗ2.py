import random
import time



def play_binary_search_game():
    """
    Мини-игра: компьютер угадывает число, которое загадал игрок,
    используя бинарный поиск.
    """
    print("=" * 50)
    print("   Добро пожаловать в игру 'Бинарный поиск'!")
    print("=" * 50)
    print("\nЗагадайте число от 1 до 100.")
    print("Компьютер будет пытаться его угадать.")
    print("Отвечайте: 'больше', 'меньше' или 'угадал'.\n")

    input("Нажмите Enter, когда загадаете число...")

    low = 1
    high = 100
    attempts = 0
    guessed = False

    while not guessed and low <= high:
        # Компьютер предполагает число (середина диапазона)
        guess = (low + high) // 2
        attempts += 1
        history.append(guess)

        print(f"\nПопытка {attempts}: Компьютер называет число {guess}.")
        print(f"Текущий диапазон: [{low}, {high}]")

        # Получаем ответ от игрока
        while True:
            user_input = input("Ваш ответ (больше / меньше / угадал): ").strip().lower()
            if user_input in ("больше", "меньше", "угадал"):
                break
            print("Пожалуйста, введите 'больше', 'меньше' или 'угадал'.")

        # Обрабатываем ответ
        if user_input == "угадал":
            guessed = True
            print(f"\n🎉 Ура! Компьютер угадал ваше число {guess} за {attempts} попыток!")
            print(history)

        elif user_input == "больше":
            low = guess + 1
            if low > high:
                print("\n⚠️ Ошибка: вы сказали 'больше', но диапазон пуст. Возможно, вы ошиблись в ответе.")
                guessed = True  # завершаем игру из-за противоречия
        elif user_input == "меньше":
            high = guess - 1
            if low > high:
                print("\n⚠️ Ошибка: вы сказали 'меньше', но диапазон пуст. Возможно, вы ошиблись в ответе.")
                guessed = True  # завершаем игру из-за противоречия

    if not guessed:
        print("\n😅 Похоже, вы где-то ошиблись в ответах. Давайте начнём заново!")

    print("\nСпасибо за игру!")


def choice_sort(dataset):
    N = len(dataset)
    for a in range(N - 1):
        m = dataset[a]
        p = a
        for b in range(a + 1, N):
            if m > dataset[b]:
                m = dataset[b]
                p = b
        if p != a:
            t = dataset[a]
            dataset[a] = dataset[p]
            dataset[p] = t
    return dataset

def main():
    while True:
        global history
        play_binary_search_game()
        start = time.time()
        history = choice_sort(history)
        print(history)
        play_again = input("\nХотите сыграть ещё раз? (да / нет): ").strip().lower()
        if play_again != "да":
            print("До свидания! 👋")
            break
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    history = []
    main()

