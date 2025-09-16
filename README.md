# Python-Based Packet Sniffer 
Capture packets. Read the network. Think like a SOC analyst, one packet at a time.


What is this?

This is a small, beginner-friendly Network tool written in Python.
It lets you capture network packets from your machine and save them in .pcap format so you can open them with Wireshark for inspection and analysis.

This project is simple and educational — built so you understand how packet capture works under the hood and can practice packet forensics.

Features

Capture live packets from your network interface (controlled capture mode).

Save captured packets to captures/test_run.pcap.


Python_Packet_Sniffer/
│── capture.py           #i like to call it the brain of the project, it's the script that captures packets
└── captures/
    └── test_run.pcap    #this is where the captured packets are saved


Prerequisites

Python 3.8+ installed

pip available

Dependencies (install with the command below):

scapy — used for sniffing & writing pcap files

Add more libraries later as the project grows.
