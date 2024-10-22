from cryptography.fernet import Fernet

def create_key(key_name='key.key'):
    """
    Makes a key that is saved to a file.
    """
    key = Fernet.generate_key()
    with open(key_name, 'wb') as key_file:
        key_file.write(key)
    print(f"Key saved to {key_name}")

if __name__ == "__main__":
    create_key()  
