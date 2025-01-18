# ARP Spoofing Tool

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#working">Working</a> •
  <a href="#future-enhancements">Future Enhancements</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## Introduction

The **ARP Spoofing Tool** is a Python-based utility built using the `Scapy` library. It allows users to perform ARP spoofing attacks by sending crafted ARP packets to a target and a gateway, effectively redirecting network traffic for monitoring or manipulation purposes.

This tool demonstrates the implementation of:

- ARP protocol manipulation
- Packet crafting and injection
- Basic error handling and recovery (restoring ARP tables)

---

## Features

- **Dynamic MAC Address Retrieval**: Automatically fetches the target's and gateway's MAC addresses.
- **ARP Spoofing**: Performs ARP poisoning on the target and gateway.
- **ARP Table Restoration**: Automatically restores the ARP tables upon termination.
- **Error Handling**: Validates input and ensures safe execution.
- **Console Output**: Displays real-time packet sending and status updates.

---

 Installation

### Prerequisites

To run this project, you need:

- **Python**: Version 3.6 or higher.
- **Scapy Library**: Install it using pip:
  ```bash
  pip install scapy

  ```
- Administrator/root privileges for network-level operations.

### Steps to Install

```bash
git clone https://github.com/your-repo/arp-spoofing.git
cd arp-spoofing
pip install -r requirements.txt
 ```

## Usage
Command-Line Options
The script uses the optparse library for command-line arguments. Run the script as follows:

    python arp_spoof.py -t <target-ip> -s <source-ip>
    
Arguments

-t or --target: The target's IP address (required).
-s or --source: The IP address to spoof as (required).


Example

    python arp_spoof.py -t 192.168.1.5 -s 192.168.1.1

    
Termination
Press CTRL+C to stop the attack and restore ARP tables.



## Working
- Fetch MAC Addresses: The tool uses ARP requests to fetch the MAC addresses of the target and the spoofed IP.
- Send ARP Packets: Sends crafted ARP responses to the target and gateway to poison their ARP tables.
- Packet Restoration: Upon termination, sends correct ARP packets to restore the original ARP tables.

## Future Enhancements
- Add logging to track ARP packets sent.
- Implement packet sniffing to capture redirected traffic.
- Introduce an interactive GUI for easier configuration.
- Add more attack scenarios, such as Man-in-the-Middle attacks.

## Disclaimer
This tool is for educational purposes only. Unauthorized use of ARP spoofing can cause network disruption and is illegal in many jurisdictions. Use responsibly and only on networks where you have explicit permission.





