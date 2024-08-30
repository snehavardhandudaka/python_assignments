from datetime import datetime

def add_entry(filename, entry):
    with open(filename, 'a') as file:
        file.write(f"{datetime.now()}: {entry}\n")

filename = 'guestbook.txt'
entry = input("Enter your entry: ")
add_entry(filename, entry)
print("Entry added.")
