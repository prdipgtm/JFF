#hangman game 

import random
import os

guess= {
  "animals" : ["Elephant", "Tiger", "Lion", "Giraffe", "Kangaroo", "Panda", "Zebra", "Dolphin", "Penguin", "Gorilla", "Hippopotamus", "Crocodile", "Rhinoceros", "Ostrich", "Koala", "Polar Bear", "Flamingo", "Seahorse", "Chimpanzee", "Cheetah"],

  "fruits" : ["Apple", "Banana", "Mango", "Orange", "Grape", "Pineapple", "Strawberry", "Blueberry", "Raspberry", "Watermelon", "Papaya", "Peach", "Plum", "Pear", "Kiwi", "Pomegranate", "Lychee", "Dragon Fruit", "Cherry", "Avocado"],

  "places" : ["Paris", "London", "New York", "Tokyo", "Sydney", "Mumbai", "Dubai", "Beijing", "Cairo", "Rio de Janeiro", "Rome", "Istanbul", "Bangkok", "Singapore", "Moscow", "Los Angeles", "Toronto", "Cape Town", "Berlin", "Hong Kong"],

}
#selects random vlaues form keys :
choiceAnimals =random.choice(guess["animals"])
choiceFruits =random.choice(guess["fruits"])
choicePlace =random.choice(guess["places"])



def instruction():
  print('Menu:')
  print("On which sector of name that you want to guess?\nAvailable -->(Animals , Fruits , Place , Device)")


def Ch_animals():
  word_to_guess= choiceAnimals.lower()
  guessed= []
  unguessed=["_"]*len(choiceAnimals)
  tries = len(choiceAnimals)
  print(f"You have got {tries} , try !")
  print(f"Guess the animal : {" ".join(unguessed)}") #creates a string from a list ["_", "_" , "_" .......] to ---> (_ _ _ _ ......) which is easy to manipulate
  
  while tries != 0 and "_"in unguessed:
    choice  = input("enter a letter -->")

    if choice in guessed:
      print("Already Guessed !")

    elif choice in word_to_guess:
      guessed.append(choice)

      for index, letter in enumerate(word_to_guess):#display the letter at it's index and removes "_"
        if letter == choice:
          unguessed[index] = choice
          print("Good guess! Current word: ", " ".join(unguessed))

    else:
      tries -=1
      print(f"Wrong guessed you have {tries} tries left !")

    if "_" not in unguessed:
      print("CONGRATULATION YOU WON !")

    if tries == 0 :
      print("You Lost !")
      print(f"The word to be guessed was {choiceAnimals}")
 

def Ch_place():
  word_to_guess= choiceFruits.lower()
  guessed= []
  unguessed=["_"]*len(choiceFruits)
  tries = len(choiceFruits)
  print(f"You have got {tries} , try !")
  print(f"Guess the Place : {" ".join(unguessed)}")
  
  while tries != 0 and "_"in unguessed:
    choice  = input("enter a letter -->")

    if choice in guessed:
      print("Already Guessed !")

    elif choice in word_to_guess:
      guessed.append(choice)

      for index, letter in enumerate(word_to_guess):
        if letter == choice:
          unguessed[index] = choice
          print("Good guess! Current word: ", " ".join(unguessed))

    else:
      tries -=1
      print(f"Wrong guessed you have {tries} tries left !")

    if "_" not in unguessed:
      print("CONGRATULATION YOU WON !")

    if tries == 0 :
      print("You Lost !")


def ch_fruits():
  word_to_guess= choiceFruits.lower()
  guessed= []
  unguessed=["_"]*len(choiceFruits)
  tries = len(choiceFruits)
  print(f"You have got {tries} , try !")
  print(f"Guess the Fruits : {" ".join(unguessed)}")
  
  while tries != 0 and "_"in unguessed:
    choice  = input("enter a letter -->")

    if choice in guessed:
      print("Already Guessed !")

    elif choice in word_to_guess:
      guessed.append(choice)

      for index, letter in enumerate(word_to_guess):
        if letter == choice:
          unguessed[index] = choice
          print("Good guess! Current word: ", " ".join(unguessed))

    else:
      tries -=1
      print(f"Wrong guessed you have {tries} tries left !")

    if "_" not in unguessed:
      print("CONGRATULATION YOU WON !")

    if tries == 0 :
      print("You Lost !")
      print(f"The word to be guessed was {choicePlace}")  



if __name__=="__main__": # sector choosing 
  while True:
    instruction()
    ch = input("enter the sector-->> ")
    if ch.lower() == "animals":
      Ch_animals()
    elif ch.lower()== 'place':
      Ch_place()
    elif ch.lower() == 'fruits':
      ch_fruits()


     