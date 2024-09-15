def separate_and_convert(s):
    # Separate numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values_even_numbers = [ord(str(num)) for num in even_numbers]

    # Convert upper-case letters to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_values_upper_case_letters = [ord(char) for char in upper_case_letters]

    return ''.join(map(str, number_string)),''.join(map(str, letter_string)),''.join(map(str, even_numbers)), ''.join(map(str, upper_case_letters)), ascii_values_even_numbers, ascii_values_upper_case_letters

# Example usage
input_string = '56aAww1984sktr235270aYmn145ss785fssq31D0'
result_number_string, result_letter_string, result_even_numbers, result_Upper_Case_letters, ascii_even_numbers, ascii_upper_case_letters = separate_and_convert(input_string)

print("Number String", result_number_string)
print("Letter String", result_letter_string)
print("Even Number String:", result_even_numbers)
print("Upper-case Letter String:", result_Upper_Case_letters)
print("ASCII Values of Even Numbers:", ascii_even_numbers)
print("ASCII Values of Upper-case Letters:", ascii_upper_case_letters)
