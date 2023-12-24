import random 

# This function is used to Roll the Dice in a random way !!
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    player = input("Enter the Number of Players(2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between 2-4")
    else:
        print("Invalid Statment, Try Again!!")

max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:
    for player_turn in range(player):
        print("\nPlayer",player_turn + 1,"has just started!!\n")
        current_score = 0   
        while True:
            should_roll = input("Would you like to roll (Y)? ")
            if should_roll.lower() !=  "y":
                break
            else:
                value = roll()
                if value == 1:
                    print("You rolled a 1!! Turn Done!! ")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You Rolled a:",value)
                print("You Current Score is:",current_score)
        player_score[player_turn] += current_score
        print("Your Total Score is", player_score[player_turn])


