# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487

big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 # b10

# Convert to hex b16 string
hex_data = hex(big_integer)

# Omit the '0x' from the raw hex data
# Convert to byte array
byte_data = bytes.fromhex(hex_data[2:])

print(byte_data.decode("utf-8"))