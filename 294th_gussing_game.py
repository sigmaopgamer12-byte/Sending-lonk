import json
import random
import sys
import os
def game():
    print("Please sign in or log in")
    print("1) Sign in")
    print("2) Log in")
    print("3) Exit")
def user_choice():
    while True:
        user = input("Enter your choice betwen 1 - 3: ")
        if(user == "1" or user == "2" or user == "3"):
            return user
            break
def exit(user):
    if(user == "3"):
        print("Thanks for playing")
        sys.exit()
def sign_in(user):
    if(user == "1"):
        username = input("Create a username: ")
        if "premium" in username:
            print("Invalid")
            sys.exit()
        password = input("Create a password: ")
        with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
            print("Account successfully created")
            data = {"Wins": 0, "Loses":  0}
        with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
            json.dump(data, file, indent = 4)
            sys.exit()
def log_in(user):
    if(user == "2"):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                print("Successfully logged in")
                return username, password
        except:
             print("Incorrect username or password")
             sys.exit()

def game_score():
    print("Choose one of the options below")
    print("1) Scores")
    print("2) Play")
    print("3) Score comparison")
    print("4) Buy premium")
    print("5) Leaderboard")
    while True:
        try:
            user_s_p = input("Enter your choice: ")
        except:
             print("Invalid")
        if(user_s_p == "1" or user_s_p == "2" or user_s_p == "3" or user_s_p == "4" or user_s_p == "5"):
            
            break
    return user_s_p
def leaderboard(user_s_p):
    if(user_s_p == "5"):
        leaderboard1 = []
        for filename in os.listdir("/storage/emulated/0/Python learning/things made by Siddharth/game"):
            if filename.endswith('.txt'):
                file_path = os.path.join("/storage/emulated/0/Python learning/things made by Siddharth/game", filename)
                with open(file_path, "r") as file:
                    data = json.load(file)
                    wins = data.get("Wins", 0)
                    loses = data.get("Loses", 0)
                    leaderboard1.append({
                    "name": filename,
                    "Wins": wins,
                    "Loses": loses})
    leaderboard1.sort(key = lambda x: x["Wins"], reverse = True)
    print("\n.........leaderboard..........")
    for entry in leaderboard1:
        print(f"{entry['name']}: {entry['Wins']} wins")
def scores(user_s_p, username, password):
    if(user_s_p == "1"):
        print("Showing scores.......")
        with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
            data = json.load(file)
            print("Your wins are:", data["Wins"])
            print("Your loses are:", data["Loses"])
            sys.exit()
