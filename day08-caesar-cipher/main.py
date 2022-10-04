import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
running = True

def caesar(text, shift, direction):
    encrypted_text = ""
    # check direction and modify shift to negative if decoding
    if direction == "encode":
        print("encoding...")
    elif direction == "decode":
        print("decoding...")
        shift = -shift
    else:
        print("unknown direction")
        return
    # decode or encode the text
    for char in text:
        for idx, letter in enumerate(alphabet):
            if char == letter:
                if (idx + shift) > len(alphabet):
                    encrypted_text += alphabet[idx + shift - len(alphabet)]
                else:
                    encrypted_text += alphabet[idx + shift]
    print(f"The {direction}d text is {encrypted_text}.")

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)

    caesar(text, shift, direction)
    cont = input("Continue? (yes/no) ")
    running = True if cont == "yes" else False\

print("Bye.")
