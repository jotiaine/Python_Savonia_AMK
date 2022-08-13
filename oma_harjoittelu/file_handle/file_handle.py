import os

# Import OS module to acces operating system

# READ FILE


def read_file():
    file = open("text.txt")
    # file = open("text.txt", "rt")
    print(file.read())  # file object method read
    file.close()


read_file()

# READ PART OF FILE


def read_part_of_file():
    file = open("text.txt")
    print(file.read(5))
    file.close()


read_part_of_file()

# READ LINE BY LINE


def read_lines():
    file = open("text.txt")
    print(file.readline())
    print(file.readline())
    file.close()


read_lines()

# Write to file
# append


def append_to_file():
    file = open("text.txt", "a")
    file.write("Kolmas rivi lisätty appendilla")
    file.close()


append_to_file()

# write


def write_to_file():
    file = open("text.txt", "w")
    file.write("Overwrite text with w")
    file.close()
    file = open("text.txt")
    print(file.read())
    file.close()


write_to_file()

# create a file


def create_file():
    file = open("new_file.txt", "w")
    file.write("This is a new file")
    file.close()
    file = open("new_file.txt")
    print(file.read())


create_file()


# Remove file
def remove_file():
    if os.path.exists("new_file.txt"):
        os.remove("new_file.txt")
    else:
        print("The file does not exist")


remove_file()


# Create and delete folders
def create_folder():
    os.mkdir("new_folder")
    if os.path.exists("new_folder"):
        os.rmdir("new_folder")
    else:
        print("The folder does not exist")


create_folder()
