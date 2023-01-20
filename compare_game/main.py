#get data from game_data.py


import random
from game_data import data
from art import logo, vs
#introduce score

#randomly choose data from game_data.py


print(logo)
def game():
    score = 0
    
    #pick random data from game_data.py
    choice_a= random.choice(data)
    choice_b= random.choice(data)
    #print choice_a
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    #print choice_b
    print(f"against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")


    
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    

    if user_input == "a":
        if choice_a["follower_count"] > choice_b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            game()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
    elif user_input == "b":
        if choice_b["follower_count"] > choice_a["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            game()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print("Invalid input. Please try again.")
        game()


           
    


game()