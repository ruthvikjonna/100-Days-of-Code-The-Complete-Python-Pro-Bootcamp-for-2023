import random
import os
from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""

score = 0
correct = False
wrong = False
start_celeb = True

while wrong == False:
    print(logo)
    print("Last updated June 21, 2022.\n")
    if correct == True:
        print(f"\nYou're right! Current Score: {score}")
    print("\nWhich celebrity has more Instagram followers?")

    # Celebrity A Details
    if start_celeb == True:
        celeb_A = random.choice(data)
        data.remove(celeb_A)

    celeb_A_name = celeb_A["name"]
    celeb_A_description = celeb_A["description"]
    celeb_A_country = celeb_A["country"]
    celeb_A_follower_count = celeb_A["follower_count"]

    string_A = (f"\nCelebrity A - {celeb_A_name}, a {celeb_A_description}, from {celeb_A_country} has {celeb_A_follower_count}M Instagram followers.")
    print(string_A)

    # VS. Logo
    print(vs)

    # Celebtrity B Details
    if start_celeb == True:
        celeb_B = random.choice(data)
        data.remove(celeb_B)

    celeb_B_name = celeb_B["name"]
    celeb_B_description = celeb_B["description"]
    celeb_B_country = celeb_B["country"]
    celeb_B_follower_count = celeb_B["follower_count"]

    string_B = (f"Celebrity B - {celeb_B_name}, a {celeb_B_description}, from {celeb_B_country}.")
    print(string_B)

    answer = input("\nDoes Celebrity B have a higher or lower Instagram follower count? Type 'higher' or 'lower': ")

    if answer == "lower" and celeb_A_follower_count > celeb_B_follower_count:
        os.system('cls')
        score += 1
        correct = True
        start_celeb = False
        if len(data) < 2: 
            break
        celeb_A = celeb_B
        celeb_B = random.choice(data)
        data.remove(celeb_B)
    elif answer == "higher" and celeb_A_follower_count < celeb_B_follower_count:
        os.system('cls')
        score += 1
        correct = True
        start_celeb = False
        if len(data) < 2: 
            break
        celeb_A = celeb_B
        celeb_B = random.choice(data)
        data.remove(celeb_B)
    elif answer == "lower" and celeb_A_follower_count < celeb_B_follower_count:
        os.system('cls')
        print(logo)
        print(f"\nSorry, that's incorrect. Final Score: {score}")
        wrong = True
    elif answer == "higher" and celeb_A_follower_count > celeb_B_follower_count:
        os.system('cls')
        print(logo)
        print(f"\nSorry, that's incorrect. Final Score: {score}")
        wrong = True
    else:
        break

if score == 48:
    print(logo)
    print("Last updated June 21, 2022.\n")
    print("Congratulations! You Won!")