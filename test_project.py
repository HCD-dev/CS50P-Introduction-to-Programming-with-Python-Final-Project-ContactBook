import pytest
from project import ContactBook

@pytest.fixture
def contact_book():
    """Fixture to initialize a fresh ContactBook before each test."""
    contact_book = ContactBook('test_contacts.csv')
    # Ensure the CSV file is cleared before each test
    contact_book.contacts = []
    contact_book.save_contacts()
    return contact_book

def test_add_contact(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    assert len(contact_book.contacts) == 1
    assert contact_book.contacts[0]['name'] == 'John Doe'
    assert contact_book.contacts[0]['phone'] == '+1234567890'
    assert contact_book.contacts[0]['email'] == 'johndoe@example.com'

def test_view_contacts(contact_book):
    contact_book.add_contact('Jane Smith', '+0987654321', 'janesmith@example.com')
    contact_book.add_contact('Bob Johnson', '+1122334455', 'bobjohnson@example.com')
    contact_book.view_contacts()
    # Assert that there are 2 contacts now
    assert len(contact_book.contacts) == 2

def test_search_contacts(contact_book):
    contact_book.add_contact('Alice Brown', '+1212121212', 'alice@example.com')
    contact_book.add_contact('Charlie White', '+1313131313', 'charlie@example.com')
    
    # Test search for a part of the name
    search_results = contact_book.search_contacts('Alice')
    assert len(search_results) == 1
    assert search_results[0]['name'] == 'Alice Brown'
    
    # Test search for a part of the phone number
    search_results = contact_book.search_contacts('1313')
    assert len(search_results) == 1
    assert search_results[0]['name'] == 'Charlie White'

def test_delete_contact(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    contact_book.add_contact('John Smith', '+0987654321', 'johnsmith@example.com')
    
    # Test deleting a single contact by exact name
    contact_book.delete_contact('John Doe')
    assert len(contact_book.contacts) == 1
    assert contact_book.contacts[0]['name'] == 'John Smith'

def test_delete_multiple_contacts(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    contact_book.add_contact('John Smith', '+0987654321', 'johnsmith@example.com')
    contact_book.add_contact('Johnny Depp', '+1122334455', 'johnny@example.com')
    
    # Test deleting contacts by prefix (John)
    contact_book.delete_contact('John')
    assert len(contact_book.contacts) == 0  # All "John" contacts should be deleted

def test_update_contact(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    contact_book.update_contact('John', new_phone='+1111111111', new_email='john.doe@example.com')
    
    # Ensure the contact was updated correctly
    updated_contact = contact_book.contacts[0]
    assert updated_contact['phone'] == '+1111111111'
    assert updated_contact['email'] == 'john.doe@example.com'

def test_invalid_delete(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    
    # Try deleting a contact with a non-matching prefix
    contact_book.delete_contact('Jane')
    assert len(contact_book.contacts) == 1  # The contact list should remain unchanged

def test_multiple_contacts_with_same_name(contact_book):
    contact_book.add_contact('John Doe', '+1234567890', 'johndoe@example.com')
    contact_book.add_contact('John Smith', '+0987654321', 'johnsmith@example.com')
    contact_book.add_contact('John Johnson', '+1122334455', 'johnjohnson@example.com')

    # Test deleting by name prefix, with multiple John contacts
    contact_book.delete_contact('John')
    assert len(contact_book.contacts) == 0  # All 'John' contacts should be deleted
