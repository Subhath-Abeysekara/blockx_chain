def execute_contract_code(contract_id, method, *parameters):
    with open(f'{contract_id}.txt', 'r') as file:
        function_code = file.read()
    exec(function_code, globals())
    if method in globals():
        func = globals()[method]
        result = func(*parameters)
        print(result)
        return result
    else:
        print(f"The function '{method}' is not defined.")

# response = execute_contract_code("contract", "add_node")
# print(response)

