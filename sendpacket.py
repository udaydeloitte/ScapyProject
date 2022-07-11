from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp
import time
from Resources.constant import *

# checksum computation
# https://www.programcreek.com/python/?CodeExample=compute+checksum

sent = 0
udpsequence = 0
while True:
    # data
    data = payload()

    # Time
    data += gettime()

    # Timestamp
    data += Timestamp

    # udpSequence
    udpsequence += 1
    data += struct.pack("I", udpsequence)

    # Signature
    data += signature

    print("Length of data: ", len(data))

    # Checksum
    checksum = cal_checksum(data)

    # create packet
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

    # print(packet)
    packet.show()
    sendp(packet)

    # time.sleep(0.1)

    sent += 1
    print("no. of packets: ", sent)
