import zlib

from Resources.data import *
import datetime

Ether_src = "00:23:69:3a:f4:7d"
Ether_dst = "90:2b:34:60:dc:2f"

s_port = 0x2710
d_port = 0x2368

IPdst = "127.0.0.2"
IPsrc = "127.0.0.1"
data2 = data2()

crc_2 = zlib.crc32(data2)
CRC2 = struct.pack('I', crc_2)

data1 = data1()

crc_1 = zlib.crc32(data2)
CRC1 = struct.pack('I', crc_2)


# System current Time
def gettime():
    now = datetime.datetime.now()
    Time = now.year - 1900, now.month, now.day, now.hour, now.minute, now.second
    Time = bytearray(Time)
    return Time


Time = gettime()

Timestamp = Timestamps()

Productmodel = productmodel()

Startofpacket = bytearray([0xEE, 0xFF])

predata = predata()

predata1 = predata1()

reservedata = reservedata()

# udpsequence = udp_sequence()

#  Taking Input for signature
signature = signature()


def payload():
    payload_data = Startofpacket + Productmodel + predata + predata1 + reservedata + data1 + CRC1 + data2 + CRC2
    return payload_data


data = payload()


def cal_checksum(data):
    checksum = 0
    for byte in data:
        checksum ^= byte

    return checksum
# https://www.programcreek.com/python/?CodeExample=compute+checksum


def convert_str_bytes(data):
    bytes = data.split(":")
    str_ = ""
    for i in range(len(bytes)):
        str_ = str_ + '\\x' + bytes[i]

    bytes_double_slash = str_.encode()
    bytes_single_slash = bytes_double_slash.decode('unicode-escape').encode('ISO-8859-1')

    return bytes_single_slash
