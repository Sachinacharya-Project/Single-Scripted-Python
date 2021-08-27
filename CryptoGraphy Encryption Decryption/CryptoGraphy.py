from cryptography.fernet import Fernet

def EncryptData():
    #this generates a key and opens a file 'key.key' and writes the key there
    key = Fernet.generate_key()

    with open('fernet.key', 'wb') as file:
        file.write(key)

    # this just opens your 'key.key' and assings the key stored there as 'key'
    with open('fernet.key','rb') as file:
        key = file.read()

    #this opens your json and reads its data into a new variable called 'data'
    with open('filename.json','rb') as f:
        data = f.read()

    #this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    #this writes your new, encrypted data into a new JSON file
    with open('filename.json','wb') as f:
        f.write(encrypted)
def DecryptData():
    #this just opens your 'key.key' and assings the key stored there as 'key'
    with open('fernet.key','rb') as file:
        key = file.read()

    #this opens your json and reads its data into a new variable called 'data'
    with open('filename.json','rb') as f:
        data = f.read()

    #this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    #this writes your new, encrypted data into a new JSON file
    with open('filename.json','wb') as f:
        f.write(decrypted)
input("Encrypt...")
EncryptData()
input("Decrypt...")
DecryptData()