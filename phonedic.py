import json

FILE_NAME = "phone_directory.json"

phone_directory = []

try:
    with open(FILE_NAME, "r") as file:
        phone_directory = json.load(file)
except FileNotFoundError:
    phone_directory = []

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(phone_directory, file)
        
# functions
def addcontact(cn, pn):
    contact = {"name": cn, "phone_number": pn}
    return phone_directory.append(contact)

def showcontact():
    print(phone_directory)

def findposition(name):
    for index, contact in enumerate(phone_directory):
        if contact["name"] == name:
            return index + 1
            
def deletecontact(name):
    for contact in phone_directory:
        if contact["name"] == name:
            phone_directory.remove(contact)
            print("The contact '{name}' has been deleted.")
def contactsletter(letter):
    foundcontacts = []
    for contact in phone_directory:
        if contact["name"].startswith(letter):
            foundcontacts.append(contact)
    if foundcontacts:
        print("Contacts starting with the letter '{letter}':")
        for contact in foundcontacts:
            print(contact["name"], "-", contact["phone_number"])
    else:
        print("No contacts found starting with the letter '{letter}'.")

def sortdir():
    sorted_dir = sorted(phone_directory, key=lambda x: (x["name"], x["name"].split()[0]))
    phone_directory.clear()
    phone_directory.extend(sorted_dir)
    print("The directory has been sorted.")
    
# l manue 

print("Hello, welcome to the phone world how may i help you please choose an operation ")
print("1_ add a new contact\n2_show the list of contacts\n3_search for a contact\n4_delete a contact\n5_show all the contacts that start with the letter\n6_sort the directory by names")
# tkhayr choice ta3 l operation
choice = int(input())

if choice == 1:
  name = input("Enter contact name: ")
  phone_number = input("Enter phone number: ")
  addcontact(name, phone_number)
  save_contacts()
elif choice == 2:
  showcontact()
elif choice == 3:
    name = input("Enter the name to search: ")
    contactp = findposition(name)

    if contactp != -1:
        print(contactp)
    else:
        print(-1)
elif choice == 4:
    name = input("Enter the name to delete: ")
    deletecontact(name)
    save_contacts()
elif choice == 5:
    letter = input("Enter the letter to search for contacts starting with: ")
    contactsletter(letter)
    save_contacts()
elif choice == 6:
    sortdir()
    save_contacts()
else:
  print( "error .. operation unkown")
