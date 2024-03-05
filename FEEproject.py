def login():
    print("Welcome to the Word Counter App!")

    # Hardcoded username and password (replace with your own logic for a real application)
    correct_username = "user123"
    correct_password = "password123"

    # Get user input
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    

    # Check if the entered credentials are correct
    if username_input == correct_username and password_input == correct_password:
        print("Login successful! You can now use the Word Counter.")
        word_counter()
    else:
        print("Incorrect username or password. Please try again.")
        login()

def word_counter():
    # Implement your word counting logic here
    text = input("Enter a sentence or paragraph: ")
    word_count = len(text.split())
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    login()
