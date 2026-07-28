from pathlib import Path
import os
import shutil
#! Creating Folder
def create_folder():
    try:
        name = input("Enter the name of your folder:- ")
        p = Path(name)
        p.mkdir()
        print("Folder created successfully")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

#! Reading File and Folder by rcecursive-glob(rglob)
def read_file_folder():
    p = Path("")
    items = list(p.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")

#! Update the folder
def update_folder():
    try:
        read_file_folder()
        old_name = input("Name the folder you want to update")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Enter the new name you want to change :- ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder is updated successfully")
        else:
            print("Sorry no such folder exists")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

# ! Delete folder
def delete_folder():
    try:
        read_file_folder()
        name = input("Enter the folder you want to delete")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder Deleted Successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

# ! Create File
def create_file():
    read_file_folder()
    name = input("Enter the name of your file")
    p = Path(name)
    if not p.exists():
        with open(name,"w") as fs:
            data = input("Enter the data you want to write")
            fs.write(data)

#! Read a file
def read_file():
    try:
        read_file_folder()
        name = input("Tell your file name")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,"r") as fs:
                content = fs.read()
                print("Your content is :- ")
                print(content)
        else:
            print("File does nt exists")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

#! Update File
def update_file():
    try:
        read_file_folder()
        name = input("Enter your file name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Options :- ")
            print("1. For Renaming a file")
            print("2. For appending data on the file ")
            print("3. For Overwriting The content")
            choice = int(input("Tell Your Choice "))
            if choice == 1:
                new_name = input("Enter the name you want to update ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("File name update successfully")
                else:
                    print("File name already exists")
            if choice == 2:
                with open(name,"a") as fs:
                    data = input("Enter what you want to append")
                    fs.write(" "+data)
                    print("File appended successfully")
            if choice == 3:
                with open(name,"w") as fs:
                    data = input("Enter what you want rewrite")
                    fs.write(data)
                    print("Data changed successfully")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

#! Delete a file
def delete_file():
    try:
        read_file_folder()
        name = input("Enter file name with extension")
        p = Path(name)
        if p.exists and p.is_file():
            p.unlink()
            print("Deleted Successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

while True:
    print(" options :")

    print("1. For Creating a folder")
    print("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete The Folder")
    print("5. Create a File")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. for exit")

    choose = int(input("Choose an option above !"))

    if choose == 1:
        create_folder()
    if choose == 2:
        read_file_folder()
    if choose == 3:
        update_folder()
    if choose == 4:
        delete_folder()
    if choose == 5:
        create_file()
    if choose == 6:
        read_file()
    if choose == 7:
        update_file()
    if choose == 8:
        delete_file()