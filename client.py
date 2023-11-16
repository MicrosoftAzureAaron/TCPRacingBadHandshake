from scapy.all import IP, TCP, send
from datetime import datetime
import sys

# Destination IP and port
dst_ip = "192.168.1.105"
if len(sys.argv) > 1:
    dst_port = sys.argv[1]
else:
    dst_port = 5221

if len(sys.argv) > 2:
    dst_port = sys.argv[2]
else:
    src_port = 12250

dst_port = int(dst_port)
src_port = int(src_port)
#print(dst_port, "   ", src_port)

# Create a TCP SYN packet
syn_packet = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags='S')

# Send the TCP SYN packet
send(syn_packet, verbose=1)
print("SENT TCP SYN ", dst_ip, ":", dst_port," and ",src_port)

# Create a TCP ACK packet
ack_packet = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags='A')#, seq=syn_ack_response[TCP].ack, ack=syn_ack_response[TCP].seq + 1)

# Send the ACK packet
send(ack_packet, verbose=1)
print("SENT TCP ACK ", dst_ip, ":", dst_port," and ",src_port)
#comments