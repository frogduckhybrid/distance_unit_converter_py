import json

conversions = json.load(open("conversions.json"))

# Lambdas
convert = lambda x, input_str, result_str: x * conversions[input_str][result_str]

convert_and_print = lambda x, input_str, result_str: print(x, input_str, "=", convert(x, input_str, result_str), result_str)

# Interactive function
def convert_interactive():

    unit_list = ', '.join(conversions.keys())

    input_str = input("Enter unit to convert from [ " + unit_list + " ]: ")

    input_val = int(input( "Enter Value in " + input_str + ": "))

    inner_unit_list = ', '.join(conversions[input_str].keys())

    result_str = input("Enter unit to convert "+ str(input_val) + input_str + " to [ " + inner_unit_list + " ]: ")

    convert_and_print(input_val, input_str, result_str)

convert_interactive()
