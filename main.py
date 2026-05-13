# Project - CRUD Operations ( Create , Read , Update & Delete )

from pathlib import Path
import os

def readfileandfolder():
    try:
        p = Path('')
        items = list(p.rglob('*'))
        for index , file in enumerate(items):
            print(f'{index+1} - {file}')
    except Exception as e:
            print(e)


# 1.) Creating a file
def create_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file : ")
        p = Path(file_name)
        if p.exists():
            print("FILE ALREADY EXISTS")
        else:
            with open(file_name, 'w') as file:
                content = input('Enter your file content: ')
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)


# 2.) Reading a file
def read_file():
    readfileandfolder()
    file_name = input('Enter name of your file:')
    p = Path(file_name)
    if p.exists():
        with open(file_name, 'r') as file:
            print(file.read())
    
    else:
        print('FILE NOT FOUND!')


# 3.) Updating a file
def update_file():
    try:
        readfileandfolder()
        file_name = input('Enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('Press 1 to overwrite the content')
            print('Press 2 to append new content')

            option = int(input('Enter your choice for updating a file: '))
            if option == 1:
                with open(file_name,'w') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED.....')

            elif option == 2:
                 with open(file_name,'w') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED.....')

            else:
                print('INVALID INPUT!')

        else:
            print('FILE DOES NOT EXISTS!')
    
    except Exception as e:
        print(e)


# 4.) Deleting file

def delete_file():
    readfileandfolder()
    file_name = input('Enter name of your file: ')
    p = Path(file_name)
    if p.exists():
        os.remove(p)    # OS is removing path of that file completely from the system
        print('FILE DELETED!')
    else:
        print('FILE DOES NOT EXISTS!!')
    

# 5.) Renaming file
def rename_file():
    readfileandfolder()
    file_name = input('Enter the name of your file : ')
    p = Path(file_name)
    if p.exists():
        new_file = input('Enter new name of your file : ')
        p.rename(new_file)
        print('FILE RENAMED ')

    else:
        print('FILE NOT FOUND !')


# 6.) Creating a folder
def create_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder : ')
    p = Path(folder_name)
    if p.exists():
        print('FOLDER ALREADY EXISTS!')

    else:
        p.mkdir()
        print('FOLDER CREATED!')
    

# 7.) Deleting a folder
def delete_folder():
    readfileandfolder()
    folder_name = input('Enter name of the folder : ')
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print('FOLDER DELETED')

    else:
        print('FOLDER NOT FOUND!')

while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for renaming a file")
    print("Press 6 for creating a folder")
    print("Press 7 for deleting a folder")
    print("Press 0 for exiting......")

    option = int(input("Enter your choice: "))
    if option == 1:
        create_file()

    if option == 2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()

    if option == 5:
        rename_file()
    
    if option == 6:
        create_folder()

    if option == 7:
        delete_folder()

    if option == 0:
        break
