import os
import random
import string
import colorama

# Change directory
path = input("\nEnter the path to folder where you want to randomize file names: ")

# Checking the existence of a path
if not os.path.exists(path):
    print(f"{colorama.Fore.RED}Error: The directory path does not exist.{colorama.Style.RESET_ALL}")
    exit()

# Confirmation 
confirmation = input(f"{colorama.Fore.YELLOW}When you press enter, the program renames ALL files in that folder. \
                                           \nYOU CAN'T UNDO THIS! \
                                           \nYOU ARE SURE you want to mess up all file names in the folder {path}? (Y/N): {colorama.Style.RESET_ALL}")

# If yes
if confirmation.lower() == "y": 
    # Main (it's renaming all the files)
    os.chdir(path)
    for filename in os.listdir(path):
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, letters=10))    # Generate a random name
        file_extension = os.path.splitext(filename)[1]                                          # Get the file extension
        new_filename = new_name + file_extension                                                # Create the new file name by concatenating the random name and file extension
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))               # Rename the file
        print("Done, all files are renamed.")

#If no
elif confirmation.lower() == "n": exit()

#If you are idiot 
else: print("Error: Invalid character.")
