import os
import random
import string
import colorama

# Change directory
path = input("\nEnter the path to folder where you want to randomize file names: ")


confirmation = input f"{colorama.Fore.YELLOW}When you press enter, the program renames ALL files in that folder. \
                                           \nYOU ARE SURE you want to mess up all file names in the folder {path}? \
                                           \nYOU CAN'T UNDO THIS! \
                       {colorama.Style.RESET_ALL}"



if not os.path.exists(path):
    print(f"{colorama.Fore.RED}Error: The directory path does not exist.{colorama.Style.RESET_ALL}")
    exit()
os.chdir(path)


# loop through all files in the folder
for filename in os.listdir(path):
    # generate a random name
    new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # get the file extension
    file_extension = os.path.splitext(filename)[1]
    # create the new file name by concatenating the random name and file extension
    new_filename = new_name + file_extension
    # rename the file
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
