
import random
# random_number = random.randint(1, 10)
# print(random_number)

import time

random_number = random.randint(1, 5)
cat_attack_random = random.randint(1, 20)
random_30_percent = random.randint(1, 3)
random_50_percent = random.randint(1, 2)

pets_left = 3


# FUNC -get name and greet 
def user_name():
  """Gets user input for user name"""
  name = input("Please enter your name. ")
  name = name.title().strip()
  return name

def decrease_score(pets_left, pets_lost):
    """Returns new score total"""

    pets_left = pets_left - pets_lost

    return pets_left



def welcome_pet_the_cat():
  """Welcomes and introduces user to game, gets user name"""
  name = user_name()
  print(f"Welcome {name}, are you ready to try petting the cat? I will give you some information about cats before we get started!")
  time.sleep(2)
  print()
  print("OK, here are some tips before you try petting this adorable cat:")
  time.sleep(3)
# info about petting cats, while cats have 9 lives they are impatient and you cannot attempt to pet them 9 times
  print("- although cats have 9 lives they do not have much patience, you can only pet the cat wrong 3 times before experiencing a full blown cat attack and losing the game.")
  time.sleep(3)
  print("- you will get three opportunities to choose where to pet the cat.")
  time.sleep(3)
  print("- because cats are the greatest animals in the world (and know it), they can be fickle. Plan accordingly.")
  time.sleep(3)
  print("That being said, it is now time to Pet the Cat!")
  print()
  time.sleep(2)


# I'd also encourage you to think about how you could actually use a function to ask all the questions and shorten your code. I would highly recommend building out the basic functionality before moving into the more complex logic. Let me know if you have any questions about this!
#you get three chances to pet the cat correctly before you get attacked and lose the game
#create WHILE loop
#must keep running count of times pet wrong, at 3 wrong pets cat attacks you lose game
#call first cat FUNC stick out hand for cat to sniff or go right for the pet? right for the pet = point off, sniff = ok 
#call first petting function petting style: pet cat head to tail, tail to head, side to side. head to tail = ok, side to side = ok 50% of time, tail to head = point off

