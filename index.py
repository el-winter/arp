# pip install pyshark
# TShark required
import pyshark
import operator

interface='Беспроводная сеть'
lst = []
dct = {}

# type: ARP (0x0806)
capture = pyshark.LiveCapture(interface, bpf_filter='ether proto 0x0806')
capture.sniff(packet_count=10)

for packet in capture:
  #cleaning the output
  string = str(packet.arp)
  string = string.split('Sender IP address:')[1]
  string = string.split('Target MAC')[0]
  string = string.strip()

  lst.append(string)

# list -> dictionary {"ip": number}
for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1 

# sorted output
for i in sorted(dct, reverse=True):
    print(dct[i], i)