import sys
import os
import struct

"""
Reading from Java DataInputStream format.
"""
class DataInputStream:
    def __init__(self, stream):
        self.stream = stream

    def read_boolean(self):
        return struct.unpack('?', self.stream.read(1))[0]

    def read_byte(self):
        return struct.unpack('b', self.stream.read(1))[0]

    def read_unsigned_byte(self):
        return struct.unpack('B', self.stream.read(1))[0]

    def read_char(self):
        return chr(struct.unpack('>H', self.stream.read(2))[0])

    def read_double(self):
        return struct.unpack('>d', self.stream.read(8))[0]

    def read_float(self):
        return struct.unpack('>f', self.stream.read(4))[0]

    def read_short(self):
        return struct.unpack('>h', self.stream.read(2))[0]

    def read_unsigned_short(self):
        return struct.unpack('>H', self.stream.read(2))[0]

    def read_long(self):
        return struct.unpack('>q', self.stream.read(8))[0]

    def read_utf(self):
        utf_length = struct.unpack('>H', self.stream.read(2))[0]
        return self.stream.read(utf_length)

    def read_int(self):
        return struct.unpack('>i', self.stream.read(4))[0]


def bin_trans(bin_file_path):
    bin_f = open(bin_file_path, 'rb')
    dis = DataInputStream(bin_f);
    model_name = dis.read_utf().decode("utf8")
    model_V = dis.read_int()
    model_b = dis.read_float()
    print('\t'.join([model_name, str(model_V), str(model_b)]))
    fSize = dis.read_int()
    model_featureMap = {}

    for f in range(fSize):
        fName = dis.read_utf().decode("utf8")
        fw = dis.read_float()
        fv = []

        for i in range(model_V):
            fv.append(str(dis.read_float()))

        print ('\t'.join([fName, str(fw), ','.join(fv)]))

if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + " bin_file_path")
        exit(1)
    bin_file_path = sys.argv[1].strip()
    bin_trans(bin_file_path)
