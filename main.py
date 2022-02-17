from cryptography.fernet import Fernet

def write_key():
  
    #Generates a key and save it into a file
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    
    #Loads the key from the current directory named `key.key`
    
    return open("key.key", "rb").read()



def encrypt(filename, key):
    
    #Given a filename (str) and key (bytes), it encrypts the file and write it
    
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):

    #Given a filename (str) and key (bytes), it decrypts the file and write it
    
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)





def main():
    choice = input("Enter your choice, E to Encrypt Or D to Decrypt : ")
    if choice == 'E' or choice=='e':
        # file name
        file = input("Enter the name of File to Encrypt : ")
        #generate key
        write_key()
        # load the key
        key = load_key()
        encrypt(file,key)
        print(file,"Encrypted")
    elif choice =='D' or choice =='d':
        file = input("Enter the name of File to Encrypt : ")
        #decrypt(file,key)
        key = load_key()
        decrypt(file, key)
        print("Decrypted",file)
    else:
        print("Invalid Choce")

main()

