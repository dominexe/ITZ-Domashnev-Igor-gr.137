import artifacts
import game
import skelet
import path1
import path2
import path3


#Запуск всей игры и ее остановка
def main():
    artifacts.load_artifacts()
    while True:
        global moves_log
        moves_log = []
        if not artifacts.start_artifacts:
            print("💀 Все артефакты у скелета. Игра завершена. 😭")
            break
        play_choice = game.get_valid_input("Хотите сыграть? (да/нет): ", ["да", "нет"])
        if play_choice == "да":
            game.start_game()
            replay = game.get_valid_input("Сыграть снова? (да/нет): ", ["да", "нет"])
            if replay != "да":
                break
        else:
            break
    artifacts.save_artifacts()
    print("Спасибо за игру!")

if __name__ == "__main__":
    main()