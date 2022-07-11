import json

from ast import literal_eval

from Resources.constant import *

# Opening JSON file
f = open('JsonValidation.json')

# returns JSON object as
# a dictionary
jsondata = json.load(f)


def testnoofpackets():
    assert len(jsondata) == no_of_packets


def testjsondatavalidate():
    for i in jsondata:
        assert i["_source"]["layers"]["eth"]["eth.dst"] == Ether_dst

        assert i["_source"]["layers"]["eth"]["eth.src"] == Ether_src

        assert i["_source"]["layers"]["udp"]["udp.srcport"] == str(int(s_port))

        assert i["_source"]["layers"]["udp"]["udp.dstport"] == str(int(d_port))

        # checksum validation
        assert literal_eval(i["_source"]["layers"]["udp"]["udp.checksum"]) == cal_checksum(
            convert_str_bytes(i["_source"]["layers"]["udp"]["udp.payload"]))




# Closing file
f.close()
