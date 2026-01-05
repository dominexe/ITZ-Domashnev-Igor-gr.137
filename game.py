import artifacts
import path1
import path2
import path3

# Вывод итогов игры
def end_game(outcome):
    artifacts.log_move(f"Итог: {outcome}")
    print(f"Концовка: {outcome}")
    print(f"🌿 Посещенные локации: {', '.join(artifacts.visited_locations)}")
    print(f"🎁 Собранные артефакты: {', '.join(artifacts.collected_artifacts)}")
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write("--- Новая игра ---\n")
        for entry in artifacts.moves_log:
            file.write(f"{entry}\n")
        file.write(f"Результат: {outcome}\n")

def get_valid_input(prompt, valid_options):
    """Запрашивает ввод у пользователя до тех пор, пока не будет введен допустимый вариант."""
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        else:
            print("❗ Неверный ввод. Пожалуйста, выберите один из допустимых вариантов.")

#запуск игры
def start_game():
    artifacts.visited_locations.clear()
    artifacts.collected_artifacts.clear()
    artifacts.log_move("--Начало игры--")
    print("🌳 Приветствую вас в нашем темном и неизведанном лесу!🌳")
    artifacts.choose_artifact()
    artifacts.visited_locations.add("Перекресток Змея Горыныча")
    print("""Перед тобой стою я - Змей Горыныч, а именно мои головы - Эдик, Вася и Миша
Если хочешь пройти дальше, то тебе нужно выбрать испытание одной из моих голов:
1 - Испытание Эдика\n2 - Испытание Васи\n3 - Испытание Миши
    """)
    choice1 = get_valid_input("Введите '1' или '2' или '3': ", ["1", "2", "3"])
    artifacts.log_move(f"Выбор испытания горыныча: {choice1}")

    if choice1 == "1":
        path1.zamok_game()
    if choice1 == "2":
        path2.starec_game()
    if choice1 == "3":
        path3.yaga_game()



