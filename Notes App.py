notes = []

def add_note(text):
   notes.append(text)
   print('Note added')

def display_notes():
   for note in notes:
      print(note)

while True:
   print("1. Add Note") 
   print("2. View Notes")
   print("3. Quit")

   choice = input("Enter choice: ")

   if choice == '1':
      note = input("Enter note: ")
      add_note(note)
      
   elif choice == '2':   
      display_notes()
      
   elif choice == '3':
      break
      
   else:
      print("Invalid choice")
