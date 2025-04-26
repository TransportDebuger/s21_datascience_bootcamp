import sys

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        with open(self.file_path, 'r') as f:
            content = f.read()
        lines = content.strip().split('\n')
        if len(lines) < 2:
            raise ValueError("The file must contain at least the header and one data line.")
        header = lines[0].split(',')
        if len(header) != 2:
            raise ValueError("Header must consist of two comma-separated strings.")
        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f"Line '{line}' does not have exactly two comma-separated values.")
            if parts[0] not in ['0', '1'] or parts[1] not in ['0', '1']:
                raise ValueError(f"Invalid values in line '{line}'. Values must be 0 or 1.")
            if parts[0] == parts[1]:
                raise ValueError(f"Both values in line '{line}' are the same.")
        return content

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python first_constructor.py <filepath>")
        sys.exit(1)
    try:
        researcher = Research(sys.argv[1])
        print(researcher.file_reader(), end='')
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)