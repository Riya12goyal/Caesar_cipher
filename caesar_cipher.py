#encoding_decoding
#each alphabet of the actual word is shifted by a number ahead
# A B C D E
# D E F G H  (shift 3)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    cipher_text =""
    for letter in text:
        if letter in alphabet:
            ind = alphabet.index(letter)
            new_ind = ind + shift
            if new_ind > 25:
                new_ind = new_ind - 26
            new_letter = alphabet[new_ind]
            cipher_text = cipher_text + new_letter
        else:
            cipher_text = cipher_text + letter
    print(f"the encrypted text is {cipher_text}")



def decrypt(text, shift):
    decrypt_text = ""
    for letter in text:
        if letter in alphabet:
            ind = alphabet.index(letter)
            new_in = ind - shift
            if new_in < 0:
                new_in = 26 + new_in
            decrypt_text = decrypt_text + alphabet[new_in]
        else:
            decrypt_text = decrypt_text + letter
    print(f"the decrypted text is : {decrypt_text}")

again = "yes"
while again == "yes":
    option = input("choose an option: encode/ decode\n"). lower()
    msg = input("type your message\n").lower()
    num = int(input("type shift number\n"))
    num = num%25
    if option == "encode":
        encrypt(msg,num)
    elif option == "decode":
        decrypt(msg,num)
    again = input("Do you want to do it again (yes/no)\n")

print("good bye!")
