alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#method 1
# def encrypt():
#     text=input("Enter the message you want to encrypt:\n").lower()
#     shift=int(input("How many shifts you want:\n"))
#     display=""
#     for i in text:
#         index=alphabet.index(i)
#         result=(index+shift)%len(alphabet)
#         display+=alphabet[result]
#     print("Your encrypted message: "+display)

# def decrypt():
#     text=input("Enter the message you want to decrypt:\n").lower()
#     shift=int(input("How many shifts you want:\n"))
#     display=""
#     for i in text:
#         index=alphabet.index(i)
#         result=(index-shift)%len(alphabet)
#         display+=alphabet[result]
#     print("Your decrypted message: "+display)

# over=False
# while not over:
#     direction=input("Type 'encrypt' to encrypt and 'decrypt' to decrypt:  ")
#     again=True
#     while again:
#         if direction=="encrypt":
#             encrypt()
#             again=False
#         if direction=="decrypt":
#             decrypt()
#             again=False
#     question=input("You wanna try again? Type Y for yes and N for no: ")
#     if question=='Y':
#         print("Here you go again")
#         over=False
#     if question=='N':
#         print("thank you!!")
#         over=True


# method 2
def caesar(original_text,shift_amount,encode_decode):
    display=""
    if encode_decode=="decode":
                shift_amount*=-1

    for letter in original_text:
        if letter not in alphabet:
            display+=letter
        else:
            index=alphabet.index(letter)
            result=index + shift_amount
            result=result % len(alphabet)
            display+=alphabet[result]
    print(f"Your {encode_decode}d message is : {display}")

over=False
while not over:
    text=input("enter the message you want to encode or decode:\n").lower()
    question=input("Type 'encode' to encode amd 'decode' to decode:\n").lower()
    shift=int(input("Enter shift number:\n"))
    caesar(text,shift,question)
    try_again=input("Type 'Y' if you wanna go again, and 'N' if you are done: ").lower()
    if try_again=='y':
        print("here you go again")
        over=False
    if try_again=='n':
        over=True
        print("Thank you!")
