# Tempest_DDoS
Tempest is a Python script designed for launching DDoS (Distributed Denial of Service) attacks. It allows you to specify a target IP address or domain name, and optionally a port, directly from the command line.

## Features

- **Simple Command-Line Interface:** Easy to use with command-line arguments for target and port.
- **Flexible Targeting:** Supports both IP addresses and domain names.
- **Threaded Attack:** Utilizes threading to simulate multiple connections for the attack.

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
