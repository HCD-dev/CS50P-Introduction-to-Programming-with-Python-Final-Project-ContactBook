# Contact Book

# Hüseyin Çağatay DOĞRUYOL

#### Video Demo: <https://www.youtube.com/watch?v=pqsDkoCWRTk>

#### Description:
This project is a simple **Contact Book** program that allows users to add, view, search, and delete contacts. The contacts are stored in a CSV file and managed using two classes: 
- `Contact` (which represents individual contacts) 
- `ContactBook` (which handles the collection of contacts). 

The program includes a command-line interface for interacting with the contact book.

#### Files:
- **`project.py`**: Contains the `Contact` and `ContactBook` classes, as well as the logic to manage contacts (add, update, delete, search).
- **`test_project.py`**: Contains tests for the core functions (`add`, `view`, `search`, `delete`) using `pytest`.
- **`requirements.txt`**: Lists dependencies (currently only `pytest`).

#### Usage:
To use this contact book:
1. Run the program using `python project.py`.
2. Choose from the available options (Add, Update, View, Search, Delete Contacts).
3. The contacts are stored in the `contacts.csv` file.
4. To run the tests, use `pytest` in the terminal: `pytest test_project.py`.

#### Features:
- **Add Contacts**: Users can add new contacts with their name, phone number, and email address.
- **Update Contacts**: Allows users to update existing contacts, including editing name, phone number, and email.
- **Delete Contacts**: Deletes contacts based on the name prefix (allows for multiple contacts with the same name).
- **Search Contacts**: Allows searching by name, phone number, or email.

#### Future Improvements:
- Implement a persistent storage system using **SQLite** for better scalability.
- Add more detailed contact information (address, birthday, etc.).
- Implement a graphical user interface (GUI) using **Tkinter**.
- Integrate contact synchronization across multiple devices.

#### Dependencies:
- `pytest` for testing.
- `csv` for managing contact storage.

#### Installation:
1. Install dependencies with `pip`:
   ```bash
   pip install -r requirements.txt
