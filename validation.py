from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether
from scapy.packet import Raw, Padding
from scapy.utils import rdpcap

from Resources.constant import *

p = rdpcap("dumpfile5.pcap")


def testpackets():
    assert len(p) == no_of_packets


def testvalidation():
    for pkt in p:
        pkt.show()

        assert pkt[Ether].src == Ether_src
        assert pkt[Ether].dst == Ether_dst

        assert pkt[UDP].sport == s_port
        assert pkt[UDP].dport == d_port

        assert pkt[IP].dst == IPdst

        assert pkt[UDP].chksum == cal_checksum(pkt[Raw].load + pkt[Padding].load)

        # assert on signature
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[-32:] == data[-32:]

        # remaining matching data
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[:len(data) - 44] == data[:len(data) - 44]

        # Not matching data
        assert bytearray(pkt[Raw].load + pkt[Padding].load)[-45:-33] != data[-45:-33]
