# pip install pyshark
# TShark required
import pyshark

# type: ARP (0x0806)
capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='ether proto 0x0806')

# while(1):
capture.sniff(packet_count=1)
for packet in capture:
  print (packet.arp)
