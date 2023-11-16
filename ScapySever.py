from scapy.all import IP, TCP, send, sniff

# Function to handle incoming SYN packets and send SYN-ACK responses
def syn_packet_handler(packet):
    packet.show()
    if packet[IP].src == "10.1.2.4" and packet[TCP].flags == 2:
        # Build the TCP SYN-ACK response
        syn_ack_response = IP(src=packet[IP].dst, dst=packet[IP].src) / TCP(sport=packet[TCP].dport, dport=packet[TCP].sport, flags='SA')

        # Send the SYN-ACK response
        send(syn_ack_response, verbose=0)

    if TCP in packet and packet[IP].src == "10.1.2.4" and packet[TCP].flags == 4:
        print("TCP RST from Dest")
        #write tcp stream to PCAP? how to capture?

# Start sniffing for incoming SYN packets, ignore my ssh connection
sniff(filter="tcp and host 10.1.2.4 and not port 22", prn=syn_packet_handler, store=0)