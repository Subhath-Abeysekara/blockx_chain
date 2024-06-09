def validate_inputs(schema , body):
    body = schema.dump(body)
    errors = schema.validate(body)
    if errors:
        raise Exception(str(errors))
    return body