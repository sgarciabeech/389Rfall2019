#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

SECTION_ASCII = 0x1
SECTION_UTF8 = 0x2
SECTION_WORDS = 0x3
SECTION_DWORDS = 0x4
SECTION_DOUBLES = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG = 0x8
SECTION_GIF87 = 0x9
SECTION_GIF89 = 0xA

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
idx = 0

magic, version = struct.unpack("<LL", data[idx:(idx + 8)])
idx += 8
time = struct.unpack("<L", data[idx:(idx + 4)])[0]
idx += 4
author = struct.unpack(">cccccccc", data[idx:(idx + 8)])
idx += 8
sections = struct.unpack("<L", data[idx:(idx + 4)])[0]
idx += 4

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

try:
    time = datetime.datetime.fromtimestamp(time)
except:
    bork("Time is not a valid UNIX timestamp! - %d" % int(time[0]))

if sections <= 0:
    bork("Not enough sections! Got %d, should be more than 0" % int(sections))

print("------- HEADER -------")
print("Magic: %s" % hex(magic))
print("Version: %d" % int(version))
print("Date: %s" % time)
print("Author: %s" % "".join(author))
print("Number of sections: %d " % sections)


print("-------  BODY  -------")

for i in range(1, sections + 1):
    stype, slen = struct.unpack("<LL", data[idx:(idx + 8)])
    idx += 8

    print("-----Section %d------" % i)
    print("Section type: %d" % int(stype))
    print("Section length: %d" % int(slen))

    if stype == 0:
        idx += int(slen)

    elif stype == SECTION_ASCII or stype == SECTION_UTF8:
        format_string = ">" + ("c" * slen)
        output = struct.unpack(format_string, data[idx:(idx + slen)])
        idx += slen

        print("".join(output))

    elif stype == SECTION_WORDS or stype == SECTION_DWORDS:
        offset = 8
        if stype == SECTION_WORDS:
            offset = 4

        output = ""
        words_num = slen / offset

        for i in range(0, words_num):
            word = struct.unpack(">L", data[idx:(idx + offset)])[0]

            output += str(word) + " "
            idx += offset

        print(output)

    elif stype == SECTION_DOUBLES:
        output = "["
        words_num = slen / 4

        for i in range(0, words_num):
            word = struct.unpack(">d", data[idx:(idx + 4)])[0]

            output += str(word) + " "
            idx += 4

        print(output + "]")

    elif stype == SECTION_COORD:
        if slen != 16:
            bork("Slen is %d, should be 16" % int(slen))
        else:
            lat, lon = struct.unpack("<dd", data[idx:(idx + 16)])
            idx += 16
            print("Coordinates: %f, %f" % (lat, lon))

    elif stype == SECTION_REFERENCE:
        ref = struct.unpack(">L", data[idx:(idx + 4)])[0]
        idx += 4

        print("Section reference: %d" % int(ref))

    elif stype in [SECTION_PNG, SECTION_GIF87, SECTION_GIF89]:
        sig = []
        file_name = ""

        if stype == SECTION_PNG:
            #png_sig = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
            sig = [137, 80, 78, 71, 13, 10, 26, 10]
            file_name = "fpffImage.png"
        elif stype == SECTION_GIF87:
            sig = [47, 49, 46, 38, 37, 61]
            file_name = "fpffImage.gif"
        else:
            sig = [47, 49, 46, 38, 39, 61]
            file_name = "fpffImage.gif"

        iter = slen / 4
        output = ""

        fh = open(file_name, "wb")
        fh.write(bytearray(sig))

        for i in range(0, iter):
            output += str(struct.unpack("!I", data[idx:(idx + 4)])[0])
            idx += 4

        fh.write(output.decode('base64'))

        #png_iend = [73, 69, 78, 68]
        #fh.write(bytearray(png_iend))

        fh.close()

    else:
        bork("Stype %d is not an approved type! " % int(stype))
