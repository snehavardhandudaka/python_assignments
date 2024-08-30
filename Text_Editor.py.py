def open_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

filename = input("Enter the filename: ")
action = input("Do you want to 'open' or 'save' the file? ").lower()

if action == 'open':
    content = open_file(filename)
    print("File content:")
    print(content)
elif action == 'save':
    content = input("Enter the content to save: ")
    save_file(filename, content)
    print("File saved.")
else:
    print("Invalid action.")
