import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert hex string to byte array then encode to base64
byte_data = bytes.fromhex(hex_string)
b64_data = base64.b64encode(byte_data)

print(b64_data.decode("utf-8"))