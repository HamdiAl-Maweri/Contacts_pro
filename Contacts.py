def view(contacts):
    print("______________________________________________________________________________")
    print("Contacts:")
    for name, number in contacts.items():
        print(name +" : " + number)
    print("______________________________________________________________________________")

def add(contacts):
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    print(name +" added successfully!")

def update(contacts):
    name = input("Enter name: ")
    if name in contacts:
        new_number = input("Enter new number: ")
        contacts[name] = new_number
        print(name +" updated successfully!")
    else:
        print(name +" not found!")

def delete(contacts):
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print(name +" deleted successfully!")
    else:
        print(name +" not found!")


contacts = {}

while True:
    print("\nMenu:")
    print("1.view")
    print("2.add")
    print("3.update")
    print("4.delete")
    print("5.close")
    
    choice = input("Enter number: ")
    
    if choice == '1':
        view(contacts)
    elif choice == '2':
        add(contacts)
    elif choice == '3':
        update(contacts)
    elif choice == '4':
        delete(contacts)
    elif choice == '5':
        print("Closing")
        break
    else:
        print("Error, please try again.")
print(contacts)