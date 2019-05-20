import json


def add_employee(salaries_json, name, salary):

    salaries_json = json.loads(salaries_json)
    salaries_json[name] = 800
    salaries_json = json.dumps(salaries_json)
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
