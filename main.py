# Nickname Generator Assignment
import random
# Make a nickname list where it stores nicknames
nickname_list = []

# Append nicknames to list
nickname_list.append("Thronebreaker")
nickname_list.append("Twinkle Toes")
nickname_list.append("Superstar")
nickname_list.append("Giggles")

def main():
    # Get users first and last name
    first_name = input("Please enter your first name ")
    last_name = input("Please enter your last name ")

    # Create loop for menu
    done = False
    while not done:
        # Print Menu
        print ("\nMAIN MENU (" + first_name + " " + last_name + ")")
        print("1. Change Name")
        print("2. Display a Random Nickname")
        print("3. Display All Nicknames")
        print("4. Add a nickname")
        print("5. Remove a Nickname")
        print("6. Exit")

        # Get selection from user
        selection = input("\nPlease enter a selection from 1-6: ")

        # Change Name
        if selection == "1":
            first_name = input("Please enter your first name ")
            last_name = input("Please enter your last name ")
        
        # Display a random nickname
        elif selection == "2":
            random_name = random.randrange(0, len(nickname_list))
            print("\n" + first_name + " " + nickname_list[random_name] + " " + last_name)
       
        # Display All Nicknames
        elif selection == "3":
            for i in range (len(nickname_list)):
                print (first_name + " " + nickname_list[i] + " " + last_name)

        # Add a nickname
        elif selection == "4":
            new_nickname = input("Enter a new nickname: ")
            if new_nickname in nickname_list:
                print("Nickname is already in list")
            else:
                nickname_list.append(new_nickname)
                print(new_nickname + " added to the nickname list")
            
        # Remove a nickname
        elif selection == "5":
            remove_nickname = input("Please enter a nickname to remove: ")
            if remove_nickname in nickname_list:
                nickname_list.remove(remove_nickname)
                print(remove_nickname + " removed from the nickname list")
            else:
                print(remove_nickname + " was not found in the nickname list")

        # Exit
        elif selection == "6":
            done = True

if __name__ == "__main__":
    main()