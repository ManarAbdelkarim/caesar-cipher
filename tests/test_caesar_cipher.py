from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_cipher():
    pins = [
        "azy",
        "MANAR" ,
        "MANAR LIKES FOOTBALL9"
  
    ]
    actual = []
    for pin in pins:
        key = random.randint(1, 26)
        encrypted_pin = encrypt2(pin, key)
        decrypted_pin = decrypt(encrypted_pin,key)
        actual.append(decrypted_pin)
    expected = [ "azy",
        "MANAR" ,
        "MANAR LIKES FOOTBALL9"]
    assert actual == expected

def test_cipher_cracker():
    word =  "It was the best of times, it was the worst of times"
    key = random.randint(1, 26)
    encrypted = encrypt2(word, key)
    actual = crack(encrypted)
    expected = word

  
  
    assert actual == expected


def test_version():
    assert __version__ == '0.1.0'