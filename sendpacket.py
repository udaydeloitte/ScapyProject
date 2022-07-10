
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp

from Resources.constant import *


data = payload()
print("Length of data: ", len(data))

checksum = cal_checksum(data)
print("This is checksum: ", checksum)
# https://www.programcreek.com/python/?CodeExample=compute+checksum


def pkt_being_Send():
    packet = Ether() / IP() / UDP() / Raw()

    packet[Ether].src = Ether_src
    packet[Ether].dst = Ether_dst

    packet[UDP].sport = s_port
    packet[UDP].dport = d_port
    packet[UDP].len = len(data)
    packet[UDP].chksum = checksum

    packet[IP].dst = IPdst
    packet[IP].chksum = checksum

    packet[Raw].load = data
    return packet


packet = pkt_being_Send()
packet.show()

sent = 0

while True:

    print(packet)

    sendp(packet)


    # time.sleep(0.1)

    sent += 1
    if sent == no_of_packets:
        break
