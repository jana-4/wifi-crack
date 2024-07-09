import requests
# URL of the router's administration interface for managing MAC address filtering
admin_url = "http://192.168.1.1/cgi-bin/content.asp"

session = requests.Session() 

# Function to remove a MAC address from the blacklist
def remove_mac_from_blacklist(mac_address):
    payload = {
        'action': 'remove_from_blacklist',
        'mac_address': mac_address
    }
    response = requests.post(admin_url, data=payload)
    if response.status_code == 200:
        print(f"MAC address {mac_address} removed from the blacklist successfully.")
        return True
    else:
        print(f"MAC address {mac_address} removed from the blacklist successfully.")
        return False
    
# MAC address to remove from the blacklist
mac_to_remove = input("Target MAC Address: ")

# Remove the MAC address from the blacklist
remove_mac_from_blacklist(mac_to_remove)

session.get(f"http://192.168.1.1/logout")