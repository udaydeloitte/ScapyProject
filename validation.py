from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether
from scapy.packet import Raw, Padding
from scapy.utils import rdpcap

from Resources.constant import *

p = rdpcap("dumpfile8.pcap")


def testvalidation():
    udp_seq = 0
    for pkt in p:
        pkt.show()

        assert pkt[Ether].src == Ether_src
        assert pkt[Ether].dst == Ether_dst

        assert pkt[UDP].sport == s_port
        assert pkt[UDP].dport == d_port

        assert pkt[IP].dst == IPdst

        # checksum validation
        assert pkt[UDP].chksum == cal_checksum(pkt[Raw].load + pkt[Padding].load)

        # assert on signature
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[-32:] == signature

        # startpacket
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[:2] == Startofpacket

        # productModel
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[2:6] == Productmodel

        # predata
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[6:26] == predata

        # predata1
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[26:33] == predata1

        # reservedata
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[33:58] == reservedata

        # data1
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[58:58 + 38] == data1

        # crc1
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[96:100] == CRC1

        # data2
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[100:150] == data2

        # crc2
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[150:154] == CRC2

        # udpSequence
        udp_seq += 1
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[-36:-32] == struct.pack("I", udp_seq)
