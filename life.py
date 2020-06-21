#!/usr/bin/python3

import random
import sys
import time
from os import system, name
from termcolor import colored, cprint

"""
init_colony: Initialize 2d array to represent colony of cells

Pre:
    new_colony: 2d array of ints to be initialized
    w: width of colony to be initialized
    h: height of colony to be initialized
    isEmpty: boolean value that determine how the array will be populated

Post:
    Populates the referanced 2d array with the appropiate numbers
"""
def init_colony(new_colony, w, h, isEmpty):
    # If the empty mode is not triggered, initialize the array with random 1's and 0's
    if not isEmpty:
        for i in range (0, h):
            new = []
            for j in range (0, w):
                new.append(random.randint(0, 1))

            new_colony.append(new)

    # If the empty mode is triggered, initialize the array with all 0's
    else:
        for i in range (0, h):
            new = []
            for j in range (0, w):
                new.append(0)

            new_colony.append(new)

"""
print_colony: Output representation of the colony to stdout

Pre: 
    cur_colony: 2d array of ints
    w: integer representing width of colony
    h: integer representing height of colony

Post:
    Output represention of colony using '@' symbol for live cells
    and '-' symbols for dead cells
"""
def print_colony(cur_colony, w, h):
    print('')
    
    for i in range (0, h):
        print("| ", end='')
        for j in range (0, w):
            if cur_colony[i][j] == 1:
                cell_text = colored("@ ", 'blue')
                print (cell_text, end='')
            
            else:
                cell_text = colored("- ", 'red')
                print(cell_text, end='')

        print("|")
    print('')


"""
clear: Clears the console on whichever operating system is running the program

Pre: 
    The terminal contains data and strings

Post: 
    The terminal will be cleared of all data and strings
"""
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


"""
next_generation: Creates the next generation of the colony using three established rules
    1) Any live cell with 1 or fewer neighbors, or more than 4 neighbors
       dies in the next generation
    2) Any live cell with 2-3 neighbors survives to the next generation
    3) Any dead cell with exactly 3 neighbors is brought to life

Pre:
    cur_colony: 2d array of ints that represents the current colony of cells
    w: int representing the width of the colony
    h: int representing the height of the colont

Post:
    A new 2d array of ints is returned with cells altered to represent a new generation
    of cells, following the rules established above
"""
def next_generation(cur_colony, w, h):
    next_gen = []
    init_colony(next_gen, w, h, True)

    for i in range (0, h):
        for j in range (0, w):
            
            """
            Neighbor counting algorithm
            """
            neighbors = 0
            
            if (i - 1) < 0 and (j - 1) < 0:             # If cell is in top left corner
                if cur_colony[i][j+1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

                if cur_colony[i+1][j+1] == 1:
                    neighbors += 1

            elif (i + 1) >= h and (j - 1) < 0:         # If cell is in the bottom left corner
                if cur_colony[i-1][j] == 1:
                    neighbors += 1

                if cur_colony[i-1][j+1] == 1:
                    neighbors += 1

                if cur_colony[i][j+1] == 1:
                    neighbors += 1

            elif (i - 1) < 0 and (j + 1) >= w:        # If cell is in the top right corner
                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

            elif (i + 1) >= h and (j + 1) >= w:      # If cell is in the bottom right corner
                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i-1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i-1][j] == 1:
                    neighbors += 1

            elif (i - 1) < 0:                         # If cell is located in the top row
                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i][j+1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

                if cur_colony[i+1][j+1] == 1:
                    neighbors += 1

            elif (i + 1) >= h:                       # If cell is located in the bottom row
                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i][j+1] == 1:
                    neighbors += 1

                if cur_colony[i-1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i-1][j] == 1:
                    neighbors += 1

                if cur_colony[i-1][j+1] == 1:
                    neighbors += 1

            elif (j - 1) < 0:                       # If cell is located in the left row
                if cur_colony[i-1][j] == 1:
                    neighbors += 1

                if cur_colony[i-1][j+1] == 1:
                    neighbors += 1

                if cur_colony[i][j+1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

                if cur_colony[i+1][j+1] == 1:
                    neighbors += 1

            elif (j + 1) >= w:                   # If cell is located in the right row
                if cur_colony[i-1][j] == 1:
                    neighbors += 1

                if cur_colony[i-1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

            else:                                # Normal cell in colony
                if cur_colony[i-1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i-1][j] == 1:
                    neighbors += 1

                if cur_colony[i-1][j+1] == 1:
                    neighbors += 1

                if cur_colony[i][j-1] == 1:
                    neighbors += 1

                if cur_colony[i][j+1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j-1] == 1:
                    neighbors += 1

                if cur_colony[i+1][j] == 1:
                    neighbors += 1

                if cur_colony[i+1][j+1] == 1:
                    neighbors += 1

            """
            Colony survivor rules
            """
            # Populated cell rules
            if (cur_colony[i][j] == 1):
                if (neighbors <= 1):
                    next_gen[i][j] = 0

                elif (neighbors >= 4):
                    next_gen[i][j] = 0

                else:
                    next_gen[i][j] = 1

            # Unpopulated cell rules
            else:
                if (neighbors == 3):
                    next_gen[i][j] = 1

                else:
                    next_gen[i][j] = 0

    
    return next_gen

"""
Main function of program
"""
def main():
    if len(sys.argv) < 4:
        print("Usage: $./life.py [# generations] [colony width] [colony height]")
        sys.exit(0)

    colony = []
    
    num_generations = int(sys.argv[1])
    colony_w = int(sys.argv[2])
    colony_h = int(sys.argv[3])

    # Input checking
    while num_generations < 3 or num_generations > 1000:
        num_generations = int(input("Please enter a number of generations between 3 & 1000: "))

    while colony_w < 5 or colony_w > 50:
        colony_w = int(input("Please enter a number between 5 & 50 for the width: "))

    while colony_h < 5 or colony_h > 50:
        colony_h = int(input("Please enter a number between 5 & 50 for the height: "))

    # Initialize colony with randomly arranged 1's and 0's
    init_colony(colony, colony_w, colony_h, False)
    
    count = 0

    # Print
    print ("\n\nSeed generation")
    print_colony(colony, colony_w, colony_h)
    time.sleep(1)
    count += 1 
   
    # Menu options
    choice = int(input("\nConway's game of Life:\n\nMenu\n1. Automatic mode\n2. Manual mode\n3. Quit game\n: "))

    while choice < 1 or choice > 3:
        choice = int(input("Please select a number from the menu"))

    # Automatic mode:
    # Automatically advance the colony to the next generation every 0.42 seconds
    # until the number of generations reaches the user specified maximum
    if choice == 1:
        while count <= num_generations:
            clear()
            print("Generation "+str(count))
            colony = next_generation(colony, colony_w, colony_h)
            print_colony(colony, colony_w, colony_h)
            time.sleep(0.42)
            count += 1
       
    # Manual mode:
    # Allow the user to advance the colony to the next generation with a keyboard input.
    # This option ignores the maximum number of generation and allows the user to view the 
    # colony expand indefinitely
    if choice == 2:
        keep_going = True
        gen_count = 0

        while keep_going:
            clear()
            print("Generation: "+str(gen_count))
            print_colony(colony, colony_w, colony_h)
            user = input("\n\nPress q to quit\nPress any other key to advance to next generation: ")
            
            if user == 'q':
                keep_going = False 
                continue

            colony = next_generation(colony, colony_w, colony_h)
            gen_count += 1

    # Quit the program from the menu
    if choice == 3: 
        pass

if __name__ == "__main__":
    main()
    print ("\n\n\aProgram Terminated")
