import json

# Byte string
byte_string = b'{"transferer_public_key": "", "reciever_public_key": "", "transfer_amount": 10}'

# Decode the byte string to a regular string
json_string = byte_string.decode('utf-8')

# Parse the JSON string to a dictionary
data = json.loads(json_string)

print(data)
