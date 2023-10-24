import time

def intro():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. You can go left or right.")

def left_path():
    print("You chose the left path. You discover a hidden cave.")
    choice = input("Do you want to enter the cave? (yes/no): ").lower()
    if choice == "yes":
        print("You entered the cave and found a treasure chest. You win!")
    elif choice == "no":
        print("You decided not to enter the cave and continue your journey.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def right_path():
    print("You chose the right path. You encounter a ferocious bear!")
    choice = input("Do you want to fight the bear or run away? (fight/run): ").lower()
    if choice == "fight":
        print("You bravely fought the bear, but it was too strong. You lost.")
    elif choice == "run":
        print("You wisely chose to run away and escape from the bear. You survive.")
    else:
        print("Invalid choice. Please enter 'fight' or 'run'.")

def main():
    intro()
    time.sleep(1)  # Add a pause for dramatic effect
    choice = input("Which path will you choose? (left/right): ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")

if __name__ == "__main__":
    main()
