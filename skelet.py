import random
import artifacts
import game

#Игра со скелетом, есть 2 испытания:
# 1 - Камень ✊, ножницы 🖖, бумага 🤚
# 2 - Броски кости
def skelet_game():
    artifacts.visited_locations.add("Встреча со скелетом")
    print("💀 Скелет преграждает вам путь и заставляет сыграть с ним в игру. Победите — получите артефакт, проиграете — он заберет ваш. 🕯️")
    print("Скелет ставит перед нами выбор: 1 или 2")
    choice = game.get_valid_input("Введите '1' или '2': ", ["1", "2"])
    artifacts.log_move(f"Выбор испытания скелета: {choice}")

    if choice == "1":
        print("☠️ Скелет бросает вам вызов в 'Камень ✊, ножницы 🖖, бумага 🤚'")
        choices = ["камень", "ножницы", "бумага"]
        skelet_won = False
        while True:
            user_choice = game.get_valid_input("Ваш выбор (камень/ножницы/бумага): ", choices)
            skeleton_choice = choices[random.randint(0, 2)]
            print("Скелет выбрал:", skeleton_choice)
            artifacts.log_move(f"Игрок: {user_choice}, Скелет: {skeleton_choice}")

            if user_choice == skeleton_choice:
                print("Ничья. Еще раз!")
            elif (user_choice == "камень" and skeleton_choice == "ножницы") or \
                    (user_choice == "ножницы" and skeleton_choice == "бумага") or \
                    (user_choice == "бумага" and skeleton_choice == "камень"):
                print("🎉 Вы победили скелета! 🏅")
                artifacts.select_skelet_artifact()
                game.end_game("ВЫ ПОБЕДИЛИ СКЕЛЕТА!")
                break
            else:
                print("💀 Скелет победил вас и забрал ваш артефакт! 🎁")
                artifacts.start_artifacts.remove(artifacts.current_artifact)
                artifacts.save_artifacts()
                game.end_game("Рука скелета умнее вас...")
                skelet_won = True
                break
        if not skelet_won:
            artifacts.save_artifacts()

    if choice == "2":
        print("""Скелет предлагает бросить кости: есть шестигранная кость
Цель — в сумме набрать больше очков, чем оппонент, но не более 12. Если перебрал — мгновенно проигрываешь.
Механика:
1.Участники бросают кость по очереди.
2.После каждого броска решают, бросать ли следующую кость или остановиться.
3.Можно остановиться на любом количестве бросков (от 1 до 3).
4.После того как оба остановились, сравниваются итоговые суммы.
        """)
        player_score = 0
        npc_score = 0
        player_rolls = 0
        npc_rolls = 0
        # Игрок ходит первым
        print("Игра началась, ход за вами")
        player_stopped = False

        while player_rolls < 3 and not player_stopped:
            if player_rolls < 3:
                print("Бросить кость?")
                choice = game.get_valid_input("Введите 'да' или 'нет': ", ["да", "нет"])

                if choice == "да":
                    roll = random.randint(1, 6)
                    player_score += roll
                    player_rolls += 1

                    print(f"\nВы бросаете кость... Выпало: {roll}")
                    print(f"Ваша сумма: {player_score}")

                    if player_score > 12:
                        print(f"ПЕРЕБОР! {player_score} > 12")
                        print("Вы проиграли...")
                        game.end_game("Жадность фраера сгубила...")
                        return

                else:
                    player_stopped = True
                    print(f"Вы останавливаетесь на сумме: {player_score}")

        print(f"Итог вашего раунда: {player_score} очков ({player_rolls} бросков)")


        # Ход NPC
        print("---Ход Скелета---")
        while npc_rolls < 3:
            if npc_rolls < 2:
                roll = random.randint(1, 6)
                npc_score += roll
                npc_rolls += 1

                print(f"\nСкелет бросает кость... Выпало: {roll}")
                print(f"Его сумма: {npc_score}")

                if npc_score > 12:
                    print(f"ПЕРЕБОР! {npc_score} > 12")
                    print("Вы победили")
                    game.end_game("Жадность скелета погубила!")
                    return

            else:
                choice  = random.randint(1, 2)
                if choice == 1:
                    roll = random.randint(1, 6)
                    npc_score += roll
                    npc_rolls += 1

                    print(f"\nСкелет бросает кость... Выпало: {roll}")
                    print(f"Его сумма: {npc_score}")

                    if npc_score > 12:
                        print(f"ПЕРЕБОР! {npc_score} > 12")
                        print("Вы победили")
                        game.end_game("Жадность скелета погубила!")
                        break
                else:
                    npc_stopped = True
                    print(f"Скелет останавливается на сумме: {npc_score}")

        artifacts.log_move(f"Игрок: {player_score}, Скелет: {npc_score}")

        if npc_score > player_score and npc_score <= 12 :
            print("💀 Скелет победил вас и забрал ваш артефакт! 🎁")
            artifacts.skelet_artifacts.append(artifacts.current_artifact)
            artifacts.start_artifacts.remove(artifacts.current_artifact)
            artifacts.save_artifacts()
            game.end_game("Удача не на вашей стороне...")
        else:
            print("🎉 Вы победили скелета! 🏅")
            artifacts.select_skelet_artifact()
            artifacts.save_artifacts()
            game.end_game("ВЫ ПОБЕДИЛИ СКЕЛЕТА!")






