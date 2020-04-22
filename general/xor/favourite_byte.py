raw = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytearray.fromhex(raw)

def xor(bytes_arr, key):
    return bytes(b ^ key for b in bytes_arr)

# Bytes 0 to 255(0x00 to 0xff)
for key in range(256):
    result = xor(cipher_bytes, key).decode("utf-8")
    
    if (result.startswith("crypto")):
        print(result)
        break