def buy_premium(user_s_p, username, password):
    if(user_s_p == "4"):
        print("The cost of premium is 20 wins")
        print("Premium will give you one hint in every match")
        print("Want to buy premium?")
        print("Your wins will be rested after premium and loses too")
        print("1) Yes")
        print("2) No")
        while True:
            try:
                premium = input("Enter your choice: ")
                if(premium == "1"):
                    with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                        data = json.load(file)
                        if(data["Wins"] >= 20):
                            print("Successfully premium bought")
                            os.remove(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt")
                            print(f"Now your username is changed from {username} to premium_{username}")
                            print("For logging please enter this username")
                            with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/premium_{username}_{password}.txt", "w") as file:
                                data = {"Wins": 0, "Loses": 0}
                                json.dump(data, file, indent = 4)
                                break
                                sys.exit()
                        else:
                            print("Not enough wins")
                            sys.exit()
                else:
                    print("Ok bye")
                    sys.exit()
            except:
              sys.exit()
def scores_comparison(user_s_p):
    if(user_s_p == "3"):
        print("Welcome to scores comparison")
        print("For comparison u need to know both player username and password and for checking without it please go to leaderboard")
        player1_username = input("Enter first player username for comparison: ")
        player1_password = input("Enter first player password for comparison: ")
        player2_username = input("Enter second player username for comparison: ")
        player2_password = input ("Enter second player password for comparison: ")
        try:
            with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{player1_username}_{player1_password}.txt", "r") as file:
                data = json.load(file)
                print("First player wins:", data["Wins"])
                print("First player loses:", data["Loses"])
        except:
            print("No such username or password")
            sys.exit()
        try:
            with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{player2_username}_{player2_password}.txt", "r") as file:
                data2 = json.load(file)
                print("Second player wins:", data2["Wins"])
                print("Second player loses:", data2["Loses"])
                
        except:
             print("No such username or password in second player")
             sys.exit()
             
        sys.exit()
def game_choice(user_s_p):
    if(user_s_p == "2"):
        print("Choose one of the options below: ")
        print("1) Pass and play")
        print("2) Robot VS")
        print("3) Exit")

def game_user_choice(user_s_p):
    if(user_s_p == "2"):
        while True:
            user = input("Enter your choice: ")
            if(user == "1" or user == "2" or user == "3"):
                return user
                break
def exit(user_choice):
    if(user_choice == "3"):
        print("Thanks for playing")
def difficulty(user_s_p):
    if(user_s_p == "2"):
        print("Choose one of the difficulty")
        print("1) Easy")
        print("2) Hard")
def difficulty_choice(user_s_p):
    if(user_s_p == "2"):
        while True:
            difficulty_user_choice = input("Enter your choice: ")
            if(difficulty_user_choice == "1" or difficulty_user_choice == "2"):
                return difficulty_user_choice
                break

def robotvs_easy(username, password, user_choice, difficulty_user_choice):
  if(user_choice == "2" and difficulty_user_choice == "1" ):
      print("You will be playing against a easy level robot having 20 number")
      attempt = 10
      computer = random.randint(1, 20)
      premium_comp1 = random.randint(1, 20)
      premium_comp2 = random.randint(1, 20)
      premium_comp3 = random.randint(1, 20)
      premium_comp4 = random.randint(1, 20)
      print(computer)
      my_comp = [computer, premium_comp1, premium_comp2, premium_comp3, premium_comp4]
      while True:
          try:
              print(f"Attempt left #{attempt}")
              user_guess = int(input("Enter your choice between 1 - 20: "))
              if(attempt == 2):
                  if "premium" in username:
                      premium_user = input("Type 'hint' for hint and for continuing without hint type anything: ").capitalize()
                      if(premium_user == "Hint"):
                          print("One of them is correct")
                          random.shuffle(my_comp)
                          print(my_comp)
              attempt -= 1
              if(user_guess == computer):
                  print("You guessed right\nYou won")
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                      data = json.load(file)
                      data["Wins"] += 1
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
                      json.dump(data, file, indent = 4)
                      break
                      sys.exit()
              else:
                  print("Try again")
                  
              if(attempt == 0):
                  print("You lost")
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file1:
                      data1 = json.load(file1)
                      data1["Loses"] += 1
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file1:
                      json.dump(data1, file1, indent = 4)
                      break
                      sys.exit()
                      
          except:
              print("Please enter number between 1 - 20")
def robotvs_hard(username, password, user_choice, difficulty_user_choice):
   if(user_choice == "2" and difficulty_user_choice == "2" ):
      print("You will be playing against a easy level robot having 40 number")
      attempt = 10
      computer = random.randint(1, 40)
      premium_comp1 = random.randint(1, 40)
      premium_comp2 = random.randint(1, 40)
      premium_comp3 = random.randint(1, 40)
      premium_comp4 = random.randint(1, 40)
      print(computer)
      my_comp = [computer, premium_comp1, premium_comp2, premium_comp3, premium_comp4]
      while True:
          try:
              print(f"Attempt left #{attempt}")
              user_guess = int(input("Enter your choice between 1 - 40: "))
              if(attempt == 2):
                  if "premium" in username:
                      premium_user = input("Type 'hint' for hint and for continuing without hint type anything: ").capitalize()
                      if(premium_user == "Hint"):
                          print("One of them is correct")
                          random.shuffle(my_comp)
                          print(my_comp)
              attempt -= 1
              if(user_guess == computer):
                  print("You guessed right\nYou won")
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                      data = json.load(file)
                      data["Wins"] += 1
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
                      json.dump(data, file, indent = 4)
                      break
                      sys.exit()
                  
              else:
                  print("Try again")
              if(attempt == 0):
                  print("You lost")
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file1:
                      data1 = json.load(file1)
                      data1["Loses"] += 1
                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file1:
                      json.dump(data1, file1, indent = 4)
                      break
                      sys.exit()
          except:
              print("Please enter number between 1 - 40")
def passnplay_easy(username, password, user_choice, difficulty_user_choice):
  if(user_choice == "1" and difficulty_user_choice == "1"):
      print("First please choose who is gonna be guessing and who is gonna pick that number who other is guessing")
      print(".......................")
      user_guess = int(input("So make other player close his eye and another one please the enter the number: "))
      premium_comp1 = random.randint(1, 20)
      premium_comp2 = random.randint(1, 20)
      premium_comp3 = random.randint(1, 20)
      premium_comp4 = random.randint(1, 20)
      my_comp = [user_guess, premium_comp1, premium_comp2, premium_comp3, premium_comp4]
      if(user_guess <= 20 and user_guess > 0):
          
          print("The screen is going to be cleared...")
          os.system('clear')
          print("Now the guessing player please guess numbers from 1 - 20")
          attempt = 10
          while True:
             try:
                  print(f"Attempt left #{attempt}")
                  
                  guessing = int(input("Enter number between 1 - 20: "))
                  if(attempt == 2):
                      if "premium" in username:
                          premium_user = input("Type 'hint' for hint and for continuing without hint type anything: ").capitalize()
                          if(premium_user == "Hint"):
                              print("One of them is correct")
                              random.shuffle(my_comp)
                              print(my_comp)
                 
                  attempt -= 1
                 
                  if(guessing == user_guess):
                      print(f"The player won\nHe guessed {user_guess}")
                      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                          data = json.load(file)
                          data["Wins"] += 1
                      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
                          json.dump(data, file, indent = 4)
                          break
                          sys.exit()
 
                      
                  else:
                      print("Try again")
                  if(attempt == 0):
                    print("You lost buddy")
                    with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file1:
                      data1 = json.load(file1)
                      data1["Loses"] += 1
                    with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file1:
                      json.dump(data1, file1, indent = 4)
                      break
                      sys.exit()    
              
             except:
                 print("Please enter a valid number")
      else:
          print("Invalid")
      
def passnplay_hard(username, password, user_choice, difficulty_user_choice):
  if(user_choice == "1" and difficulty_user_choice == "2"):
      print("First please choose who is gonna be guessing and who is gonna pick that number who other is guessing")
      print(".......................")
      user_guess = int(input("So make other player close his eye and another one please the enter the number: "))
      premium_comp1 = random.randint(1, 40)
      premium_comp2 = random.randint(1, 40)
      premium_comp3 = random.randint(1, 40)
      premium_comp4 = random.randint(1, 40)
      my_comp = [user_guess, premium_comp1, premium_comp2, premium_comp3, premium_comp4]
      if(user_guess <= 40 and user_guess > 0):
          
          print("The screen is going to be cleared...")
          os.system('clear')
          print("Now the guessing player please guess numbers from 1 - 40")
          attempt = 10
          while True:
             try:
                  print(f"Attempt left #{attempt}")
                  
                  guessing = int(input("Enter number between 1 - 40: "))
                  if(attempt == 2):
                      if "premium" in username:
                          premium_user = input("Type 'hint' for hint and for continuing without hint type anything: ").capitalize()
                          if(premium_user == "Hint"):
                              print("One of them is correct")
                              random.shuffle(my_comp)
                              print(my_comp)
                 
                  attempt -= 1
                 
                  if(guessing == user_guess):
                      print(f"The player won\nHe guessed {user_guess}")
                      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file:
                          data = json.load(file)
                          data["Wins"] += 1
                      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file:
                          json.dump(data, file, indent = 4)
                          break
                          sys.exit()
 
                      
                  else:
                      print("Try again")
                  if(attempt == 0):
                    print("You lost buddy")
                    with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "r") as file1:
                      data1 = json.load(file1)
                      data1["Loses"] += 1
                    with open(f"/storage/emulated/0/Python learning/things made by Siddharth/game/{username}_{password}.txt", "w") as file1:
                      json.dump(data1, file1, indent = 4)
                      break
                      sys.exit()    
              
             except:
                 print("Please enter a valid number")
      else:
          print("Invalid")
             
          
  
game()
user = user_choice()
exit(user)
sign_in(user)
username, password = log_in(user)
user_s_p = game_score()
leaderboard(user_s_p)
scores(user_s_p, username, password)
buy_premium(user_s_p, username, password)
scores_comparison(user_s_p)
game_choice(user_s_p)
user_choice = game_user_choice(user_s_p)
exit(user_choice)
difficulty(user_s_p)
difficulty_user_choice = difficulty_choice(user_s_p)
robotvs_easy(username, password, user_choice, difficulty_user_choice)
robotvs_hard(username, password, user_choice, difficulty_user_choice)
passnplay_easy(username, password, user_choice, difficulty_user_choice)
passnplay_hard(username, password, user_choice, difficulty_user_choice)