conversions = {
    'cm' : {
        'cm' : 1,
        'ft' : 0.0328084,
        'in' : 0.3937008,
        'km' : 0.00001,
        'm' : 0.01,
        'mi' : 0.000006213712,
        'nm' : 0.000005399565,
        'yd' : 0.01093613
    },
    'ft' : {
        'cm' : 30.48,
        'ft' : 1,
        'in' : 12,
        'km' : 0.0003048,
        'm' : 0.3048,
        'mi' : 0.0001893939,
        'nm' : 0.0001645788,
        'yd' : 0.3333333333
    },
    'in' : {
        'cm' : 2.54,
        'ft' : 0.08333333,
        'in' : 1,
        'km' : 0.0000254,
        'm' : 0.0254,
        'mi' : 0.00001578283,
        'nm' : 0.0000137149,
        'yd' : 0.02777778
    },
    'km' : {
        'cm' : 100000,
        'ft': 3280.84,
        'in' : 39370.08,
        'km' : 1,
        'm' : 1000,
        'mi' : 0.62137,
        'nm' : 0.5399565,
        'yd' : 1093.613
    },
    'm' : {
        'cm' : 100,
        'ft' : 3.28084,
        'in' : 39.37008,
        'km' : 0.001,
        'm' : 1,
        'mi' : 0.0006213712,
        'nm' : 0.0005399565,
        'yd' : 1.093613,
    },
    'mi' : {
        'cm' : 160934.4,
        'ft' : 5280,
        'in' : 63360,
        'km' : 1.609344,
        'm' : 1609.344,
        'mi' : 1,
        'nm' : 0.8689758,
        'yd' : 1760
    },
    'nm' : {
        'cm' : 185200.1,
        'ft' : 6076.118,
        'in' : 72913.42,
        'km' : 1.852001,
        'm' : 1852.001,
        'mi' : 1.15078,
        'nm' : 1,
        'yd' : 2025.373
    },
    'yd' : {
        'cm' : 91.44,
        'ft' : 3,
        'in' : 36,
        'km' : 0.0009144,
        'm' : 0.9144,
        'mi' : 0.0005681818,
        'nm' : 0.0004937363,
        'yd' : 1
    }
}

# Lambdas
convert = lambda x, input_str, result_str: x * conversions[input_str][result_str]
print(convert(5, 'cm', 'in'))

convert_and_print = lambda value, input_str, result_str: print(value, input_str, "=", convert(value, input_str, result_str), result_str)
convert_and_print(51, 'mi', 'km')

# Interactive function
def convert_interactive():

    unit_list = str(list(conversions.keys()))

    input_str = input("Enters Units to convert from " + unit_list + ": ")

    input_val = int(input( "Enter Value in " + input_str + ": "))

    result_str = input("Enter Unit to convert "+ str(input_val) + input_str + " to " + unit_list + ": ")

    convert_and_print(input_val, input_str, result_str);


convert_interactive()
