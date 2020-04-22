raw = "label"
xor_result = [(ord(c) ^ 13) for c in raw]
flag = ''.join([chr(x) for x in xor_result])

print("crypto{%s}" % flag)