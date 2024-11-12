import csv
import re

class ContactBook:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        contacts.append({'name': row[0], 'phone': row[1], 'email': row[2]})
        except FileNotFoundError:
            pass
        return contacts

    def save_contacts(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact['name'], contact['phone'], contact['email']])

    def add_contact(self, name, phone, email):
        self.contacts.append({'name': name, 'phone': phone, 'email': email})
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        if results:
            for idx, contact in enumerate(results, 1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts found.")

    def delete_contact(self, name_prefix):
        matches = [contact for contact in self.contacts if contact['name'].lower().startswith(name_prefix.lower())]
        if matches:
            for idx, contact in enumerate(matches, 1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            choice = input(f"Which contact would you like to delete? Enter the number or press Enter to cancel: ")
            if choice:
                try:
                    index = int(choice) - 1
                    self.contacts.remove(matches[index])
                    self.save_contacts()
                    print("Contact deleted successfully.")
                except (ValueError, IndexError):
                    print("Invalid choice. Deletion canceled.")
        else:
            print("No contacts found with that name prefix.")

    def update_contact(self, name_prefix):
        matches = [contact for contact in self.contacts if contact['name'].lower().startswith(name_prefix.lower())]
        if matches:
            if len(matches) > 1:
                print("Multiple contacts found with that name prefix:")
                for idx, contact in enumerate(matches, 1):
                    print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                choice = input(f"Which contact would you like to update? Enter the number or press Enter to cancel: ")
                if choice:
                    try:
                        index = int(choice) - 1
                        contact_to_update = matches[index]
                        self.edit_contact(contact_to_update)
                    except (ValueError, IndexError):
                        print("Invalid choice. Update canceled.")
            else:
                contact_to_update = matches[0]
                self.edit_contact(contact_to_update)
        else:
            print("No contacts found with that name prefix.")

    def edit_contact(self, contact):
        print(f"Updating contact: {contact['name']}")
        new_phone = input(f"Enter new phone number (current: {contact['phone']}): ")
        if new_phone:
            contact['phone'] = new_phone
        new_email = input(f"Enter new email (current: {contact['email']}): ")
        if new_email:
            contact['email'] = new_email
        self.save_contacts()
        print("Contact updated successfully.")

# Example usage of the ContactBook class
contact_book = ContactBook()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contacts\n4. Delete Contact\n5. Update Contact\n6. Exit")
    choice = input("Please choose an option (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_book.add_contact(name, phone, email)

    elif choice == "2":
        contact_book.view_contacts()

    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        contact_book.search_contacts(query)

    elif choice == "4":
        name_prefix = input("Enter the name prefix to delete: ")
        contact_book.delete_contact(name_prefix)

    elif choice == "5":
        name_prefix = input("Enter the name prefix to update: ")
        contact_book.update_contact(name_prefix)

    elif choice == "6":
        break
    else:
        print("Invalid option. Please choose between 1 and 6.")
