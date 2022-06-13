import random

print("=====Let's Play Rock Paper Scissors: The Python Game=====")
 
print("Possible options are:")  
print("R = rock")  
print("P = paper")  
print("S = scissors") 

while True:
  
  possible_choices = ["R", "P", "S"]

  # take input from the user
  user_choice = input("Enter a choice\n['R', 'P', 'S']: ")                  
                      
  computer_choice = random.choice(possible_choices) 
                      
  print(f"You chose {user_choice}, computer chose {computer_choice}")
                      
  if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie! Try again")
  elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
  elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
  elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

  else:
         print("Invalid Entry! Try again")
         continue

  continue_again = input("Play again? [y/n]: ")
  
  if continue_again == "y":
      pass

  if continue_again == "n":


      print("Thank you for playing")
      break