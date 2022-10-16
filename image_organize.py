import glob
import os
import string


# test folder location for my reference: /Users/jasbook/Pictures/22_09_13-copy
# note that at the moment you need to enter the full path to the folder in the prompt.

def prompt_user():
    folder = input("Enter folder location: ")
    if os.path.exists(folder):
        return folder
    else:
        print("Invalid folder location")
        prompt_user()


def select_files(folder, extension):
    os.chdir(folder)
    files = glob.glob("*." + extension)
    return files


def get_extensions(folder):
    files = os.listdir(folder)
    for file in files:
        print(file.split(".")[-1])



def rename_files(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    for file in files:
        os.rename(file, file.lower())


def create_folder(folder, extension):
    if not os.path.exists(folder + "/" + extension):
        os.makedirs(folder + "/" + extension)


def move_files(folder, extension):
    files = select_files(folder, extension)
    for file in files:
        os.rename(folder + "/" + file, folder + "/" + extension + "/" + file)


def quit_or_rerun():
    query_rerun = (input("Sort another folder? (y/n): ")).lower()
    if query_rerun == "n":
        print("Peace.")
        exit(0)
    elif query_rerun == "y":
        main()
    else:
        print("Invalid selection, try again.")
        quit_or_rerun()


def main():
    folder = prompt_user()
    rename_files(folder)
    get_extensions(folder)
    extensions = ["jpg", "png", "gif", "svg", "cr2", "tif", "tiff", ".dng"]
    for extension in extensions:
        create_folder(folder, extension)
        move_files(folder, extension)
    print("Success. Probably? I'd check if I were you.")
    quit_or_rerun()


main()
