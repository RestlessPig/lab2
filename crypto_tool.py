from cryptography.fernet import Fernet
import argparse

def load_key(key_name='key.key'):
    """
    Loads the already created key from a specified file.
    """
    with open(key_name, 'rb') as key_file: 
        key = key_file.read()
    print(f"Loaded key: {key.decode()}")  
    return key

def encrypt(filename, key):
    """
    Encrypts the given file with the loaded key and overwrites it.
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        print(f"Data to encrypt: {file_data}")

    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

    print("File is now encrypted.")
    print(f"Encrypted data: {encrypted_data}")

def decrypt(filename, key):
    """
    Decrypts a file with an existing key.
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
        print(f"Encrypted data to decrypt: {encrypted_data}")

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, 'wb') as file:
        file.write(decrypted_data)

    print("File is now decrypted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encryptor Script")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file

    key = load_key()  # Load the key

    if args.encrypt and args.decrypt:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif args.encrypt:
        encrypt(file, key)
    elif args.decrypt:
        decrypt(file, key)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")