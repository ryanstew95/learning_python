import random

# Function to roll dice and remove 2s and 5s
def roll_dice(dice_count):
    roll = [random.randint(1, 6) for _ in range(dice_count)]
    # Keep only dice that are not 2 or 5
    remaining_dice = [die for die in roll if die != 2 and die != 5]
    return roll, remaining_dice

# Function for each player's turn
def player_turn(player_name):
    score = 0
    dice_count = 5  # Start with 5 dice

    print(f"\n{player_name}'s turn begins.")
    
    while dice_count > 0:
        # Ask player if they want to roll the dice
        roll_choice = input("Roll the dice (y/n)? ").strip().lower()
        
        if roll_choice == 'n':
            print(f"{player_name} decides to keep their score of {score}.")
            break

        roll, remaining_dice = roll_dice(dice_count)
        print(f"{player_name} rolled: {roll}")
        
        # If no 2s or 5s, add remaining dice sum to score
        if len(remaining_dice) == dice_count:
            roll_score = sum(remaining_dice)
            score += roll_score
            print(f"No 2s or 5s rolled. Adding {roll_score} to score.")
        else:
            print(f"Removing 2s and 5s: {remaining_dice}")
        
        # Update the number of dice left to roll
        dice_count = len(remaining_dice)
        
        # If no dice left to roll, end turn
        if dice_count == 0:
            print(f"{player_name} has no dice left to roll. Turn ends.")
            break
        
    print(f"{player_name}'s turn ends with a score of {score}.\n")
    return score

# Main game function
def drop_dead_game():
    # Set up players
    num_players = int(input("Enter the number of players (2-8): "))
    while num_players < 2 or num_players > 8:
        num_players = int(input("Please enter a valid number of players (2-8): "))
    
    players = [input(f"Enter name for player {i+1}: ") for i in range(num_players)]
    scores = {player: 0 for player in players}
    
    # Each player takes their turn
    for player in players:
        scores[player] = player_turn(player)
    
    # Determine the winner
    winner = max(scores, key=scores.get)
    print("Game over!")
    for player, score in scores.items():
        print(f"{player} scored {score}")
    print(f"The winner is {winner} with a score of {scores[winner]}!")
    
# Run the game
drop_dead_game()
