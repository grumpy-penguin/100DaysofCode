from art import logo

def caesar(string, shift_amount, cipher_direction):

    out_string = ""

    if shift_amount >= int(len(alphabet) / 2 ):
        shift_amount = shift_amount % int(len(alphabet) / 2 )

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in string:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_position = char_index + shift_amount
            out_string += alphabet[new_position]
        else:
            out_string += char

    print(f"The {cipher_direction}d text is {out_string}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

rerun=True

while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypted_string = ""

    caesar(string=text, shift_amount=shift, cipher_direction=direction)
    restart=input("Would you like to encode or decode another message? Yes or No?\n")
    if restart == "Yes" or restart == "yes" or restart =="Y" or restart == "y":
        rerun = True
    else:
        rerun = False
        print("Goodbye")
