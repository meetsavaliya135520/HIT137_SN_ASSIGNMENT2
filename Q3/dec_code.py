def encrypt(text, key):
    enc_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            enc_text += chr(shifted)
        else:
            enc_text += char

    return enc_text


def read_encrypted_file():
    file_path = "enc_code.txt"

    # Read the contents of the file and store them in a variable
    with open(file_path, 'r', encoding='utf-8') as file:
        encrypted_text = file.read()

    return encrypted_text


key1 = -13  # key for decryption
encrypted_text = read_encrypted_file()

# store text to a variable

decrypted_text = encrypt(encrypted_text, key1)
print(decrypted_text)

