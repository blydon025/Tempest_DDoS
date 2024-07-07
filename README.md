![Background Image](https://www.google.com/imgres?q=cool%20hacking%20background&imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fdd%2F53%2Fd8%2Fdd53d87ffa084978d5d1734b03ec1266.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F678354762641045945%2F&docid=IeoOH0jwykqsTM&tbnid=aWeJQBMwbxidDM&vet=12ahUKEwjzgaf7gpWHAxUUZ0EAHU6-CHkQM3oECGcQAA..i&w=1680&h=1050&hcb=2&ved=2ahUKEwjzgaf7gpWHAxUUZ0EAHU6-CHkQM3oECGcQAA)
# Tempest_DDoS
Tempest is a Python script designed for launching DDoS (Distributed Denial of Service) attacks. It allows you to specify a target IP address or domain name, and optionally a port, directly from the command line.

## Features

- **Simple Command-Line Interface:** Easy to use with command-line arguments for target and port.
- **Flexible Targeting:** Supports both IP addresses and domain names.
- **Threaded Attack:** Utilizes threading to simulate multiple connections for the attack.

## Installation

Clone the repository:

```bash
git clone https://github.com/blydon025/Tempest_DDoS.git
cd Tempest_DDoS
```

## Usage

To run Tempest, use the following command format:

```bash
python tempest.py TARGET [-p PORT]
```
- `TARGET` can be a website URL or an IP address.
- `-p PORT` (optional) specifies the port to target (default is 80).

## Examples
Launch a DDoS attack on example.com:
```bash
python tempest.py example.com
```

Launch a DDoS attack on 192.168.1.100 on port 8080:
```bash
python tempest.py 192.168.1.100 -p 8080
```
## Notes
Use this script responsibly and only in environments you have permission to test.
Adjust the number of threads (range(500)) in the script based on your testing requirements and target system capabilities.
Disclaimer
This script is provided for educational purposes only. Misuse of this script for attacking targets without authorization is illegal and unethical. Use it responsibly and only on systems you have permission to test.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Brads - @blydon025
