# Text-based Adventure Game

def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious room.")
    print("Your goal is to find the treasure and escape the room.")
    print("Good luck!")

def explore_room():
    print("You look around the room.")
    print("There are two doors: one on the left and one on the right.")
    print("Which door do you choose? (left/right)")

    choice = input().lower()

    if choice == "left":
        enter_left_door()
    elif choice == "right":
        enter_right_door()
    else:
        print("Invalid choice. Try again.")
        explore_room()

def enter_left_door():
    print("You open the left door.")
    print("You see a dark hallway stretching out in front of you.")
    print("What do you do? (proceed/turn back)")

    choice = input().lower()

    if choice == "proceed":
        print("You cautiously move forward in the dark hallway.")
        print("You stumble upon a hidden trap and get caught.")
        print("Game over!")
    elif choice == "turn back":
        print("You decide to turn back and go to the main room.")
        explore_room()
    else:
        print("Invalid choice. Try again.")
        enter_left_door()

def enter_right_door():
    print("You open the right door.")
    print("You see a brightly lit room with a treasure chest in the corner.")
    print("Congratulations! You found the treasure.")
    print("You win the game!")

# Start the game
start_game()

# Explore the room
explore_room()


'''
=================================
Test Case:
=================================

Welcome to the Adventure Game!
You wake up in a mysterious room.
Your goal is to find the treasure and escape the room.
Good luck!
You look around the room.
There are two doors: one on the left and one on the right.
Which door do you choose? (left/right)
left
You open the left door.
You see a dark hallway stretching out in front of you.
What do you do? (proceed/turn back)
proceed
You cautiously move forward in the dark hallway.
You stumble upon a hidden trap and get caught.
Game over!

'''