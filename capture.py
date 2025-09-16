#As usual i begin with the brain of my project so Welcome to my Python Packet Sniffer Project !

#i'll be starting with importing the man of the moment in this project lol - Scapy
from scapy.all import sniff, wrpcap                         #sniff will capture packets while wrpcap will writes packets to my .pcap file 
import os                           #to check for files in the os


OUTPUT_FILE = "captures/test_run.pcap"          #this is where the capture will be saved


#this will check if the captures" folder exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok = True)

#just a simple logic to create the "output_file" if it does not exist 
if not os.path.exists(OUTPUT_FILE):
    open(OUTPUT_FILE, "wb").close()
    



#the packets_capture functions begins 
def capture_packets():
    #nothing serious just an indicator that the capturing process has begun and an instructiion to follow if you want to stop the damn thing - ops sorry lol
    print("[*] Starting packet capture") 
    packets = sniff(count = 50)     #captures 50 packets
    wrpcap(OUTPUT_FILE, packets)
    print(f"[*] Saved {len(packets)} packets to {OUTPUT_FILE}")






if __name__ == "__main__":
    capture_packets()