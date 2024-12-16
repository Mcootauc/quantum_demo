from cryptography.fernet import Fernet
import os
import random

# Simulated Quantum Key Distribution (BB84)
def quantum_key_distribution():
    # Step 1: Alice prepares her bits and randomly chooses bases
    alice_bits = [random.randint(0, 1) for _ in range(128)]  # Random bits (0 or 1)
    alice_bases = [random.randint(0, 1) for _ in range(128)] # Random bases (0 or 1, representing rectilinear or diagonal)

    # Step 2: Bob randomly chooses his bases to measure the incoming qubits
    bob_bases = [random.randint(0, 1) for _ in range(128)]  # Random bases (0 or 1)

    # Step 3: Bob measures qubits using his randomly chosen bases
    # If Alice's and Bob's bases match, Bob uses Alice's bit; otherwise, Bob guesses a bit
    bob_results = [alice_bits[i] if alice_bases[i] == bob_bases[i] else random.randint(0, 1) for i in range(128)]

    # Step 4: Alice and Bob publicly compare bases and discard bits where bases do not match
    key_bits = [bob_results[i] for i in range(128) if alice_bases[i] == bob_bases[i]]

    # Step 5: The remaining bits form the shared key
    key = bytes(key_bits[:32])  # Truncate to 256 bits for Fernet compatibility
    return key

def encrypt_message(message, key):
    fernet = Fernet(key)
    ciphertext = fernet.encrypt(message.encode())
    return ciphertext

def decrypt_message(ciphertext, key):
    fernet = Fernet(key)
    plaintext = fernet.decrypt(ciphertext).decode()
    return plaintext

def main():
    # Simulated Quantum Key Distribution
    qkd_key = quantum_key_distribution()

    fernet_key = Fernet.generate_key()

    # Print keys for demonstration 
    print(f'Simulated Quantum Key: {qkd_key}')
    print(f'Fernet Key: {fernet_key.decode()}')

    # Encrypting with Fernet Key
    message = 'Hello, Quantum World!'
    ciphertext = encrypt_message(message, fernet_key)
    print(f'Encrypted Message: {ciphertext.decode()}')

    decrypted_message = decrypt_message(ciphertext, fernet_key)
    print(f'Decrypted Message: {decrypted_message}')

if __name__ == '__main__':
    main()