import json

response = {
    'state': True,
    'chain': [
        {
            'timestamp': 1719081735.7112288,
            'data': {
                'transferer_public_key': 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwhYr+Ggz0xDTS1Q4SYdoSwgHxdz22OPBETsJUcS6eCi4eG9NDva0xDzDLlNThS0JicPf05CyKVdXfjDZ153wKw==',
                'reciever_public_key': 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEsGFS01VRJrnybmODNsk5sMzTlTdgoWKIpFBxWrq5ZgczY+9tfJOVZLygZGh/4RuQizV6Wnh9vB2nzz42vX5xJQ==',
                'transfer_amount': 100,
                'transferer_minted_token_balance': 0,
                'transferer_donated_token_balance': 0,
                'reciever_minted_token_balance': 0,
                'reciever_donated_token_balance': 0,
                'transferer_balnce': {'minted': 100, 'donated': 100},
                'reciever_balnce': {'minted': 100, 'donated': 100}
            },
            'previous_hash': 'a2ca20cbb8501dd1d199907932b8f9ddbaddcc28c24f2681c8d742feb3c6393a',
            'hash': 'd9ba3ccaccfaca62862eec032551a96985d711a71fc0df882472b9992b2416e1'
        },
        {
            'timestamp': 1719081836.5905597,
            'data': {
                'transferer_public_key': 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwhYr+Ggz0xDTS1Q4SYdoSwgHxdz22OPBETsJUcS6eCi4eG9NDva0xDzDLlNThS0JicPf05CyKVdXfjDZ153wKw==',
                'reciever_public_key': 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEf9Sl4SgieBlB9tQEWwEe3WBp4kvu093xXl6QKnOLo5cWb0wIxiCstxz4zvpx6VB8+2ChN2RFIQSqPEjc4dnOqA==',
                'transfer_amount': 100,
                'transferer_minted_token_balance': 0,
                'transferer_donated_token_balance': 0,
                'reciever_minted_token_balance': 0,
                'reciever_donated_token_balance': 0,
                'transferer_balnce': {'minted': 100, 'donated': 100},
                'reciever_balnce': {'minted': 100, 'donated': 100}
            },
            'previous_hash': 'd9ba3ccaccfaca62862eec032551a96985d711a71fc0df882472b9992b2416e1',
            'hash': 'bf800fee94ce5a1101e49b5f69f4294586a8e8f501850269844426fafda029d6'
        },
        {
            'timestamp': 1719080912.572144,
            'data': {
                'transferer_public_key': '000000000000000000000000000000000',
                'reciever_public_key': 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwhYr+Ggz0xDTS1Q4SYdoSwgHxdz22OPBETsJUcS6eCi4eG9NDva0xDzDLlNThS0JicPf05CyKVdXfjDZ153wKw==',
                'transfer_amount': 1000000000,
                'transferer_balnce': {'minted': 0, 'donated': 1000000000},
                'reciever_balnce': {'minted': 1000000000, 'donated': 0}
            },
            'previous_hash': '0',
            'hash': 'a2ca20cbb8501dd1d199907932b8f9ddbaddcc28c24f2681c8d742feb3c6393a'
        }
    ]
}

response_data = json.dumps(response).encode('utf-8')
print(response_data)


