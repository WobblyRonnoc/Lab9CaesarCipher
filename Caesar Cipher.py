#Caesar Cipher

substitution_ciper_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
substitution_ciper_b = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

print(f"{'-'*28}\n| Welcome to Caesar Cipher |\n{'-'*28}")
def get_choice():
    try:
        choice = input("\n1. Encrypt a message \n2. Decrypt a message \n3. Crack \n4. Exit \nEnter your choice: ")
        if choice not in ["1", "2", "3", "4"]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a valid choice.")
        return get_choice()
    return choice

def get_message():
    message = input("Enter the message to encrypt: ").lower()
    return message

def get_encrypted_message():
    message = input("Enter the message to decrypt: ").lower()
    return message

def get_message_to_crack():
    message = input("Enter the message to crack: ").lower()
    return message

# returns a valid key (0 - 25)
def get_key(): 
    while True:
        try:
            key = int(input("Enter the key: "))
            if key < 0 or key > 25:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid key. Key must be an integer between 0 and 25.")
    return key

#* x = substituted message string list (each letter is an index)
#* k = each letter in the message string + key
#* y = (x+k) % 26

# Encrypt the message(x) using key(k)
def encrypt(x, k):
    message_list = [*x] #/ split the string into a list of letters
    encrypted_message = [] # empty list to store the encrypted message
    ciper_text = [] # empty list to store the encrypted message as letters


    for i in range(len(message_list)):
        substituted_letter = substitution_ciper_a[message_list[i]]  # substitute each letter in the message with the corresponding letter in the dictionary
        Y = (substituted_letter + k) % 26 # add the key to the substituted letter and mod 26
        encrypted_message.append(Y) # append the encrypted letter to the empty list
        
    
    for i in range(len(encrypted_message)):
        encrypted_message[i] = substitution_ciper_b[encrypted_message[i]]
        ciper_text.append(encrypted_message[i])
        
    return ''.join(ciper_text) # join the list of letters into a string

# Decrypt the message(x) using key(k) 
def decrypt(x, k):
    message_list = [*x] # split the string into a list of letters
    decrypted_message = [] # empty list to store the decrypted message
    plain_text = [] # empty list to store the decrypted message as letters 

    # keep the space in the decrypted message
    for i in range(len(message_list)):
        if message_list[i] == ' ': 
            decrypted_message.append(message_list[i]) 
            continue        
        
        substituted_letter = substitution_ciper_a[message_list[i]] 
        Y = (substituted_letter - k) % 26 
        decrypted_message.append(Y) 
        
    
    # keep the space in the decrypted message
    for i in range(len(decrypted_message)):
        if decrypted_message[i] == ' ':
            plain_text.append(decrypted_message[i])
            continue 
        
        decrypted_message[i] = substitution_ciper_b[decrypted_message[i]] 
        plain_text.append(decrypted_message[i]) 
        
    return plain_text 

# Crack the message(x) using brute force
#! QVIREFVGL ZJ DJG LMKXGZMA
#! diversity is our strength
def crack(message):
    m_length = len(message)
    print("\nCracking the message...\n")
    print(f"{'DECRYPTED MESSAGE'.center(m_length,'=')} | KEY")
    for i in range(26):
        print(f"{''.join(decrypt(message, i))} | {i}")

# Print the result 
# accept a string as an argument
def print_result(title, result_string):
    border = '-' * (len(result_string) + 3) # create a border of dashes adjusting for the length of the string
    print(f"\n{title}\n{border}\n| {result_string} |\n{border}") # print the result string with a border


# Main program
while True:
    choice = get_choice()
    if choice == "1":
        x = get_message()
        k = get_key()
        print_result("Encrypted Message", encrypt(x, k))
    elif choice == "2":
        x = get_encrypted_message()
        k = get_key()
        print_result(f"Decrypted Message", ''.join(decrypt(x, k)))
    elif choice == "3":
        x = get_message_to_crack()
        crack(x)
    else:
        # any other choice, exit the program
        print("Goodbye!")
        exit(0)