#belly FUNC - omg cat has shown you it's belly!!! It looks so cute, inviting and floofy, pet the belly? No = always safe, Yes = Ok 25% of the time (you should have known it was a trap)
#random cat attack FUNC - 5% of time cat attacks for no reason at all, lose game
def petting_style_cat(): 
  """function for petting the cat"""
  while True:
    pets_left = 3
    random_number = random.randint(1, 5)
    # cat_attack_random = random.randint(1, 20)
    random_30_percent = random.randint(1, 3)
    random_50_percent = random.randint(1, 2)
    pet_style = input("How would you like to pet the cat? Please enter 1 for head-to-tail, 2 for side-to-side or 3 for tail-to-head.")
    time.sleep(3)
    pet_style = pet_style.strip().lower()
    # elif cat_attack_random == 17:
    #   print("Oh wow, you just experienced a random cat attack for no reason. The cat was having a bad day and you were supposed to know. Sorry, you lost this game.")
    #   break
    if pet_style == "1":
      print("Good job, that was the correct direction to pet the cat in.")
    elif pet_style == "2" and (random_number == 2 or random_number == 4):
      print("Sorry, sometimes it's ok to pet the cat side to side but not today. You lost a point.")
      time.sleep(2)
      pets_lost = 1
      pets_left = decrease_score(pets_left, pets_lost)
      print(f"Pets left: {pets_left}.")
    elif pet_style == "2":
      print("The cat decided it was OK for you to pet it side to side today. You're safe for now.")
    elif pet_style == "3":
      print("You can never pet a cat backwards! You lose one point.")
      time.sleep(2)
      pets_lost = 1
      pets_left = decrease_score(pets_left, pets_lost)
      print(f"Pets left: {pets_left}.")
    #secret pspspsp
   
    else:
      print("Error. That was not a valid option. The cat says you must do everything perfectly. You lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_left, pets_lost)
      print(f"Pets left: {pets_left}.")
      
    return pets_left
    
      # second petting FUNC choose where to pet cat (head, neck, back, front legs, back legs, paws, tail). 10% of time even if right spot cat gets mad and you lose a point (cats aren't always in a good mood and you should know that), head = ok, back = ok, front legs = point off, back legs = point off, tail = ok 75% of time
def pet_location_cat():
  while True:
    pets_left = pets_update_1
    pet_location = input("Now you get to decide where to pet the cat. Please enter 1 to pet it's head, 2 to pet it's back, 3 to pet it all the way to it's tail, or 4 to boop it's paws.")
    pet_location = pet_location.strip().lower()
    time.sleep(2)
    if pet_location == "1":
      print("Great choice! It is almost always ok to pet a cat on the head.")
    elif pet_location == "2":
      print("Cats like to be pet on their back, good choice.")
    elif pet_location == "3" and random_number == 4:
      print("That was a questionable spot to pet the cat and today it didn't work out for you, you lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_update_1, pets_lost)
      print(f"Pets left: {pets_left}.")
    elif pet_location == "3":
      print("The tail can be a little risky but it looks like you pulled it off.")
    elif pet_location == "4" and random_30_percent == 2:
      print("Booping is fun but extremely risky, you lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_update_1, pets_lost)
      print(f"Pets left: {pets_left}.")
    elif pet_location == "4":
      print("Booping is extremely risky but somehow you pulled it off today.")

    else:
      print("Error. That was not a valid option. The cat says you must do everything perfectly. You lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_update_1, pets_lost)
      print(f"Pets left: {pets_left}.")

    return pets_left

    time.sleep(2)
def belly_pet_cat():
  """Prompts user to pet belly and subtracts points if option causes loss of points"""
  print("Oh. My. God. The cat has rolled over and showed you it's squishy belly!!! It is so cute and floofy!")
  while True:
    pets_left = pets_update_2
    time.sleep(3)
    belly_pet = input("Are you going to pet the cats belly? Please type yes or no.")
    belly_pet = belly_pet.lower()
    belly_pet = belly_pet.strip()
    if "p" in belly_pet and "s" in belly_pet:
      print("OMG you speak cat, have broken the secret code, and have won the game! Congratulations!!!!")
      pets_left = 10000000
      print(f"Pets left: {pets_left}.")
      
    elif belly_pet == "no":
      print("That was a safe choice, 50% of the time the belly roll is a trap.")
      time.sleep(2)
    elif (belly_pet == "yes") and (random_50_percent == 2):
      print("That was a trap. You lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_update_2, pets_lost)
      print(f"Pets left: {pets_left}.")
      time.sleep(2)
    elif belly_pet == "yes":
      print("Wow you got lucky today, half the time a belly roll is a trap but you pulled it off.")
      time.sleep(2)
  
    else:
      print("Error. That was not a valid option. The cat says you must do everything perfectly. You lose a point.")
      pets_lost = 1
      pets_left = decrease_score(pets_update_2, pets_lost)
      print(f"Pets left: {pets_left}.")
    
    return pets_left

# def final_score():
#   """Calculates is user won depending on points left"""
# #If you get to this point with less than 3 wrong pets, congratulations you are a cat petting expert!!! You have won a lifelong friend to feed treats to and pet every day!
# while True:
    # if pets_left > 0:
    #     print("Woohoo!!! You have made it to the end of the game without petting the cat wrong too many times. Congrtulations you are a cat petting expert and have won a lifelong friend to feed treats to and pet every day! Yay!")
    #     break
    # elif pets_left <= 0:
    #     print("Sorry you are not a cat petting expert. You have lost this game.")
    #     break
    # else:
    #     print("An error has occured.")
  


def play_cat_petting_game():
  """Uses all functions created to play cat petting game from start to finish"""
while True:
  pets_left = 3
  # user_name()
  welcome_pet_the_cat()
  cat_attack_random = random.randint(1, 20)
  if cat_attack_random == 17:
    print("Oh wow, you just experienced a random cat attack for no reason. The cat was having a bad day and you were supposed to know. Sorry, you lost this game.")
    break
  pets_update_1 = petting_style_cat()
  print()
  pets_update_2 = pet_location_cat()
  print()
  ending_pets_left = belly_pet_cat()
  print()
  if ending_pets_left > 0:
        print("Woohoo!!! You have made it to the end of the game without petting the cat wrong too many times. Congratulations you are a cat petting expert and have won a lifelong friend to feed treats to and pet every day! Yay!")
        break
  elif ending_pets_left <= 0:
        print("Sorry you are not a cat petting expert. You have lost this game.")
        break
  else:
        print("An error has occured.")
  # final_score()

    
  # while True:
  #     if pets_left > 0:
  #       print("Woohoo!!! You have made it to the end of the game without petting the cat wrong too many times. Congrtulations you are a cat petting expert and have won a lifelong friend to feed treats to and pet every day! Yay!")
  #     break
    
  #     else:
  #       print("Sorry you are not a cat petting expert. You have lost this game.")
  #         break
      
      
# def final_score():
#   """Calculates is user won depending on points left"""
# #If you get to this point with less than 3 wrong pets, congratulations you are a cat petting expert!!! You have won a lifelong friend to feed treats to and pet every day!
# while True:
#     if pets_left > 0:
#         print("Woohoo!!! You have made it to the end of the game without petting the cat wrong too many times. Congrtulations you are a cat petting expert and have won a lifelong friend to feed treats to and pet every day! Yay!")
#         break
#     elif pets_left <= 0:
#         print("Sorry you are not a cat petting expert. You have lost this game.")
#         break
#     else:
#         print("An error has occured.")

play_cat_petting_game()


