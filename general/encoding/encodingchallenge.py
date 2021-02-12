from socket import socket
import json
import base64
import codecs

# hex -> 37412e17
# ascii -> int[]
# bigint -> 0xdeadbeef
# rot13 -> thuyashtrua_eawe_
# base64 -> d2ltcGxlc19w

# Setup socket connection
sock = socket()
sock.connect(("socket.cryptohack.org", 13377))

steps = 100

# steps + 1, so that we could see the flag after the last decoding iteration
for s in range(steps + 1):
    # Receive the message and parse into dictionary
    msg = sock.recv(1024).decode()
    json_data = json.loads(msg)
    print(json_data)
    
    enc_type = json_data['type']
    enc_data = json_data['encoded']
    dec_data = ""

    # Do the conversions
    if enc_type == "hex":
        # Hex strings to bytearray
        dec_data = bytes.fromhex(enc_data).decode("utf-8")
    elif enc_type == "ascii":
        # Convert integers to ordinal bytes
        for i in enc_data:
            dec_data += chr(i)
    elif enc_type == "bigint":
        # Convert raw hex to byte array
        dec_data = bytes.fromhex(enc_data[2:]).decode("utf-8")
    elif enc_type == "rot13":
        # Decode rot13 using codecs lib
        dec_data = codecs.decode(enc_data, "rot_13")
    elif enc_type == "base64":
        # Decode base64 using base64 lib
        dec_data = base64.b64decode(enc_data).decode("utf-8")

    # Build reply body
    reply = "{\"type\": \"%s\", \"decoded\": \"%s\"}" % (enc_type, dec_data)
    print(reply)
    sock.send(reply.encode())