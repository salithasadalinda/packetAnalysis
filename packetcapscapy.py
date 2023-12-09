from scapy.all import *
from scapy.all import rdpcap
from scapy.layers.inet import UDP

packets = sniff(count=10)
print(packets.summary())


# print(IFACES.show())