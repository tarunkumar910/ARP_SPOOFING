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

## Installation

### Prerequisites

To run this project, you need:

- **Python**: Version 3.6 or higher.
- **Scapy Library**: Install it using pip:
  ```bash
  pip install scapy
