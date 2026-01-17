import json
 
try:
    with open("notesList.json", "r") as file:
        notesList = json.load(file)
except:
    notesList = []

print("--🎀 Welcome to Notes App 🎯--")
print("1-Add Note ➕ ")
print("2-List The Notes 🗒️")
print("3-Delete Note 🗑️")
print("4-Exit 👋")

while True:
    try:
        userInput = int(input("Please choose one of the options(1-4): "))
    except ValueError:
        print("Invalid option. Please enter a valid option!")
        continue

    if userInput == 1:
        textInput = input("\nEnter note: \n")
        notesList.append(textInput)

    elif userInput == 2:
        if not notesList:
            print("\nThere is no note yet, please add one.\n")
        else:
            for index,value in enumerate(notesList):
                print(f"\n{index + 1}: {value}\n")

    elif userInput == 3:
        popInput = int(input("\nPlease choose a note to delete: \n"))
        notesList.pop(popInput - 1)
        print("\nNote deleted succesfully!\n")

    elif userInput == 4:
        with open("notesList.json", "w") as file:
            json.dump(notesList, file)
        print("\nThanks for using Notes App. Goodbye👋")
        break
    else:
        print("\nInvalid Option!\n")