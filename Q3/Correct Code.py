# ____________________ correction for encrypted file ____________________

global_variable = 100

# Define a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# Function to process numbers
def process_numbers():
    global global_variable
    local_variable = 15
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.append(local_variable)
        local_variable -= 1

    return numbers


my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

result = process_numbers()


# Function to modify the dictionary
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable


# Call the modify_dict function
# fixed -> removing unwanted args.

modify_dict()


# Function to change the global variable
def change_global():
    global global_variable
    global_variable += 10


# Loop to print numbers
for i in range(5):
    print(i)
    i += 1
# Check conditions and print messages
if 5 not in my_set and my_dict.get('key4') == 10:
    print("Conditional met!")

if 5 not in my_set:
    print("5 not found in the set!")

# Print the global variable, dictionary, and set value
print("Global Variable:", global_variable)
print("Dictionary:", my_dict)
print("Set:", my_set)
