def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text,shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char)-65 - shift)% 26 +65)
            else:
                decrypted_text += chr((ord(char)-97-shift)%26+97)
        else:
            decrypted_text +=char
    return decrypted_text


def main():
    plaintext = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_cipher(plaintext, shift)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message,shift)
    print("Decrypted Message:",decrypted_message)

if __name__ == "__main__":
    main()
