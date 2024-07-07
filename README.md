# Tempest DDoS Attack Script

This script allows you to perform a DDoS attack on a specified target IP address or domain name. It includes ASCII art for visual appeal when the script starts.

## Features

- Simple and easy-to-use DDoS attack script
- ASCII art displayed on startup
- Prompts user for target IP address/domain and port
- Default port set to 80 if not specified
- Multi-threaded attack for increased impact

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/blydon025/Tempest_DDoS.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd Tempest_DDoS
    ```

3. Run the script:

    ```bash
    python3 tempest.py
    ```

## Usage

1. Run the script:

    ```bash
    python tempest.py
    ```

2. Enter the target IP address or domain name when prompted:

    ```
    Target (IP or domain): -> example.com
    ```

3. Enter the target port when prompted (default is 80 if left blank):

    ```
    Port (default is 80): -> 80
    ```

4. The script will start the DDoS attack with 500 threads.

## Disclaimer

This script is for educational purposes only. Do not use it to attack any systems or networks without proper authorization. Unauthorized use of this script may violate local, state, or federal laws.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

