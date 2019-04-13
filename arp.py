# pip install pyshark
import pyshark

capture = pyshark.LiveCapture(interface='eth0')

while(1):
 capture.sniff(packet_count=1)
 for packet in capture:
  print (packet)
