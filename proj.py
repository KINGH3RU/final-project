import time
tag = input("Welcome to the Metropoitan Mainnet, What is your name?")
time.sleep(2)
print("Hey", tag)
time.sleep(1)
route = input('Would you like to log into the Philadelphia net or the NewYorkCity net? Say "P" to log into the Philadelphia net or "N" the NewYorkCity net')

contacts = {}
contacts["proffesor rosen"] = {'phone': "1234567890", 'email': "example@temple.edu"}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {'phone': phone, 'email': email}
    print("Contact {name} added successfully.")

def view_contacts():
    if len(contacts) == 0:
        print("No members found.")
    else:
        for name, info in contacts.items():
            print(f"{name}: {info['phone']}, {info['email']}")

def show_objective():
    if route == "P" or "p":
        objective = "Create a fund to purchase wholesale fresh food fom local farms and establish a community farmers market"
        print(objective)
    elif route == "N" or "n":
        objective = "create a community fund to pay unemployed citizens to clean local streets to tackle the rat crisis"
        print(objective)
    
def show_menu():
    if route == "N":
                print("Welcome to the NewYorkCity Mainnet.")
    elif route == "P":
                print("Welcome to the Philadelphia Mainnet.")
    while True:
        import time
        time.sleep(3)
        print("Select an option:")
        print("1. Join Notificaion List")
        print("2. Show Group Objective")
        print("3. View Active Members")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_objective()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    show_menu()
