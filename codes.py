# issue with TShark subprocess parameters
# https://github.com/KimiNewt/pyshark/issues/299

capture.sniff(packet_count=3)
for packet in capture.sniff_continuously(packet_count=3):
  #cleaning the output
  string = str(packet.arp)
  string = string.split('Sender IP address:')[1]
  string = string.split('Target MAC')[0]
  string = string.strip()
  print(string)

# working part - return ip value one by one

def print_callback(packet):
    # cleaning the output
    string = str(packet.arp)
    string = string.split('Sender IP address:')[1]
    string = string.split('Target MAC')[0]
    string = string.strip()
    print(string)
capture.apply_on_packets(print_callback, packet_count=5)