import sys

def main():
    if len(sys.argv) != 4:
        raise Exception("Error: Incorrect number of arguments")

    mode = sys.argv[1]
    text = sys.argv[2]
    shift_arg = sys.argv[3]

    if mode not in ['encode', 'decode']:
        raise Exception("Error: Invalid mode. Use 'encode' or 'decode'")

    try:
        shift = int(shift_arg)
    except ValueError:
        raise Exception("Error: Shift must be an integer")

    for c in text:
        if '\u0400' <= c <= '\u04FF':
            raise Exception("The script does not support your language yet")

    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            original = ord(c) - base
            if mode == 'encode':
                shifted = (original + shift) % 26
            else:
                shifted = (original - shift) % 26
            new_c = chr(base + shifted)
            result.append(new_c)
        else:
            result.append(c)

    print(''.join(result))

if __name__ == '__main__':
    main()