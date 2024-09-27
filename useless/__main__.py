from useless import encrypt, decrypt
import sys

def invalid_input():
    print("Usage: python -m useless <encrypt|decrypt> <key> <message>")
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        invalid_input()

    mode = sys.argv[1]

    match mode:
        case 'encrypt':
            print(encrypt(sys.argv[2], sys.argv[3]))
        case 'decrypt':
            print(decrypt(sys.argv[2], sys.argv[3]))
        case _:
            invalid_input()