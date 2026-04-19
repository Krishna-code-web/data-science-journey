from pathlib import Path
import os

def readfileandfolder():
    path = Path('') # Gives the path of the current folder # 01_file_handling_project
    items = list(path.rglob('*')) # Gives all the items in this path folder
    for i, items in enumerate(items):
        print(f"{i+1}  : {items} ")

def createfile():
    try:
        readfileandfolder()
        name = input('Please tell your file name :- ')
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
            
            print(f'FILE CREATED SUCCESSFULLY!')
        else:
            print(f'File already exists!')
    
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input('Please tell your file name :- ')
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("Readed Successfully!")
        else:
            print("File does not exists!")
    
    except Exception as err:
        print(f'An error occured as {err}')

def updatefile():
    try:
        readfileandfolder()
        name = input('Please tell your file name :- ')
        p = Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("tell  your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data :- ")
                    fs.write(data)
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" "+data)
        else:
            print('File does not exists!')
    
    except Exception as err:
        print("an error occured as {err}")

def deletefile():
    try:

        readfileandfolder()
        name = input("which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes successfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

if __name__ == "__main__":
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")

    check = int(input("PLease tell your response :- "))

    if check == 1:
        createfile()

    if check == 2:
        readfile()

    if check == 3:
        updatefile()

    if check == 4:
        deletefile()
