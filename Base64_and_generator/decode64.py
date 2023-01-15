# Base64 decoder

import base64

example1 = "Raz dwa trzy i cztery"
example2 = " moj nr indexu to 76103"


# decoding from Base64
def decode_from_Base64(to_decode_ascii):
    base64_decode_bytes = base64.b64decode(to_decode_ascii)
    basse64_string_bytes = base64_decode_bytes.decode("ascii")
    return basse64_string_bytes

# encoding to Base64 
def encode_to_Base64(to_base64_string):
    string_to_encode = to_base64_string.encode("ascii")
    base64_encoded_bytes = base64.b64encode(string_to_encode)
    base64_encoded_ascii = base64_encoded_bytes.decode("ascii")
    return base64_encoded_ascii


# TEST 1 - example1
# coding to Base64
print("Przyklad 2")
print(example1)
print("... encoding to Base64 ...")
encoding_result = encode_to_Base64(example1)
print("Result: ")
print(encoding_result)
# decoding to base64
print("decoding from Base64 ...")
print(decode_from_Base64(encoding_result))


# TEST 1 - example2
# coding to Base64
print("Przyklad 2")
print(example2)
print("... encoding to Base64 ...")
encoding_result = encode_to_Base64(example2)
print("Result: ")
print(encoding_result)
# decoding to base64
print("decoding from Base64 ...")
print(decode_from_Base64(encoding_result))

