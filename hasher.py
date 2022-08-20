import os
from hashlib import sha256

original_string = input("What is the last string used?\n")
order_up = True
if original_string == "":
    original_string = ("0" * 64)
else:
    print("Use + to go up in order or - to go down in order.")
    order = input("\nWhat order do you want to go?\n")
    if order == "-":
        order_up = False

# File location
File_Name = input("\n\n\nWhat is the filename used to store the hashes?\n")
if File_Name == "":
    File_Name = "sha256_log.txt"
    print("\nSince you don't have a file yet, we'll create one called ", File_Name, ".\n")
File_location = ""
if File_location == "":
    while File_location == "":
        File_location = input("\nPlease input the full location of the folder where you want to store the file:\n")
Folder_bol = os.path.exists(File_location)
if not Folder_bol:
    os.mkdir(File_location)
    Folder_bol = True
if "\\" in File_location:
    Linux = False
else:
    Linux = True
if Linux:
    File_Full = File_location + "/" + File_Name
else:
    File_Full = File_location + "\\" + File_Name
File_bol = os.path.exists(File_Full)
if not File_bol:
    with open(File_Full, 'w') as File:
        First_line = "original_String:Hash_string"
        File.write((" "*int(65-(len(First_line)/2)) + First_line + "\n"))
File = open(File_Full, 'a')
input("\nAll ready.\n\n\n")

while True:
    Hashed = sha256(original_string.encode('utf-8')).hexdigest()
    Hashed_string = str(Hashed)
    File.write(original_string + (" "*5) + Hashed_string + "\n")
    if order_up:
        hex_string = hex(int(original_string, 16) + 1)
    else:
        hex_string = hex(int(original_string, 16) - 1)
    original_string = ("0" * (64 - len(hex_string[2:]))) + hex_string[2:]
    print(original_string, ":", Hashed_string)
