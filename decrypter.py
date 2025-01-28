import os
import pyaes

path = os.getcwd()
files_name = [f for f in os.listdir() if f.endswith('.txt.ransomware')]
key = b"testeransomwares"

for file_name in files_name:
    with open(file_name, 'rb') as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    original_file = file_name.replace('.ransomware', '')
    with open(original_file, 'wb') as file:
        file.write(decrypt_data)
    os.remove(file_name)