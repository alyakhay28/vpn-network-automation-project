# VPN Network Automation Project

This project demonstrates the automation of **Site-to-Site GRE VPN tunnels** between a headquarters and branch offices using Python scripts and Cisco routers simulated in GNS3. The automation server is a Debian appliance that runs the Python script to configure routers via **chained Telnet sessions**.

The project highlights:

- Network automation for VPN deployment
- Hub-and-spoke topology with GRE tunnels
- Python scripting for configuration and testing
- Secure deployment practices by injecting scripts at the border router

---

## Project Structure

```

vpn-network-automation/
├── README.md             # Project overview and instructions
├── requirements.txt      # Python dependencies
├── scripts/
│   └── vpn_automation.py # Main automation script
├── configs/              # Router configurations (optional)
├── docs/                 # Project documentation
├── tests/                # Testing scripts
└── images/               # Screenshots and diagrams

````

---

## Prerequisites

Before running the automation script, make sure you have:

- Python 3 installed
- Telnet enabled on the network devices
- Debian (or Linux) automation server setup
- GNS3 topology with routers configured as described in the project

---

## How to Run

1. Open a terminal on the Debian automation server.
2. Navigate to the `scripts/` directory.
3. Run the automation script "vpn_automation.py".
4. The script will configure GRE tunnels and static routes on R2, R3, and R4 automatically using chained Telnet sessions.
5. Verify connectivity using 'ping' or 'traceroute' commands to confirm the tunnels between the HQ and the branch sites are operational.
---

## Network Topology

The network is set up in a **hub-and-spoke** architecture:

* **R1 (HQ Router)** – internal services and security gateway
* **R2 (Transit Router)** – border router and automation script injection point
* **R3 (Johor Branch Router)** – connects to R2 via Tunnel0
* **R4 (Penang Branch Router)** – connects to R2 via Tunnel1

The automation server communicates with R1, then chains Telnet to R2, and from there to R3 and R4.

---

## GRE Tunnel Details

| Router | Tunnel  | IP Address  | Source       | Destination  | Purpose            |
| ------ | ------- | ----------- | ------------ | ------------ | ------------------ |
| R2     | Tunnel0 | 10.0.0.1/30 | 192.168.51.2 | 192.168.51.3 | Connects to R3     |
| R2     | Tunnel1 | 10.0.0.5/30 | 192.168.52.2 | 192.168.52.3 | Connects to R4     |
| R3     | Tunnel0 | 10.0.0.2/30 | 192.168.51.3 | 192.168.51.2 | Reverse path to R2 |
| R4     | Tunnel1 | 10.0.0.6/30 | 192.168.52.3 | 192.168.52.2 | Reverse path to R2 |

---

## Key Lessons Learned

* **Efficiency of Automation:** Reduces repetitive CLI commands, saves time, and decreases human errors.
* **Standardization:** Consistent configurations across routers simplify troubleshooting.
* **Network Security:** Script injection at the border router ensures internal network isolation.
* **Chained Telnet Limitations:** Works for lab environment, but SSH is recommended for secure production automation.

---

## Future Improvements

* Replace Telnet with SSH-based libraries such as **Netmiko** for secure automation.
* Integrate **dynamic routing protocols** like OSPF or EIGRP.
* Implement **error handling and logging** in Python scripts for better automation management.

---

## Screenshots / Documentation

Refer to the `images/` folder for:

* Network Topology Diagram
* GRE Tunnel Status (R2, R3, R4)
* IP Addressing and Configuration Documentation
