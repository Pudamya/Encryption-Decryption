# Encryption and Decryption

This repository contains Python scripts for encryption and decryption of text files using substitution ciphers.

## Introduction
Encryption is the process of converting plaintext into ciphertext to secure it from unauthorized access. Decryption is the reverse process of converting ciphertext back into plaintext.

## Encryption Process
Substitution Cipher: The encryption script (enc.py) uses a simple substitution cipher to encrypt text files. Each character in the plaintext is replaced with another character according to predefined mappings.

Input: The script takes an input text file and encrypts its contents using the substitution cipher.

Output: The encrypted text is written to an output file.

## Decryption Process
Reverse Substitution: The decryption script (dec.py) reverses the substitution cipher applied during encryption to decrypt the text.

Input: The script takes an encrypted text file as input.

Output: The decrypted text is written to an output file.

## Usage
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/encryption-and-decryption.git
Navigate to the Project Directory

bash
Copy code
cd encryption-and-decryption
Encryption

Copy code
python enc.py input_file.txt encrypted_file.txt
Replace input_file.txt with the path to the plaintext input file and encrypted_file.txt with the desired output file path.

Decryption

Copy code
python dec.py encrypted_file.txt decrypted_file.txt
Replace encrypted_file.txt with the path to the encrypted input file and decrypted_file.txt with the desired output file path.

## Requirements
Python 3.x
## Contributions
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
