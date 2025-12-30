# VPN Network Automation using GRE and Python

This project demonstrates the automation of Site-to-Site VPN deployment using
Generic Routing Encapsulation (GRE) tunnels in a hub-and-spoke enterprise network
topology. The automation is implemented using Python and Telnet, executed from a
Debian-based Network Automation Server in a GNS3 simulated environment.

## 📌 Project Overview

- **HQ Router (R1)**: Internal services and access point for the automation server  
- **Transit Router (R2)**: Border router and automation injection point  
- **Branch Routers (R3 & R4)**: Remote sites connected via GRE tunnels  
- **Automation Server**: Debian Linux running Python automation scripts  

The project uses **chained Telnet access** to configure routers that are not
directly reachable from the automation server, demonstrating real-world
automation constraints and solutions.

## 🎯 Objectives

- Automate GRE tunnel configuration between HQ and branch routers
- Implement a hub-and-spoke VPN topology
- Reduce manual configuration and human error
- Demonstrate secure automation practices by isolating internal HQ devices
- Verify VPN connectivity using testing and validation commands

## 🛠 Tools & Technologies

- Python 3
- Telnet (telnetlib)
- GNS3
- Cisco IOS Routers
- Debian Linux (Automation Server)
- GRE (Generic Routing Encapsulation)

## 📂 Project Structure
vpn-network-automation/
├── README.md
├── requirements.txt
├── scripts/
│ └── vpn_automation.py
├── configs/
├── docs/
├── tests/
└── images/


## 🚀 How Automation Works

1. The Debian automation server connects to **R1** via Telnet
2. Chained Telnet access is used to reach **R2**
3. From **R2**, the script configures:
   - GRE Tunnel0 (R2 ↔ R3)
   - GRE Tunnel1 (R2 ↔ R4)
4. Tunnel interfaces are assigned IP addresses and activated
5. Configurations are saved automatically

## 🔐 Security Note

Telnet is used for educational purposes in a simulated environment. In production
networks, SSH-based automation tools such as **Netmiko** or **Paramiko** should be
used instead.

## 📈 Learning Outcomes

- Practical understanding of network automation
- Hands-on experience with GRE tunneling
- Chained device access using Telnet
- Automation scripting with Python
- Secure network design principles

## 👤 Author

'ALYA' ADIBAH BINTI KHAIRUDDIN
Bachelor of Computer Science (Hons.) Computer Networks  
