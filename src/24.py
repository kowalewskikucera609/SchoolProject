import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    print("Let's play rock-paper-scissors!")
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if player_choice not in choices:
        print(f"Invalid choice. Please enter either 'rock', 'paper' or 'scissors'.")
        return
    
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game()
