#
# Alejandro Ramirez Valdes
# Text Based Game 'Chicken Ghost Buster'
# December 25,2021
#


def show_instructions():
    # print a main menu and the commands
    print ('****Chicken Ghost Buster Text Adventure Game****')
    print ('Collect 6 amulets to win the game, or be burned alive by the Evil Entity.')
    print ('Amulets: Aztec Medallion, Einstein"s Watch, Soul Ring, Pearl Necklace, Sapphire Blade, Mystical Tiara')
    print ('Add to Inventory: get "item name"')
    print ('Move commands: South, North, East, West')


def main():
    rooms = {  # All rooms in the game
        'Great Room': {'name': 'Great Room', 'South': 'Gym', 'North': 'Bedroom', 'West': 'Office', 'East': 'Kitchen'},
        'Bedroom': {'name': 'Bedroom', 'East': 'Patio', 'South': 'Great Room', 'item': 'Aztec Medallion'},
        'Patio': {'name': 'Patio', 'West': 'Bedroom', 'item': "Einstein's Watch"},
        'Office': {'name': 'Office', 'East': 'Great Room', 'item': 'Soul Ring'},
        'Gym': {'name': 'Gym', 'North': 'Great Room', 'East': 'Bathroom', 'item': 'Pearl Necklace'},
        'Bathroom': {'name': 'Bathroom', 'West': 'Gym', 'item': 'Sapphire Blade'},
        'Kitchen': {'name': 'Kitchen', 'West': 'Great Room', 'North': 'Dining Room', 'item': 'Mystical Tiara'},
        'Dining Room': {'name': 'Dining Room', 'South': 'Kitchen'}}  # Evil Entity
    directions = ['North', 'South', 'East', 'West']
    current_room = rooms['Great Room']
    inventory = [] # Holds list of amulets as they are discovered

    # Game loop
    while True:
        if current_room == rooms['Patio']:  # Defines exit statement
            print ('\nHello! You have reached the Patio and found an exit!')
            command = input('\nType "exit" to leave or "continue" to keep playing: ')
            if command == 'exit':
                print ('\nGoodbye!')
                break
            elif command == 'continue':
                print ('\nAlright!')
            else:
                print('\nInvalid entry. Try Again. ') # Check for valid input
        elif current_room == rooms['Dining Room']:  # Winning the game
            len(inventory)
            if len(inventory) == 6: # Game is won when inventory equals 6 and player enters Dinning Room
                print ('Congratulations!! You collected all the amulets and defeated evil!')
                print ('Thank you for playing the game. I hope you enjoyed it')
                break
            else:   # Losing the game
                print ('Oh no! Looks like you are a burned chicken!')
                print ('Game Over!')
                print ('Thank you for playing the game.')
                play_again = input('\nWould you like to play again? Type "Y" for yes or "N" for no: ')
                if play_again == 'Y':
                    print ('\nHere we go!!')
                    if __name__ == '__main__':
                        main()
                else:
                    print ('\nCome back soon!')
                    break
            break
        print ('\n###############')
        print ('You are in the {}.'.format(current_room['name']))  # Display current location
        if 'item' in current_room:
            print ('Look, there is the {}.'.format(current_room['item']))
            if current_room['item'] in inventory:
                print ('You already have this item')
            else:
                command = input('Do you want to get the amulet? ')
                if command == 'get {}'.format(current_room['item']):
                    print ('\nYou have added the {} to your inventory.'.format(current_room['item']))
                    inventory.append(current_room['item'])  # Adding items to inventory
                else:
                    print ('Wrong instruction. You left the {} behind.'.format(current_room['item']))
            print ('\nInventory: ' + str(inventory))
        command = input('\nWhich direction do you want to go? ')  # Get user direction input
        if command in directions:  # Movement
            if command in current_room:
                current_room = rooms[current_room[command]]
            else:
                print ('\nYou cannot go that way.')  # Wrong move
        elif command == 'quit':
            print ('\nThanks for playing!')  # Quit game
            break
        else:
            print ('\nInvalid input')  # Bad command


print (show_instructions())


if __name__ == '__main__':
    main()
