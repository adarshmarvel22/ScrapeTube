

def extract_number(string):
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(char)
        else:
            continue
    if numbers:
        extracted_number = int("".join(numbers))
    return extracted_number