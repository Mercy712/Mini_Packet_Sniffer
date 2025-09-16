# Python-Based Packet Sniffer 
Capture packets. Read the network. Think like a SOC analyst, one packet at a time.


# What is this?

This is a small, beginner-friendly Network tool written in Python.
It lets you capture network packets from your machine and save them in .pcap format so you can open them with Wireshark for inspection and analysis.

This project is simple and educational — built so you understand how packet capture works under the hood and can practice packet forensics.

# Features

Capture live packets from your network interface (It can be controlled).
Save captured packets to captures/test_run.pcap.


# Project Structure

Python_Packet_Sniffer/
│── capture.py           #i like to call it the brain of the project, it's the script that captures packets
└── captures/
    └── test_run.pcap    #this is where the captured packets are saved


# Prerequisites

Python 3.8+ installed
Dependencies (install with the command below):
scapy — used for sniffing & writing pcap files

#Clone this Repo
git clone https://github.com/Mecy712/Python_Packet_Sniffer.git
cd Python_Packet_Sniffer


#create a virtual environment 
python -m venv .venv

#Windows PowerShell:
.venv\Scripts\Activate.ps1

#or if you don't have a requirements file yet:
pip install scapy


# Quick usage checklist (SOC-style)

Run python capture.py.

Perform some safe browsing/pings on your laptop while capture runs (e.g., ping 8.8.8.8, open Google, visit a website).

Stop when capture finishes and open captures/test_run.pcap in Wireshark for futher analysis.




