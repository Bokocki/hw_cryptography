import argparse
import sys
from ciphers import caesar_encrypt, caesar_decrypt, morse_encrypt, morse_decrypt


def main():
    parser = argparse.ArgumentParser(
        description="A command-line tool to encrypt or decrypt messages from files.",
        epilog="Examples:\n"
        "  python main.py -e -c -n 5 input.txt output.txt\n"
        "  python main.py -d -m input.txt output.txt",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Mutually exclusive group: Must choose EITHER encrypt OR decrypt
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument(
        "-e", "--encrypt", action="store_true", help="Encrypt the input file"
    )
    action_group.add_argument(
        "-d", "--decrypt", action="store_true", help="Decrypt the input file"
    )

    # Mutually exclusive group: Must choose EITHER Caesar OR Morse
    cipher_group = parser.add_mutually_exclusive_group(required=True)
    cipher_group.add_argument(
        "-c", "--caesar", action="store_true", help="Use Caesar cipher"
    )
    cipher_group.add_argument(
        "-m", "--morse", action="store_true", help="Use Morse code"
    )

    # Shift value (only used if -c is provided)
    parser.add_argument(
        "-n",
        "--shift",
        type=int,
        default=None,
        help="Value of the right shift for Caesar cipher (required if -c is used)",
    )

    # File paths
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Requirement Check: If Caesar cipher is chosen, the shift (-n) must be provided
    if args.caesar and args.shift is None:
        parser.error("-n/--shift is required when using the Caesar cipher (-c).")

    # Read the input file
    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    # Process the text based on the selected arguments
    result_text = ""
    if args.caesar:
        if args.encrypt:
            result_text = caesar_encrypt(text, args.shift)
        elif args.decrypt:
            result_text = caesar_decrypt(text, args.shift)

    elif args.morse:
        if args.encrypt:
            result_text = morse_encrypt(text)
        elif args.decrypt:
            result_text = morse_decrypt(text)

    # Write the result to the output file
    try:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(result_text)
        print(f"Success! Processed data written to '{args.output_file}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
