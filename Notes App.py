import os

def show_menu():
    print("Simple Notes App")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                for idx, note in enumerate(notes, start=1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

def edit_note():
    view_notes()
    try:
        note_number = int(input("Enter the note number you want to edit: "))
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 1 <= note_number <= len(notes):
            new_note = input("Enter the new note: ")
            notes[note_number - 1] = new_note + "\n"
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print("Note edited successfully.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a valid note number.")

def delete_note():
    view_notes()
    try:
        note_number = int(input("Enter the note number you want to delete: "))
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 1 <= note_number <= len(notes):
            del notes[note_number - 1]
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print("Note deleted successfully.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a valid note number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting the notes app. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
