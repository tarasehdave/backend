# Dictionary to store username and password pairs
user_credentials = {
    "sharonkodali": "pears",
    "tarasehdave": "apples",
    "alishahussain": "trees"
    ""
}

# Function to check if the entered credentials are valid
def login(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    else:
        return False

# Main login loop
while True:
    print("Please log in:")
    username = input("Username: ")
    password = input("Password: ")

    if login(username, password):
        print("Login successful. Welcome, " + username + "!")
        break
    else:
        print("Invalid credentials. Please try again.")



