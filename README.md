# Personal-Password-Manager

This Python script provides a Personal Password Manager, allowing users to securely store and retrieve their passwords using a MySQL database. 

## It offers the following features:

- Password Saving: Users can save their passwords along with their name, username/email address/phone number, and the website/app name.
- Strong Password Generation: Users can generate a random and strong password using a combination of lowercase letters, uppercase letters, numbers, and special characters.
- Manual Password Entry: Users can manually enter their desired password.
- Database Storage: All password information is securely stored in a MySQL database.
- Password Retrieval: Users can retrieve their saved passwords by providing their name and the corresponding website/app name.
- Copy to Clipboard: The script allows users to copy their retrieved passwords to the clipboard for convenience.

## Requirements
- Python 3.x
- random library
- pyautogui library
- pyperclip library
- pymysql library
- MySQL database (e.g., MySQL server installed locally)

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command: 
      - pip install pyautogui webbrowser pyperclip pymysql
3. Set up a MySQL database and ensure you have the necessary credentials (host, username, password, database name).
4. Update the database connection details in the script by modifying the host, user, passwd, and db variables in the code.
5. Run the script using the Python interpreter:
      - python PersonalPasswordManager.py

## Usage
1. Upon running the script, you will be prompted with options to save a password or view saved passwords.
2. If you choose to save a password:
     - Enter your name, username/email address/phone number, and the website/app name.
     - Select the option to generate a strong password or create one manually.
     - If you generate a strong password, it will be displayed, and you can choose to copy it to the clipboard.
     - If you create a password manually, enter the desired password, and choose to copy it to the clipboard.
     - Your password information will be securely stored in the MySQL database.
3. If you choose to view saved passwords:
    - Enter your name and the corresponding website/app name.
    - The script will retrieve the password from the database and display it.
    - If no matching records are found, an appropriate message will be displayed.
4. Close the script when you have finished using it.

## Note
- Ensure that you have a MySQL server running and accessible with the provided credentials for the script to connect to the database.
- Make sure to handle the security of your database and sensitive information appropriately.

## Acknowledgments

The script utilizes the following libraries:

- pyautogui - Provides GUI automation capabilities for displaying prompts and alerts.
- pyperclip - Enables copying passwords to the clipboard.
- pymysql - Provides the interface to connect and interact with the MySQL database.
- random - Used to generate random numbers in Python

Feel free to contribute, report issues, or suggest improvements.
