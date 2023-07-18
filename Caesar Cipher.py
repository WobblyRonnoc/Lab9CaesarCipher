#Caesar Cipher

substitution_ciper_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
substitution_ciper_b = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

def get_choice():
    choice = input("---------------------------------------------------------------\nWhat would you like to do? (Press enter to continue) \n1. Encrypt a message \n2. Decrypt a message \n3. Crack \nEnter your choice: ")
    return choice

def get_message(option):
    if option == "1":
        message = input("Enter the message to encrypt: ").lower()
    elif option == "2":
        message = input("Enter the message to decrypt: ").lower()
    elif option == "3":
        message = input("Enter the message to crack: ").lower()
    else:
        return None
    return message

def get_key():
    key = int(input("Enter the shift cipher: "))
    while key < 0 or key > 25:
        print("Invalid shift cipher. Please enter a number between 0 and 25")
        key = int(input("Enter the key: "))
    return key

# x = substituted message string list (each letter is an index)
# k = each letter in the message string + key
# y = (x+k) % 26

# Encrypt the message(x) using key(k)
def encrypt(x, k):
    message_list = [*x] #/ *x splits the string into a list of letters
    encrypted_message = [] # empty list to store the encrypted message
    
    for i in range(len(message_list)):
        substituted_letter = substitution_ciper_a[message_list[i]]  # substitute each letter in the message with the corresponding letter in the dictionary
        Y = (substituted_letter + k) % 26 # add the key to the substituted letter and mod 26
        encrypted_message.append(Y) # append the encrypted letter to the empty list
        
    ciper_text = [] # empty list to store the encrypted message as letters
    
    for i in range(len(encrypted_message)):
        encrypted_message[i] = substitution_ciper_b[encrypted_message[i]]
        ciper_text.append(encrypted_message[i])
        
    return ''.join(ciper_text) # join the list of letters into a string

# Decrypt the message(x) using key(k) 
def decrypt(x, k):
    message_list = [*x] #/ *x splits the string into a list of letters
    decrypted_message = [] # empty list to store the decrypted message
    
    for i in range(len(message_list)):
        if message_list[i] == ' ': # keep the space in the decrypted message
            decrypted_message.append(message_list[i]) 
            continue        
        substituted_letter = substitution_ciper_a[message_list[i]]  # substitute each letter in the message with the corresponding letter in the dictionary
        Y = (substituted_letter - k) % 26 # subtract the key to the substituted letter and mod 26
        decrypted_message.append(Y) # append the decrypted letter to the empty list
        
    plain_text = [] 
    
    for i in range(len(decrypted_message)):
        if decrypted_message[i] == ' ':
            plain_text.append(decrypted_message[i]) # keep the space in the decrypted message
            continue
        decrypted_message[i] = substitution_ciper_b[decrypted_message[i]]
        plain_text.append(decrypted_message[i])
        
    return plain_text 

# Crack the message(x) using brute force
#! Diversity is our strength
def crack(message):
    for i in range(26):
        print(f"Key: {i}, Message: {''.join(decrypt(message, i))}")
        

while True:
    choice = get_choice()
    if choice == "1":
        x = get_message(choice)
        k = get_key()
        print(f"Encrypted Message: {encrypt(x, k)}")
        break
    elif choice == "2":
        x = get_message(choice)
        k = get_key()
        print(f"Decrypted Message: {decrypt(x, k)}")
        break
    elif choice == "3":
        x = get_message(choice)
        crack(x)
    else:
        exit(0)


