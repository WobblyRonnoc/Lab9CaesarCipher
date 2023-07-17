#Caesar Cipher

substitution_ciper_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
substitution_ciper_b = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

message = input("Enter the message to encrypt: ").lower()

key = int(input("Enter the shift cipher: "))
while key < 0 or key > 25:
    print("Invalid shift cipher. Please enter a number between 0 and 25")
    key = int(input("Enter the key: "))


# x = substituted message string list (each letter is an index)
# k = each letter in the message string + key
# y = (x+k) % 26

# Encrypt the message using key
def enrypt(x, k):
    message_list = [*x] #? *x splits the string into a list of letters
    encrypted_message = [] #? empty list to store the encrypted message
    
    for i in range(len(message_list) - 1):
        substituted_letter = substitution_ciper_a[message_list[i]]  #? substitute each letter in the message with the corresponding letter in the dictionary
        Y = (substituted_letter + k) % 26 #? add the key to the substituted letter and mod 26
        print(Y)
        encrypted_message.append(Y) #? append the encrypted letter to the empty list
        
encrypted_message = enrypt(message, key)
print(encrypted_message)