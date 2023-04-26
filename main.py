import os
import random
import string
import colorama

# messages
error = f"{colorama.Fore.RED}Error: "           # Error
notif = f"{colorama.Fore.BLUE}Notification: "   # Notification
warn = f"{colorama.Fore.YELLOW}Warning: "       # Warning
scess = f"{colorama.Fore.GREEN}Success: "       # Success
end = f"{colorama.Style.RESET_ALL}"             # Reset all styles

# Change directory
path = input("\nEnter the path to folder where you want to randomize file names: ")

# Checking the existence of a path
if not os.path.exists(path):
    print(f"{error}Error: The directory path does not exist.{end}")
    exit()

# Confirmation 
confirmation = input(f"{warn}When you press enter, the program renames ALL files in that folder.\n"
                            "YOU CAN'T UNDO THIS!\n"
                           f"YOU ARE SURE you want to mess up all file names in the folder {path}? (Y/N): {end}")

# If yes
if confirmation.lower() == "y": 
    # Main (it's renaming all the files)
    os.chdir(path)
    for filename in os.listdir(path):
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))    # Generate a random name
        file_extension = os.path.splitext(filename)[1]                                    # Get the file extension
        new_filename = new_name + file_extension                                          # Create the new file name by concatenating the random name and file extension
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))         # Rename the file
    print(f"{scess}Done, all files are renamed.{end}")

#If no
elif confirmation.lower() == "n": exit()

#If you are idiot 
else: print(f"{error}Invalid character.{end}")
