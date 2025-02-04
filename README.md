# Encrypter & Decrypter

This project consists of two Python scripts for encrypting and decrypting text files using the AES algorithm in CTR mode. It is ideal for those who want to understand how to encrypt files simply by implementing their own encryption keys.

## 🚀 Functionality

**Encrypter (encrypter.py):** Encrypts `.txt` files in the current directory, generating an encrypted version with the `.txt.ransomware` extension.

**Decrypter (decrypter.py):** Decrypts `.txt.ransomware` files, restoring the original files.

## 🔐 How It Works

Both scripts use the AES algorithm with the fixed key `testeransomwares` in CTR mode.

- The **encrypter** reads `.txt` files, encrypts their content, saves them as a new `.ransomware` file, and deletes the original file.
- The **decrypter** reads `.ransomware` files, decrypts them, and restores the files to `.txt` format.

## 📝 Test File Generation: `create_txt.py`

The `create_txt.py` script is designed to automatically generate test text files in the current directory, filled with generic content, for use in encryption and decryption tests. It simplifies validating the functionality of the `encrypter.py` and `decrypter.py` scripts by creating `.txt` files that can be encrypted and later decrypted.

### How It Works:
1. **Test File Generation:** The script creates a series of text files, such as `passwords.txt`, `bank_accounts.txt`, and more, filled with fictional data.
2. **Usage in Test Flow:** After running the script, you will have files that can be used as input for the encryption process (`encrypter.py`) and later for decryption (`decrypter.py`).

## 🚀 How to Run

### Prerequisites:
- Python 3.x
- `pyaes` library

### Steps to Run:

1. Clone this repository:

    ```bash
    git clone https://github.com/jwilliangp/repository-name.git
    ```

2. Install the `pyaes` dependency:

    ```bash
    pip install pyaes
    ```

3. Run the scripts:

    To encrypt the test files:

    ```bash
    python encrypter.py
    ```

    To decrypt the files:

    ```bash
    python decrypter.py
    ```

The test files will be automatically created by the `create_txt.py` script in `.txt` format. After running `encrypter.py`, the encrypted files will have the `.txt.ransomware` extension and can be restored using `decrypter.py`.

## 🛠️ Technologies

- **Python 3.x:** Programming language used to develop the project.
- **pyaes:** Python library for AES encryption.

## 📚 Project from Santander Cybersecurity Bootcamp

This project was developed as part of the **Santander Cybersecurity Bootcamp** course, aiming to apply concepts of cryptography and file security in a practical way.

## ⚠️ Important Notice

This is sample code for encrypting and decrypting files. It is **not recommended for production use** without additional security validations and key management. The use of this type of encryption on sensitive data should be done with caution and adherence to best security practices.
