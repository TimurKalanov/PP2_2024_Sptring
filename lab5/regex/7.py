def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string
def convert_snake_to_camel(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        snake_case_input = input_file.read().strip()
    camel_case_output = snake_to_camel(snake_case_input)
    print("Camel case:", camel_case_output)
input_filename = 'row.txt'
convert_snake_to_camel(input_filename)
