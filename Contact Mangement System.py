import os

File_Name="Contact.txt"

def add_contact():
    name= input("Enter Name: ")
    phone= input("Enter Phone Number: ")
    email= input("Enter Email: ")

    with open(File_Name,"a") as file:
        file.write(f"{name},{phone},{email}\n")

        print("Contact Added Successfully!\n")


def view_Contact():
    if not os.path.exists(File_Name):
        print("No Contacts Found!")
        return
    
    with open(File_Name,"r") as file:
        contacts=file.readlines()
    
    if not contacts:
        print("No Contacts Found!")
    else:
        print("\n Contact Lists:")
        for index,contact in enumerate(contacts,start=1):
            name,phone,email=contact.strip().split(",")
            print(f"{index}.{name}-{phone}-{email}")
    print()

def search_contact(contacts,target,index=0):
    if index >=len(contacts):
        return None

    name,phone,email = contacts[index].strip().split(",")
        
    if target.lower() in name.lower()or target in phone:
        return f"{name} - {phone} -{email}"
    return search_contact(contacts,target,index+1)
    
def search():
    if not os.path.exists(File_Name):
        print("No Contact Found!")
        return
        
    target = input("Enter Name or Phone no. to Search: ")

    with open(File_Name,"r") as file:
        contacts= file.readlines()

    result=search_contact(contacts,target)
    if result:
        print("\n Contact Found:",result,"\n")
    else:
        print("\n Cpntact Not Found!\n")

def update_contact():
    if not os.path.exists(File_Name):
        print("No Contact Found! ")
        return
    
    name_to_update = input("Enter Name to Update: ")

    with open (File_Name,"r") as file:
        contacts = file.readlines()

    updated_contacts= []
    found = False

    for contact in contacts:
        name,phone,email= contact.strip().split(",")
        if name.lower()== name_to_update.lower():
            found = True
            new_phone = input(f"Enter New Phone no. for {name} (Press Enter to Keep {phone}):  ") or phone
            new_email = input(f"Enter New Email ID for {name} (Press Enter to Keep {email}):  ") or email
            updated_contacts.append(f"{name},{new_phone},{new_email}\n")
        else:
            updated_contacts.append(contact)
    
    if found:
        with open(File_Name,"w") as file:
            file.writelines(updated_contacts)
        print("Contact Updated Successfully! \n")
    else:
        print("Contact Not Found!\n")

def delete_contact():
    if not os.path.exists(File_Name):
        print("No Contact found!")
        return
    name_to_delete = input("Enter Name to Delete: ")

    with open(File_Name,"r") as file:
        contacts=file.readlines()

    updated_contacts = [contact for contact in contacts if not contact.lower().startswith(name_to_delete.lower())]

    if len(updated_contacts) < len(contacts):
        with open(File_Name,"w") as files:
            files.writelines(updated_contacts)
        print("Contact Deleted Successfully!\n")
    else:
        print("Contact Not Found \n")

def menu ():
    while True:
        print("Press 1 to Add Contacts")
        print("Press 2 to View Conatcs")
        print("Press 3 to Search Contact")
        print("Press 4 to Update Contact")
        print("Press 5 to Delete Contact")
        print("Press 6 to Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_contact()
        elif choice =="2":
            view_Contact()
        elif choice =="3":
            search()
        elif choice =="4":
            update_contact()
        elif choice =="5":
            delete_contact()
        elif choice =="6":
            print("Exiting... Have a Great Day!")
            break
        else:
            print("Invalid Choice! Please Try Again.\n")


menu()