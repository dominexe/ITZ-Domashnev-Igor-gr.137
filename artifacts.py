# Инициализация списков артефактов
def generate_artifact_files():
    start_artifacts = [
    "🥊 Перчатки викинга",
    "🔪 Нож мясника",
    "🛡️ Щит надежды",
    "🗡️ Копьё преследования",
    "🕶️ Очки стиля",
    "🕑 Часы будующего",
    "🆘 Помощь духов ",
    "⚜️ Знак мужества"
    ]

    skelet_artifacts = [
    "🏹 Арбалет огра",
    "⚔️ Клинки тьмы",
    "🧿 Амулет Страданий",
    "🪏 Лопата смерти",
    "💀 Голова брата",
    "💣 Бомба",
    "🪄 Палочка огня"
    ]

    with open("start_gift.txt", "w", encoding="utf-8") as start_file:
        for artifact in start_artifacts:
            start_file.write(artifact + "\n")

    with open("skelet_artefact.txt", "w", encoding="utf-8") as skelet_file:
        for artifact in skelet_artifacts:
            skelet_file.write(artifact + "\n")

    print("Файлы с артефактами успешно созданы.")
generate_artifact_files()
moves_log = []

# Словари для артефактов
start_artifacts = []
skelet_artifacts = []
current_artifact = ""

# Множество для отслеживания посещенных локаций
visited_locations = set()

# Список для хранения всех выигранных артефактов в текущей игре
collected_artifacts = []

# Загрузка артефактов из файлов
def load_artifacts():
    global start_artifacts, skelet_artifacts
    with open("start_gift.txt", "r", encoding="utf-8") as file:
        start_artifacts = [line.strip() for line in file if line.strip()]
    with open("skelet_artefact.txt", "r", encoding="utf-8") as file:
        skelet_artifacts = [line.strip() for line in file if line.strip()]




# Сохранение артефактов в файлы
def save_artifacts():
    with open("start_gift.txt", "w", encoding="utf-8") as file:
        for item in start_artifacts:
            file.write(item + "\n")
    with open("skelet_artefact.txt", "w", encoding="utf-8") as file:
        for item in skelet_artifacts:
            file.write(item + "\n")


# Запись действий
def log_move(description):
    moves_log.append(description)

# выбор артефакта
def choose_artifact():
    global current_artifact
    print("Выберите артефакт:")
    for i, item in enumerate(start_artifacts, 1):
        print(f"{i}. {item}")
    choice = int(input("Введите номер выбранного артефакта: ")) - 1
    current_artifact = start_artifacts[choice]
    collected_artifacts.append(current_artifact)  # Добавляем артефакт в список
    print(f"💎 Вы получаете артефакт: {current_artifact} — 'Древняя сила пробуждается в ваших руках! ⚡'")

def select_skelet_artifact():
    print("Выберите артефакт:")
    for i, item in enumerate(skelet_artifacts, 1):
        print(f"{i}. {item}")
    choice = int(input("Введите номер выбранного артефакта: ")) - 1
    selected_item = skelet_artifacts.pop(choice)
    start_artifacts.append(selected_item)
    collected_artifacts.append(selected_item)  # Добавляем выбранный артефакт в список
    save_artifacts()
    print(f"Вы получили артефакт: {selected_item}! Судьба улыбнулась вам! 😊")



