raw = "label"
# XOR against each ordinal repr of each character in string
xor_result = [(ord(c) ^ 13) for c in raw]

# Convert ordinal repr into ASCII string
flag = ''.join([chr(x) for x in xor_result])

print("crypto{%s}" % flag)