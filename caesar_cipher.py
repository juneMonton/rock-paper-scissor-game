alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift =shift%26

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    # def encrypt(plain_text,shift_amount):


    #     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #     #e.g. 
    #     #plain_text = "hello"
    #     #shift = 5
    #     #cipher_text = "mjqqt"
    #     #print output: "The encoded text is mjqqt"

    #     cipher_text=""
    #     for letter in plain_text:
    #         position=alphabet.index(letter)
    #         new_position=position+shift_amount
    #         new_letter=alphabet[new_position]
    #         cipher_text+=new_letter
    #     print(cipher_text)

    # def decrypt(cipher_text, shift_amount):
    #     plain_text=""
    #     for letter in cipher_text:
    #         position=alphabet.index(letter)
    #         new_position=position-shift_amount
    #         plain_text+=alphabet[new_position]
    #     print(f"The decoded text is {plain_text}")


    # if direction=="encode":
    #     encrypt(plain_text=text,shift_amount=shift)
    # elif direction=="decode":
    #     decrypt(cipher_text=text,shift_amount=shift)



    def caesar(start_text,shift_amount,cipher_direction):
        end_text=""
        if cipher_direction=="decode":
                shift_amount*=-1
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_amount
                end_text+=alphabet[new_position]
            else:
                end_text+=char
        print(f"Here's the {direction}d result: {end_text}")

    caesar(start_text=text, shift_amount=shift,cipher_direction=direction)

    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result=="no":
          should_continue=False
          print("Goodbye!")





    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 