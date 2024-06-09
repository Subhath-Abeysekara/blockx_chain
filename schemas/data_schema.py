from marshmallow import Schema, fields , validate

class Transaction_Data(Schema):
    transferer_public_key = fields.Str(required=True)
    reciever_public_key = fields.Str(required=True)
    transfer_amount = fields.Int(required=True)
    transferer_minted_token_balance = fields.Int(dump_default=0)
    transferer_donated_token_balance = fields.Int(dump_default=0)
    reciever_minted_token_balance = fields.Int(dump_default=0)
    reciever_donated_token_balance = fields.Int(dump_default=0)

class Data(Schema):
    headers = fields.Dict(required=True)
    data = fields.Dict(required=True)