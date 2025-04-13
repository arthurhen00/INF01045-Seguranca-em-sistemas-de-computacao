# This has nothing to do with Valorant.
# I declare here all my hatred for Valorant,
# Riot, its players and community.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from binascii import hexlify

def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
        if 32 <= ord(char) <= 126:
            new_char = chr((ord(char) - 32 + shift) % 95 + 32)
            result.append(new_char)
        else:
            print(f"Character out of ASCII range [32, 126]: {ord(char)} -> {char}")
            result.append(char)
    return ''.join(result)

def des_cbc_cipher(text: str, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv)
    text_bytes = text.encode("utf-8")
    padded_text = pad(text_bytes, DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def generate_iv() -> bytes:
    return b'\x01\x02\x03\x04\x05\x06\x07\x08'
    # return get_random_bytes(8)

def split_blocks(data, block_size=8):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def des_ecb_cipher(text: str, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    text_bytes = text.encode("utf-8")
    padded_text = pad(text_bytes, DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)

    blocks_ecb = split_blocks(encrypted_text)

    reordered_blocks = blocks_ecb[:]
    if len(reordered_blocks) < 4:
        raise Exception("Not enough blocks")

    reordered_blocks[0], reordered_blocks[3] = reordered_blocks[3], reordered_blocks[0]
    reordered_ciphertext = b"".join(reordered_blocks)
    
    print(f"\nDES ECB - Encrypted text         (hex): {hexlify(encrypted_text).decode()}")
    print(  f"DES ECB - Encrypted text C1<->C4 (hex): {hexlify(reordered_ciphertext).decode()}")

    print("\nDES ECB - Encrypted blocks (hex) / Decrypted blocks:")
    for i, block in enumerate(blocks_ecb, 1):
        decrypted_block = cipher.decrypt(block)
        print(f"C{i}: {hexlify(block).decode()} -> {decrypted_block}")

    decrypted_message = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    print(f"\nDES ECB - Decrypted text        : {decrypted_message}")
    decrypted_message = unpad(cipher.decrypt(reordered_ciphertext), DES.block_size)
    print(  f"DES ECB - Decrypted text C1<->C4: {decrypted_message}")


def des_cbc_cipher2(text: str, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    text_bytes = text.encode("utf-8")
    padded_text = pad(text_bytes, DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    
    blocks_cbc = split_blocks(encrypted_text, DES.block_size)

    reordered_blocks = blocks_cbc[:]
    if len(reordered_blocks) < 4:
        raise Exception("Not enough blocks")
    
    reordered_blocks[0], reordered_blocks[3] = reordered_blocks[3], reordered_blocks[0]
    reordered_ciphertext = b"".join(reordered_blocks)
    
    print(f"\nDES CBC - Encrypted text         (hex): {hexlify(encrypted_text).decode()}")
    print(  f"DES CBC - Encrypted text C1<->C4 (hex): {hexlify(reordered_ciphertext).decode()}")
    
    print("\nDES CBC - Encrypted blocks (hex) / Decrypted blocks:")
    for i, block in enumerate(blocks_cbc, 1):
        decrypted_block = decrypt_cipher.decrypt(block)
        print(f"C{i}: {hexlify(block).decode()} -> {decrypted_block}")

    
    decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_message = unpad(decrypt_cipher.decrypt(encrypted_text), DES.block_size)
    print(f"\nDES CBC - Decrypted text        : {decrypted_message}")
    
    decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_message = unpad(decrypt_cipher.decrypt(reordered_ciphertext), DES.block_size)
    print(  f"DES CBC - Decrypted text C1<->C4: {decrypted_message}")
    