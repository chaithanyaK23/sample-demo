#Player Score Calculator
player_name = input("Enter the player name:")
no_of_games = int(input("Enter number of games played:"))
total_score = int(input("Enter total score achieved: "))
avg_score = total_score / no_of_games
print(f"Player: {player_name}")
print(f"Games Played: {no_of_games}")
print(f"Total Score: {total_score}")
print(f"Average Score: {avg_score}")

'''
#Output sample from above code
Enter the player name:Sachin Tendulkar
Enter number of games played:25
Enter total score achieved: 1540
Player: Sachin Tendulkar
Games Played: 25
Total Score: 1540
Average Score: 61.6
'''