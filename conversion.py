# Convert Distance units program - John Gormley Frogduckhybrid

# Centimetre
cm_conversions = {
    'cm' : 1,
    'ft' : 0.0328084,
    'in' : 0.3937008,
    'km' : 0.00001,
    'm' : 0.01,
    'mi' : 0.000006213712,
    'nm' : 0.000005399565,
    'yd' : 0.01093613
}

# Feet
ft_conversions = {
    'cm' : 30.48,
    'ft' : 1,
    'in' : 12,
    'km' : 0.0003048,
    'm' : 0.3048,
    'mi' : 0.0001893939,
    'nm' : 0.0001645788,
    'yd' : 0.3333333333
}

# Inch
in_conversions = {
    'cm' : 2.54,
    'ft' : 0.08333333,
    'in' : 1,
    'km' : 0.0000254,
    'm' : 0.0254,
    'mi' : 0.00001578283,
    'nm' : 0.0000137149,
    'yd' : 0.02777778
}

# Kilometre
km_conversions = {
    'cm' : 100000,
    'ft': 3280.84,
    'in' : 39370.08,
    'km' : 1,
    'm' : 1000,
    'mi' : 0.62137,
    'nm' : 0.5399565,
    'yd' : 1093.613
}

# Metre
m_conversions = {
    'cm' : 100,
    'ft' : 3.28084,
    'in' : 39.37008,
    'km' : 0.001,
    'm' : 1,
    'mi' : 0.0006213712,
    'nm' : 0.0005399565,
    'yd' : 1.093613,
}


# Mile
mi_conversions = {
    'cm' : 160934.4,
    'ft' : 5280,
    'in' : 63360,
    'km' : 1.609344,
    'm' : 1609.344,
    'mi' : 1,
    'nm' : 0.8689758,
    'yd' : 1760
}

# Nautical Mile
nm_conversions = {
    'cm' : 185200.1,
    'ft' : 6076.118,
    'in' : 72913.42,
    'km' : 1.852001,
    'm' : 1852.001,
    'mi' : 1.15078,
    'nm' : 1,
    'yd' : 2025.373
}

# Yard
yd_conversions = {
    'cm' : 91.44,
    'ft' : 3,
    'in' : 36,
    'km' : 0.0009144,
    'm' : 0.9144,
    'mi' : 0.0005681818,
    'nm' : 0.0004937363,
    'yd' : 1
}


# all conversions
conversions = {
    'cm' : cm_conversions,
    'ft' : ft_conversions,
    'in' : in_conversions,
    'km' : km_conversions,
    'm' : m_conversions,
    'mi' : mi_conversions,
    'nm' : nm_conversions,
    'yd' : yd_conversions
}

unit_names = ['cm', 'ft', 'in', 'km', 'm', 'mi', 'nm', 'yd']
# Lambdas
convert = lambda value, input_str, result_str: value * conversions[input_str][result_str]
# print(convert(5, 'mi', 'ft'))

convert_and_print = lambda value, input_str, result_str: print(value, input_str, "=", convert(value, input_str, result_str), result_str)
# convert_and_print(51, 'mi', 'km')


# Interactive function
def convert_interactive():
    print("Unit to convert from?")
    for i in range(len(unit_names)):
        print(i, ": ", unit_names[i])

    input_int = int(input())
    input_str = unit_names[input_int]

    print("Enter Value in ", end = "")
    input_value = int(input(input_str + ": "))

    print("Unit to convert ", input_value, input_str, " to?")
    for i in range(len(unit_names)):
        print(i, ": ", unit_names[i])

    result_int = int(input())
    result_str = unit_names[result_int]

    convert_and_print(input_value, input_str, result_str);


convert_interactive()
