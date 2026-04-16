MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

INV_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypts text using the Caesar cipher with a given right shift."""
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            # Shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result.append(shifted_char)
        else:
            # Leave non-alphabet characters (like punctuation/spaces) as they are
            result.append(char)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypts text using the Caesar cipher by reversing the shift."""
    return caesar_encrypt(text, -shift)


def morse_encrypt(text: str) -> str:
    """Encrypts text to Morse code. Words are separated by '/'."""
    encrypted = []
    for char in text.upper():
        if char == " ":
            encrypted.append("/")
        elif char in MORSE_CODE_DICT:
            encrypted.append(MORSE_CODE_DICT[char])
        else:
            # Preserve unknown characters (like newlines)
            encrypted.append(char)
    # Join with a space to separate individual morse letters
    return " ".join(encrypted)


def morse_decrypt(text: str) -> str:
    """Decrypts Morse code back to text."""
    decrypted = []
    tokens = text.split(" ")
    for token in tokens:
        if token == "/":
            decrypted.append(" ")
        elif token in INV_MORSE_DICT:
            decrypted.append(INV_MORSE_DICT[token])
        elif token == "":
            pass
        else:
            decrypted.append(token)
    return "".join(decrypted)
