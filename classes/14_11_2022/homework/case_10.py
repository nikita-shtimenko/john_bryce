GAME_OBJECTS = ["rock", "scissors", "paper"]

first_player_wins_count = 0
first_players_loss_count = 0

second_player_wins_count = 0
second_player_loss_count = 0

draw_count = 0
rounds_count = 1

while True:
    print("- New round started.")
    print(f"Round number: {rounds_count}\n")

    is_round_finished = False
    winner = -1

    first_player_choise = input("[First player] Enter your choise: ")

    if first_player_choise not in GAME_OBJECTS:
        print("[First player] Error: invalid input.")
        print("Restart...")
        continue

    second_player_choise = input("[Second player] Enter your choise: ")

    if second_player_choise not in GAME_OBJECTS:
        print("[Second player] Error: invalid input.")
        print("Restart...")
        continue

    if first_player_choise == second_player_choise:
        draw_count += 1

    elif first_player_choise == GAME_OBJECTS[0]:
        winner = 1 if second_player_choise == GAME_OBJECTS[1] else 2

    elif first_player_choise == GAME_OBJECTS[1]:
        winner = 1 if second_player_choise == GAME_OBJECTS[2] else 2

    elif first_player_choise == GAME_OBJECTS[2]:
        winner = 1 if second_player_choise == GAME_OBJECTS[0] else 2

    print(f"""
        - First player: {first_player_choise}
        - Second player: {second_player_choise}
        """)

    if winner == 1:
        first_player_wins_count += 1
        second_player_loss_count += 1
        print("Result: First player wins! Congratulations!")

    elif winner == 2:
        second_player_wins_count += 1
        first_players_loss_count += 1
        print("Result: Second player wins! Congratulations!")

    else:
        print("Result: Draw! Congratulations!")
    
    rounds_count += 1
    restart = None

    while True:
        restart = input("Would you like to play one more round? (yes/no): ").capitalize()

        if restart not in ["Yes", "No"]:
            print("Error: invalid input. Please, type 'yes' or 'no'.")
            continue

        break

    if restart == "Yes":
        print("Nice to hear! Starting next round...\n")
        continue

    else:
        print("\nEnd of game...\n")
        print(f"""
            Game stats:

            - Rounds played: {rounds_count}

            | Wins
                - First player: {first_player_wins_count}
                - Second player: {second_player_wins_count}
            
            | Losses
                - First player: {first_players_loss_count}
                - Second player: {second_player_loss_count}

            - Draws count: {draw_count}
            """)

        break