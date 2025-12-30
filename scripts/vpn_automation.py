"""
VPN Network Automation Script
Author: Alya Adibah
Date: 25-06-2025
Description: Automates GRE tunnel configuration using Python and Telnet
in a hub-and-spoke topology (R1, R2, R3, R4).
"""


import telnetlib
import time

R1_IP = "192.168.122.2"
PORT = 23
USER = "admin"
PASS = "cisco123"

def send(tn, cmd, delay=0.8):
    print(f"[>] Sending: {cmd}")
    tn.write(cmd.encode('ascii') + b"\n")
    time.sleep(delay)

def login(tn):
    tn.read_until(b"Username:", timeout=10)
    tn.write(USER.encode("ascii") + b"\n")
    tn.read_until(b"Password:", timeout=10)
    tn.write(PASS.encode("ascii") + b"\n")
    tn.read_until(b"#", timeout=10)

def configure_r2(tn):
    send(tn, "conf t")

    send(tn, "interface Tunnel0")
    send(tn, "ip address 10.0.0.1 255.255.255.252")
    send(tn, "tunnel source
