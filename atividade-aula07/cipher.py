# This has nothing to do with Valorant.
# I declare here all my hatred for Valorant,
# Riot, its players and community.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from typing import Union
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

def des_cbc_cipher(text: str, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv)
    text_bytes = text.encode("utf-8")
    padded_text = pad(text_bytes, DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def generate_iv() -> bytes:
    return b'\x01\x02\x03\x04\x05\x06\x07\x08'
    # return get_random_bytes(8)
