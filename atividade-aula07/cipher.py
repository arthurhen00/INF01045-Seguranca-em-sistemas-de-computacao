# This has nothing to do with Valorant.
# I declare here all my hatred for Valorant,
# Riot, its players and community.

from typing import Tuple
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

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

def generate_iv() -> bytes:
    return b'\x01\x02\x03\x04\x05\x06\x07\x08'
    # return get_random_bytes(8)

def split_blocks(data: bytes, block_size: int = 8) -> list[bytes]:
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def des_cipher(
    mode: str,
    text: str,
    key: bytes,
    iv: bytes = None
) -> Tuple[bytes, list[bytes]]:
    cipher = None
    if mode == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
    elif mode == "CBC":
        cipher = DES.new(key, DES.MODE_CBC, iv)
    else:
        raise ValueError("Unsupported des mode")
    
    text_bytes = pad(text.encode("utf-8"), DES.block_size)

    encrypted_text = cipher.encrypt(text_bytes)
    encrypted_blocks = split_blocks(encrypted_text)

    return encrypted_text, encrypted_blocks

def des_cipher_decode(
    mode: str,
    ciphertext: bytes,
    blocks: list[bytes],
    key: bytes,
    iv: bytes = None
) -> Tuple[bytes, list[bytes]]:
    decrypt_cipher = None
    decrypted_message = None
    if mode == "ECB":
        decrypt_cipher = DES.new(key, DES.MODE_ECB)
    elif mode == "CBC":
        decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    else:
        raise ValueError("Unsupported des mode")
    
    decrypted_message = unpad(decrypt_cipher.decrypt(ciphertext), DES.block_size)

    if mode == "CBC": 
        decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    
    decrypted_blocks = []
    for i, block in enumerate(blocks, 1):
        decrypted_block = decrypt_cipher.decrypt(block)
        decrypted_blocks.append(decrypted_block)

    return decrypted_message, decrypted_blocks