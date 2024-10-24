import bcrypt
import csv
import re
import requests
import getpass

# Hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# Check if entered password matches stored password
def check_password(stored_password, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_password)

# Writing a new user to the CSV file (Registration process)
def write_user_to_csv(email, password, security_question):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        hashed_password = hash_password(password)
        # Store the hashed password, email, and security question
        writer.writerow([email, hashed_password.decode(), security_question])

# Email validation
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Password validation
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[\W_]', password):  # Special characters
        return False
    return True

# Register a new user
def register():
    print("Register a new account")
    email = input("Enter email: ")
    
    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return
    
    password = getpass.getpass("Enter password: ")
    
    if not validate_password(password):
        print("Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character.")
        return
    
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    
    security_question = input("Enter a security question (e.g., What is your favorite color?): ")
    
    # Store the new user credentials
    write_user_to_csv(email, password, security_question)
    print("Registration successful! You can now log in.")

# Resetting the password
def reset_password(email):
    rows = []
    found = False
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                security_question = row[2]
                answer = input(f'{security_question}: ')
                if answer.lower() == 'blue':  # Example static check for answer
                    new_password = input('Enter new password: ')
                    if validate_password(new_password):
                        hashed_password = hash_password(new_password)
                        row[1] = hashed_password.decode()  # Update the password
                        print('Password updated successfully!')
                    else:
                        print('Invalid password format. Must meet the criteria.')
                else:
                    print('Incorrect answer to the security question.')
                found = True
            rows.append(row)
    
    if not found:
        print('Email not found!')

    # Write back updated data to CSV
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Login system
def login():
    attempts = 5
    while attempts > 0:
        email = input('Email: ')
        password = getpass.getpass('Password: ')  # Hides password input

        if validate_email(email):
            with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == email:
                        stored_password = row[1].encode()  # Decode the stored password
                        if check_password(stored_password, password):
                            print('Login successful!')
                            return True
                        else:
                            print('Incorrect password.')
                        break
                else:
                    print('Email not found.')
        else:
            print('Invalid email format.')

        attempts -= 1
        print(f'{attempts} attempts remaining.')

    print('Too many failed attempts. Locked out.')
    return False

# Searching for a game via CheapShark API
def search_game(game_title):
    url = f"https://www.cheapshark.com/api/1.0/deals?title={game_title}&sortBy=Deal%20Rating"
    response = requests.get(url)
    if response.status_code == 200:
        deals = response.json()
        if deals:
            for deal in deals:
                print(f"Game: {deal['title']}")
                print(f"Store: {deal['storeID']}")  # Can be mapped to store names if necessary
                print(f"Normal Price: ${deal['normalPrice']}")
                print(f"Sale Price: ${deal['salePrice']}")
                print(f"Savings: {deal['savings']}%")
                print(f"Deal Rating: {deal['dealRating']}")
                print(f"Link: https://www.cheapshark.com/redirect?dealID={deal['dealID']}")  # Corrected link to store
                print('-' * 40)
        else:
            print("No deals found for this game.")
    else:
        print("Error fetching game data from the API.")

# Main application flow
def main():
    print("Welcome to the PC Game Price Comparison Application!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                game_title = input("Enter the name of the game to search for: ")
                search_game(game_title)
        elif choice == '3':
            email = input("Enter your registered email: ")
            reset_password(email)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()  